const state = {
  manifest: null,
  spec: null,
  scenes: [],
  activeSceneId: null,
  activeToken: "softmax",
  activePanel: "formula",
  pixverseRuns: new Map()
};

const tokenNotes = {
  Q: {
    label: "Query",
    text: "Q is the question a token asks: which other tokens matter to me right now?",
    sceneId: "s02",
    boundary: "Manim owns the exact Q role split and labels."
  },
  K: {
    label: "Key",
    text: "K is what each token offers as an answerable address. Q compares against K to form relevance scores.",
    sceneId: "s02",
    boundary: "PixVerse can show atmosphere, but readable key labels stay in Manim."
  },
  V: {
    label: "Value",
    text: "V carries the information that will be mixed once attention weights are known.",
    sceneId: "s05",
    boundary: "The weighted sum is exact Manim; PixVerse can support the convergence mood."
  },
  QK: {
    label: "QK^T",
    text: "QK^T creates a table of pairwise relevance scores between queries and keys.",
    sceneId: "s03",
    boundary: "The heatmap and matrix semantics must be rendered by Manim."
  },
  scale: {
    label: "sqrt(d_k)",
    text: "Scaling keeps raw scores from becoming too sharp before softmax normalizes them.",
    sceneId: "s03",
    boundary: "PixVerse must not invent equations; it may only support the cooling transition."
  },
  softmax: {
    label: "softmax",
    text: "Softmax turns relevance scores into proportions, so the values can be mixed by weight.",
    sceneId: "s04",
    boundary: "The normalization bars and sum-to-one claim stay in Manim."
  },
  context: {
    label: "Context output",
    text: "The output token carries a weighted blend of value vectors from the tokens it attended to.",
    sceneId: "s05",
    boundary: "PixVerse can show convergence; exact vector mixing remains Manim."
  }
};

