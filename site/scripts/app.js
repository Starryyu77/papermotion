const state = {
  manifest: null,
  spec: null,
  scenes: [],
  activeSceneId: null,
  activeStepId: "intake",
  runTimer: null,
  running: false,
  completed: false
};

const presets = {
  formula: `Explain scaled dot-product attention from this formula for ML students:
Attention(Q,K,V) = softmax(QK^T / sqrt(d_k))V`,
  paper: `Create a short visual explainer from this paper excerpt:
Attention computes weighted values by comparing queries with keys, scaling the scores by sqrt(d_k), normalizing them with softmax, and using those weights to aggregate value vectors.`
};

const pipelineSteps = [
  {
    id: "intake",
    title: "Research intake",
    detail: "Normalize the formula, target audience, and learning goal.",
    artifact: "examples/attention/input.md",
    explanation: "The source request is converted into a bounded video task: topic, audience, learning objective, scope, and out-of-scope items.",
    output: "A clean run brief that tells later stages what the video should teach and what it must not claim.",
    log: "Source request normalized into the attention demo run."
  },
  {
    id: "mechanism",
    title: "Mechanism model",
    detail: "Extract symbols, assumptions, causal steps, and misconception guardrails.",
    artifact: "examples/attention/mechanism_spec.json",
    explanation: "PaperMotion identifies the symbols and mechanism behind the equation, then records guardrails so the video does not over-explain or invent meaning.",
    output: "A symbol ledger for Q, K, V, scaling, softmax, weights, and contextual output.",
    log: "Q, K, V, scaling, softmax, and weighted values mapped into a symbol ledger."
  },
  {
    id: "storyboard",
    title: "Storyboard",
    detail: "Turn teaching beats into five timed scenes.",
    artifact: "examples/attention/storyboard.md",
    explanation: "The teaching script is split into visual chapters so each conceptual move has one clear scene and one viewer takeaway.",
    output: "Five scenes: tokens, Q/K/V roles, similarity heatmap, softmax weights, and weighted values.",
    log: "Five-scene attention storyboard selected for the preview."
  },
  {
    id: "scene-spec",
    title: "Scene contract",
    detail: "Freeze timing, layers, narration, QA checks, and output paths.",
    artifact: "examples/attention/enriched_scene_spec.json",
    explanation: "The scene contract is the handoff between planning and rendering. It declares timing, Manim classes, optional cinematic support, assembly hints, and QA checks.",
    output: "An executable scene-level contract that the website and renderer can both inspect.",
    log: "Enriched scene spec loaded as the executable single source of truth."
  },
  {
    id: "exact-render",
    title: "Manim exact render",
    detail: "Render formulas, matrices, heatmaps, bars, and labels deterministically.",
    artifact: "manim/attention_demo.py",
    explanation: "Exact math stays in deterministic code. Manim owns the equation, matrix grids, labels, heatmap, and symbolic transformations.",
    output: "A rough but traceable MP4 demo plus scene-layer WebM artifacts.",
    log: "Pre-rendered Manim rough pass found at site/public/videos/attention-demo.mp4."
  },
  {
    id: "support",
    title: "Cinematic support",
    detail: "Reserve PixVerse for non-exact atmosphere and transitions only.",
    artifact: "examples/attention/keyframes/",
    explanation: "AI video is treated as optional support material. It can add atmosphere, abstract transitions, and non-symbolic motion, but it cannot render equations or labels.",
    output: "Provider-neutral support-shot prompts and text-free keyframes.",
    log: "Optional PixVerse support jobs prepared; exact math remains in Manim."
  },
  {
    id: "delivery",
    title: "Assembly and QA",
    detail: "Reveal the pre-generated video and linked scene evidence.",
    artifact: "site/public/videos/attention-demo.mp4",
    explanation: "The demo reveals the already-rendered video while keeping the trace visible, so the result can be reviewed against the source artifacts.",
    output: "A pre-rendered attention explainer video with clickable evidence below.",
    log: "Preview complete. Final demo video unlocked."
  }
];

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => Array.from(document.querySelectorAll(selector));

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw new Error(`Failed to load ${path}: ${response.status}`);
  return response.json();
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function formatTime(seconds = 0) {
  const rounded = Math.max(0, Math.round(Number(seconds) || 0));
  const minutes = String(Math.floor(rounded / 60)).padStart(2, "0");
  const secs = String(rounded % 60).padStart(2, "0");
  return `${minutes}:${secs}`;
}

function normalizeScenes(manifest, spec) {
  const manifestScenes = new Map((manifest.scenes || []).map((scene) => [scene.scene_id, scene]));
  const storyboardScenes = new Map((manifest.storyboard?.scenes || []).map((scene) => [scene.scene_id, scene]));

  return (spec.scenes || []).map((scene, index) => {
    const manifestScene = manifestScenes.get(scene.scene_id) || {};
    const storyboardScene = storyboardScenes.get(scene.scene_id) || {};
    return {
      id: scene.scene_id,
      index,
      title: scene.title || storyboardScene.title || scene.scene_id,
      startS: Number(scene.timestamp_start_s || manifestScene.timestamp_start_s || 0),
      durationS: Number(scene.duration_s || storyboardScene.duration_seconds || 0),
      visualType: scene.visual_type || "manim",
      narration: scene.narration || "",
      subtitle: scene.assembly?.subtitle || "",
      manimClass: scene.manim?.scene_class || "planned",
      pixverseJob: scene.pixverse?.job_id || "",
      qaChecks: scene.qa_checks || [],
      status: manifestScene.status || "planned",
      outputPath: scene.manim?.render?.output_path || ""
    };
  });
}

function renderPipeline(activeIndex = -1, completed = false) {
  $("#pipelineList").innerHTML = pipelineSteps
    .map((step, index) => {
      let status = "waiting";
      if (completed || index < activeIndex) status = "done";
      if (index === activeIndex && !completed) status = "running";
      const statusLabel = status === "done" ? "Done" : status === "running" ? "Running" : "Waiting";
      const active = state.activeStepId === step.id ? " active" : "";
      return `
        <button class="pipeline-step ${status}${active}" type="button" data-step-id="${escapeHtml(step.id)}">
          <span class="pipeline-index">${String(index + 1).padStart(2, "0")}</span>
          <div class="pipeline-copy">
            <strong>${escapeHtml(step.title)}</strong>
            <p>${escapeHtml(step.detail)}</p>
          </div>
          <em class="pipeline-status">${statusLabel}</em>
        </button>
      `;
    })
    .join("");

  $$(".pipeline-step").forEach((button) => {
    button.addEventListener("click", () => {
      setActiveStep(button.dataset.stepId);
    });
  });
}

function renderWorkflowRail() {
  $("#workflowRail").innerHTML = pipelineSteps
    .map(
      (step, index) => `
        <article class="workflow-step">
          <span>${String(index + 1).padStart(2, "0")}</span>
          <h3>${escapeHtml(step.title)}</h3>
          <p>${escapeHtml(step.detail)}</p>
          <code>${escapeHtml(step.artifact)}</code>
        </article>
      `
    )
    .join("");
}

function setActiveStep(stepId) {
  state.activeStepId = stepId;
  renderPipeline(currentRunIndex(), state.completed);
  renderStepDetail();
}

function currentRunIndex() {
  if (state.completed) return pipelineSteps.length;
  const status = $("#pipelineStatus")?.dataset.activeIndex;
  return status ? Number(status) : -1;
}

function renderStepDetail() {
  const step = pipelineSteps.find((item) => item.id === state.activeStepId) || pipelineSteps[0];
  const index = pipelineSteps.findIndex((item) => item.id === step.id);
  $("#stepDetail").innerHTML = `
    <span class="detail-label">Step ${String(index + 1).padStart(2, "0")}</span>
    <h3>${escapeHtml(step.title)}</h3>
    <p>${escapeHtml(step.explanation)}</p>
    <div class="detail-grid">
      <div class="detail-row"><span>Output</span><strong>${escapeHtml(step.output)}</strong></div>
      <div class="detail-row"><span>Artifact</span><code>${escapeHtml(step.artifact)}</code></div>
      <div class="detail-row"><span>Boundary</span><strong>${step.id === "support" ? "Cinematic only. No exact math or readable formulas." : "File-backed and reviewable."}</strong></div>
    </div>
  `;
}

function activeScene() {
  return state.scenes.find((scene) => scene.id === state.activeSceneId) || state.scenes[0];
}

function renderScenes() {
  const active = activeScene();
  $("#activeSceneBadge").textContent = active ? `Scene ${String(active.index + 1).padStart(2, "0")}` : "Scene";
  $("#sceneList").innerHTML = state.scenes
    .map((scene) => {
      const isActive = scene.id === state.activeSceneId ? " active" : "";
      return `
        <button class="scene-button${isActive}" type="button" data-scene-id="${escapeHtml(scene.id)}">
          <span>${String(scene.index + 1).padStart(2, "0")} / ${formatTime(scene.startS)}</span>
          <strong>${escapeHtml(scene.title)}</strong>
          <small>${escapeHtml(scene.visualType)} · ${escapeHtml(scene.status)}</small>
        </button>
      `;
    })
    .join("");

  $$(".scene-button").forEach((button) => {
    button.addEventListener("click", () => {
      state.activeSceneId = button.dataset.sceneId;
      renderScenes();
    });
  });

  if (!active) return;
  $("#sceneDetail").innerHTML = `
    <strong>${escapeHtml(active.title)}</strong>
    <p>${escapeHtml(active.narration)}</p>
    <dl>
      <div><dt>Timing</dt><dd>${formatTime(active.startS)} · ${active.durationS}s</dd></div>
      <div><dt>Manim</dt><dd>${escapeHtml(active.manimClass)}</dd></div>
      <div><dt>PixVerse</dt><dd>${escapeHtml(active.pixverseJob || "not used")}</dd></div>
      <div><dt>Layer</dt><dd>${escapeHtml(active.outputPath || "planned")}</dd></div>
    </dl>
  `;
}