const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => Array.from(document.querySelectorAll(selector));

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load ${path}: ${response.status}`);
  }
  return response.json();
}

function formatTime(seconds = 0) {
  const whole = Math.max(0, Math.round(seconds));
  const minutes = String(Math.floor(whole / 60)).padStart(2, "0");
  const secs = String(whole % 60).padStart(2, "0");
  return `${minutes}:${secs}`;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function normalizeScenes(manifest, spec) {
  const manifestById = new Map((manifest.scenes || []).map((scene) => [scene.scene_id, scene]));
  const storyboardById = new Map((manifest.storyboard?.scenes || []).map((scene) => [scene.scene_id, scene]));
  const beatsById = new Map((manifest.script?.beats || []).map((beat) => [beat.beat_id, beat]));
  const jobsById = new Map((manifest.pixverse_jobs || []).map((job) => [job.job_id, job]));

  return (spec.scenes || []).map((scene, index) => {
    const manifestScene = manifestById.get(scene.scene_id) || {};
    const storyboard = storyboardById.get(scene.scene_id) || {};
    const activeBeats = (scene.linked_beats || []).map((beatId) => beatsById.get(beatId)).filter(Boolean);
    const manifestPixverse = scene.pixverse?.job_id ? jobsById.get(scene.pixverse.job_id) : null;
    return {
      id: scene.scene_id,
      index,
      title: scene.title || storyboard.title || scene.scene_id,
      startS: Number(scene.timestamp_start_s || 0),
      durationS: Number(scene.duration_s || storyboard.duration_seconds || 0),
      endS: Number(scene.timestamp_start_s || 0) + Number(scene.duration_s || storyboard.duration_seconds || 0),
      narration: scene.narration || activeBeats.map((beat) => beat.spoken_text).join(" "),
      subtitle: scene.assembly?.subtitle || "",
      visualType: scene.visual_type || "manim",
      isInsightMoment: Boolean(scene.insight_moment),
      pacing: scene.pacing || "medium",
      renderLayers: manifestScene.render_layer || [],
      manifestStatus: manifestScene.status || "planned",
      storyboard,
      activeBeats,
      manim: scene.manim || null,
      pixverse: scene.pixverse || null,
      manifestPixverse,
      tts: scene.tts || {},
      musicCue: scene.music_cue || {},
      assembly: scene.assembly || {},
      qaChecks: scene.qa_checks || []
    };
  });
}

function setActivePanel(panelName) {
  state.activePanel = panelName;
  $$(".tab").forEach((tab) => tab.classList.toggle("active", tab.dataset.panel === panelName));
  $$(".switcher-item").forEach((item) => {
    item.classList.toggle("active", item.dataset.panel === panelName || (item.dataset.panel === "formula" && panelName === "formula"));
  });
  $$(".panel").forEach((panel) => panel.classList.toggle("active", panel.id === `panel-${panelName}`));
  openInspector();
}

function openInspector() {
  const drawer = $("#inspectorDrawer");
  drawer.classList.add("open");
  drawer.setAttribute("aria-hidden", "false");
  drawer.removeAttribute("inert");
}

function closeInspector() {
  const drawer = $("#inspectorDrawer");
  drawer.classList.remove("open");
  drawer.setAttribute("aria-hidden", "true");
  drawer.setAttribute("inert", "");
}

function setActiveToken(token, options = {}) {
  state.activeToken = token;
  $$("[data-token]").forEach((button) => button.classList.toggle("active", button.dataset.token === token));
  const note = tokenNotes[token] || tokenNotes.softmax;
  $("#formulaNote").textContent = `${note.label}: ${note.text}`;
  if (options.jumpToLinkedScene && note.sceneId) {
    setActiveScene(note.sceneId, { preserveToken: true });
  } else {
    renderInspector();
  }
}

function setActiveScene(sceneId, options = {}) {
  const scene = state.scenes.find((item) => item.id === sceneId) || state.scenes[0];
  state.activeSceneId = scene.id;
  if (!options.preserveToken) {
    state.activeToken = tokenForScene(scene.id);
  }
  render();
}

function tokenForScene(sceneId) {
  if (sceneId === "s01") return "Q";
  if (sceneId === "s02") return "K";
  if (sceneId === "s03") return "QK";
  if (sceneId === "s04") return "softmax";
  if (sceneId === "s05") return "context";
  return "softmax";
}

function activeScene() {
  return state.scenes.find((scene) => scene.id === state.activeSceneId) || state.scenes[0];
}

function renderChapters() {
  const rail = $("#chapterRail");
  rail.innerHTML = state.scenes
    .map((scene) => {
      const active = scene.id === state.activeSceneId ? " active" : "";
      return `
        <button class="chapter-button${active}" type="button" data-scene-id="${scene.id}">
          <small>${String(scene.index + 1).padStart(2, "0")} ${formatTime(scene.startS)}</small>
          <strong>${escapeHtml(scene.title)}</strong>
        </button>
      `;
    })
    .join("");

  $$(".chapter-button").forEach((button) => {
    button.addEventListener("click", () => setActiveScene(button.dataset.sceneId));
  });
}

function renderMain() {
  const scene = activeScene();
  if (!scene) return;
  $("#activeSceneTitle").textContent = scene.title;
  $("#activeNarration").textContent = scene.narration;
  $("#sceneTimecode").textContent = `${formatTime(scene.startS)} / ${formatTime(state.spec.total_duration_s)}`;
  $("#projectStatus").textContent = `${state.manifest.project.status} / ${scene.manifestStatus}`;
  setActiveToken(state.activeToken, { jumpToLinkedScene: false });
}

function renderInspector() {
  const scene = activeScene();
  if (!scene) return;
  renderFormulaPanel(scene);
  renderSpecPanel(scene);
  renderPixversePanel(scene);
}

function renderFormulaPanel(scene) {
  const token = tokenNotes[state.activeToken] || tokenNotes.softmax;
  $("#panel-formula").innerHTML = `
    <article class="inspector-card">
      <span class="mini-label">Active Symbol</span>
      <h2>${escapeHtml(token.label)}</h2>
      <p>${escapeHtml(token.text)}</p>
    </article>
    <article class="inspector-card">
      <h3>Linked Scene</h3>
      <div class="kv-grid">
        <div class="kv-row"><span>Scene</span><strong>${escapeHtml(scene.id)} - ${escapeHtml(scene.title)}</strong></div>
        <div class="kv-row"><span>Visual type</span><code>${escapeHtml(scene.visualType)}</code></div>
        <div class="kv-row"><span>Manim</span><code>${escapeHtml(scene.manim?.scene_class || "planned")}</code></div>
        <div class="kv-row"><span>Boundary</span><p>${escapeHtml(token.boundary)}</p></div>
      </div>
    </article>
    <article class="inspector-card">
      <h3>Teaching Beat</h3>
      <p>${escapeHtml(scene.activeBeats[0]?.spoken_text || scene.narration)}</p>
    </article>
  `;
}

function renderSpecPanel(scene) {
  const objects = (scene.manim?.objects || []).map((object) => object.id || object.type).join(", ") || "planned";
  const actions = (scene.manim?.animation_sequence || [])
    .slice(0, 4)
    .map((action) => `${action.action}: ${action.target || action.description || "step"} (${action.run_time}s)`)
    .join("\n");
  $("#panel-spec").innerHTML = `
    <article class="inspector-card">
      <span class="mini-label">Scene Contract</span>
      <h2>${escapeHtml(scene.title)}</h2>
      <div class="kv-grid">
        <div class="kv-row"><span>Timing</span><code>${formatTime(scene.startS)} - ${formatTime(scene.endS)} (${scene.durationS}s)</code></div>
        <div class="kv-row"><span>Narration</span><code>${scene.tts?.pause_before_s ?? 0}s in / ${scene.narration_duration_s || scene.durationS}s voice</code></div>
        <div class="kv-row"><span>Pacing</span><code>${escapeHtml(scene.pacing)}${scene.isInsightMoment ? " / insight" : ""}</code></div>
        <div class="kv-row"><span>Objects</span><p>${escapeHtml(objects)}</p></div>
      </div>
    </article>
    <article class="inspector-card">
      <h3>Animation Sequence</h3>
      <pre class="code-box">${escapeHtml(actions || "No Manim steps declared yet.")}</pre>
    </article>
    <article class="inspector-card">
      <h3>QA Checks</h3>
      <div class="badge-row">
        ${scene.qaChecks.map((check) => `<span class="badge blue">${escapeHtml(check)}</span>`).join("") || '<span class="badge amber">QA pending</span>'}
      </div>
    </article>
  `;
}

function renderPixversePanel(scene) {
  const pixverse = scene.pixverse;
  const run = pixverse?.job_id ? state.pixverseRuns.get(pixverse.job_id) : null;
  if (!pixverse) {
    $("#panel-pixverse").innerHTML = `
      <article class="inspector-card">
        <span class="mini-label">PixVerse Boundary</span>
        <h2>Not used in this scene</h2>
        <p>This scene relies on the Manim exact layer. PixVerse is reserved for cinematic support, transitions, and atmosphere.</p>
      </article>
    `;
    return;
  }

  const status = run?.status || pixverse.status || scene.manifestPixverse?.status || "proposed";
  const stateClass = status === "generating" || status === "polling" ? "generating" : "";
  $("#panel-pixverse").innerHTML = `
    <article class="inspector-card">
      <span class="mini-label">Support Shot</span>
      <h2>${escapeHtml(pixverse.job_id)}</h2>
      <div class="kv-grid">
        <div class="kv-row"><span>Mode</span><code>${escapeHtml(pixverse.mode)}</code></div>
        <div class="kv-row"><span>Duration</span><code>${pixverse.duration_s || scene.manifestPixverse?.duration_seconds || 4}s</code></div>
        <div class="kv-row"><span>Status</span><strong>${escapeHtml(status)}</strong></div>
      </div>
      <div class="queue-state ${stateClass}">
        <strong>${escapeHtml(run?.video_id || "No video ID yet")}</strong>
        <span>${escapeHtml(run?.message || "Ready to request a cinematic support clip.")}</span>
      </div>
      <button class="generate-button" type="button" data-generate-job="${escapeHtml(pixverse.job_id)}">
        Generate Support Shot
      </button>
    </article>
    <article class="inspector-card">
      <h3>Prompt</h3>
      <pre class="code-box">${escapeHtml(pixverse.prompt)}</pre>
    </article>
    <article class="inspector-card">
      <h3>Must Not Include</h3>
      <div class="badge-row">
        ${(pixverse.must_not_include || []).map((item) => `<span class="badge amber">${escapeHtml(item)}</span>`).join("")}
      </div>
    </article>
  `;

  const button = $("[data-generate-job]");
  button?.addEventListener("click", () => generatePixverse(scene));
}

async function generatePixverse(scene) {
  const pixverse = scene.pixverse;
  if (!pixverse) return;
  state.pixverseRuns.set(pixverse.job_id, {
    status: "generating",
    video_id: "pending",
    message: "Queued through local server adapter."
  });
  renderPixversePanel(scene);

  try {
    const response = await fetch("/api/pixverse/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ scene_id: scene.id, job: pixverse })
    });
    const result = await response.json();
    state.pixverseRuns.set(pixverse.job_id, {
      status: "polling",
      video_id: result.video_id,
      message: result.message || "Generation submitted. Polling mock status."
    });
    renderPixversePanel(scene);

    setTimeout(async () => {
      const statusResponse = await fetch(`/api/pixverse/status/${encodeURIComponent(result.video_id)}`);
      const status = await statusResponse.json();
      state.pixverseRuns.set(pixverse.job_id, {
        status: status.status,
        video_id: status.video_id,
        message: status.message || "Mock clip ready for preview wiring."
      });
      renderPixversePanel(activeScene());
    }, 900);
  } catch (error) {
    state.pixverseRuns.set(pixverse.job_id, {
      status: "failed",
      video_id: "local-error",
      message: error.message
    });
    renderPixversePanel(scene);
  }
}

function render() {
  renderMain();
  renderChapters();
  renderInspector();
}

function wireStaticControls() {
  $$(".tab").forEach((tab) => {
    tab.addEventListener("click", () => setActivePanel(tab.dataset.panel));
  });
  $$(".switcher-item").forEach((item) => {
    item.addEventListener("click", () => setActivePanel(item.dataset.panel));
  });
  $$("[data-token]").forEach((button) => {
    button.addEventListener("click", () => setActiveToken(button.dataset.token, { jumpToLinkedScene: true }));
  });
  $("#inspectButton")?.addEventListener("click", () => openInspector());
  $("#openInspectorFromStrip")?.addEventListener("click", () => openInspector());
  $("#closeInspector")?.addEventListener("click", () => closeInspector());
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeInspector();
  });
  const clock = $("#clock");
  const updateClock = () => {
    clock.textContent = new Intl.DateTimeFormat([], { hour: "2-digit", minute: "2-digit" }).format(new Date());
  };
  updateClock();
  setInterval(updateClock, 30000);
}

async function init() {
  wireStaticControls();
  try {
    const [manifest, spec] = await Promise.all([
      loadJson("./data/production_manifest.json"),
      loadJson("./data/enriched_scene_spec.json")
    ]);
    state.manifest = manifest;
    state.spec = spec;
    state.scenes = normalizeScenes(manifest, spec);
    state.activeSceneId = state.scenes[0]?.id;
    state.activeToken = tokenForScene(state.activeSceneId);
    render();
  } catch (error) {
    $("#activeSceneTitle").textContent = "Data load failed";
    $("#activeNarration").textContent = error.message;
  }
}

init();