function renderDataSummary() {
  const totalDuration = state.spec?.total_duration_s || state.scenes.reduce((sum, scene) => sum + scene.durationS, 0);
  $("#presetTitle").textContent = state.manifest?.project?.title || "Scaled Dot-Product Attention";
  $("#sceneCount").textContent = `${state.scenes.length || 5} scenes`;
  $("#durationLabel").textContent = `${totalDuration}s scene plan`;
  $("#manifestSummary").textContent =
    `${state.manifest?.project?.title || "Attention demo"} tracks source intent, storyboard scenes, PixVerse jobs, asset paths, and edit decisions.`;
  $("#specSummary").textContent =
    `${state.scenes.length} scene contracts define timing, narration, Manim classes, optional PixVerse jobs, assembly hints, and QA checks.`;
}

function appendLog(message) {
  const log = $("#consoleLog");
  const row = document.createElement("div");
  row.textContent = `[${new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" })}] ${message}`;
  log.append(row);
  log.scrollTop = log.scrollHeight;
}

function resetRun() {
  window.clearTimeout(state.runTimer);
  state.running = false;
  state.completed = false;
  $("#generateButton").disabled = false;
  $("#generateButton").textContent = "Start simulated generation";
  $("#runState").textContent = "Ready";
  $("#pipelineStatus").textContent = "Waiting for input";
  $("#pipelineStatus").dataset.activeIndex = "";
  $("#outputStatus").textContent = "Locked until run completes";
  $("#runState").className = "state-pill";
  $("#pipelineStatus").className = "state-pill";
  $("#resultShell").classList.remove("complete");
  $("#resultShell").classList.remove("playing");
  $("#consoleLog").innerHTML = "";
  const video = $("#finalVideo");
  video.pause();
  video.currentTime = 0;
  renderPipeline();
}

function completeRun() {
  state.running = false;
  state.completed = true;
  $("#generateButton").disabled = false;
  $("#generateButton").textContent = "Run simulation again";
  $("#runState").textContent = "Complete";
  $("#pipelineStatus").textContent = "All preset stages complete";
  $("#pipelineStatus").dataset.activeIndex = String(pipelineSteps.length);
  $("#outputStatus").textContent = "Pre-rendered demo unlocked";
  $("#runState").className = "state-pill complete";
  $("#pipelineStatus").className = "state-pill complete";
  $("#resultShell").classList.add("complete");
  state.activeStepId = "delivery";
  renderPipeline(pipelineSteps.length, true);
  renderStepDetail();
  const video = $("#finalVideo");
  video.pause();
  video.currentTime = 0;
}

function startRun() {
  if (state.running) return;
  resetRun();
  state.running = true;
  $("#generateButton").disabled = true;
  $("#generateButton").textContent = "Simulating...";
  $("#runState").textContent = "Running";
  $("#runState").className = "state-pill running";
  $("#pipelineStatus").className = "state-pill running";
  appendLog(`Input accepted: ${$("#sourceInput").value.trim().slice(0, 90)}...`);

  let index = 0;
  const tick = () => {
    const step = pipelineSteps[index];
    if (!step) {
      completeRun();
      appendLog("Pre-rendered attention demo is now available.");
      return;
    }

    $("#pipelineStatus").textContent = step.title;
    $("#pipelineStatus").dataset.activeIndex = String(index);
    state.activeStepId = step.id;
    renderPipeline(index);
    renderStepDetail();
    appendLog(step.log);
    index += 1;
    state.runTimer = window.setTimeout(tick, index === pipelineSteps.length ? 720 : 620);
  };

  tick();
}

function wireControls() {
  $("#generateButton")?.addEventListener("click", startRun);
  $("#resultCover")?.addEventListener("click", () => {
    const video = $("#finalVideo");
    $("#resultShell").classList.add("playing");
    video.currentTime = 0;
    video.play();
  });
  $$("[data-preset]").forEach((button) => {
    button.addEventListener("click", () => {
      $("#sourceInput").value = presets[button.dataset.preset] || presets.formula;
      $("#sourceInput").focus();
    });
  });
}

async function init() {
  wireControls();
  renderPipeline();
  renderWorkflowRail();
  renderStepDetail();

  try {
    const [manifest, spec] = await Promise.all([
      loadJson("./data/production_manifest.json"),
      loadJson("./data/enriched_scene_spec.json")
    ]);
    state.manifest = manifest;
    state.spec = spec;
    state.scenes = normalizeScenes(manifest, spec);
    state.activeSceneId = state.scenes[0]?.id;
    renderDataSummary();
    renderScenes();
  } catch (error) {
    $("#pipelineStatus").textContent = "Data load failed";
    appendLog(error.message);
  }
}

init();
