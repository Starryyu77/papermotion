#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

WITH_MANIM=0
WITH_SITE=0
CHECK_ONLY=0

usage() {
  cat <<'EOF'
PaperMotion setup backend

Usage:
  ./setup.sh [options]

Options:
  --with-manim     Install Manim into .venv. This may need system libraries.
  --with-site      Run optional site build checks.
  --check-only     Do not install; only validate the current environment and examples.
  -h, --help       Show this help.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --with-manim) WITH_MANIM=1 ;;
    --with-site) WITH_SITE=1 ;;
    --check-only) CHECK_ONLY=1 ;;
    --skip-site) WITH_SITE=0 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
  shift
done

say() {
  printf '\n==> %s\n' "$1"
}

warn() {
  printf 'warn: %s\n' "$1" >&2
}

have() {
  command -v "$1" >/dev/null 2>&1
}

can_import_jsonschema() {
  "$1" - <<'PY' >/dev/null 2>&1
import jsonschema
PY
}

PYTHON_BIN=""

if [[ "$CHECK_ONLY" -eq 0 ]]; then
  say "Create Python environment"
  if have uv; then
    uv venv .venv
    PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
    uv pip install --python "$PYTHON_BIN" jsonschema
    if [[ "$WITH_MANIM" -eq 1 ]]; then
      uv pip install --python "$PYTHON_BIN" manim
    fi
  else
    if ! have python3; then
      echo "python3 is required when uv is not installed." >&2
      exit 1
    fi
    python3 -m venv .venv
    PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
    "$PYTHON_BIN" -m pip install --upgrade pip
    "$PYTHON_BIN" -m pip install jsonschema
    if [[ "$WITH_MANIM" -eq 1 ]]; then
      "$PYTHON_BIN" -m pip install manim
    fi
  fi

  say "Create local env file"
  if [[ ! -f .env.local ]]; then
    cp .env.example .env.local
    echo "Created .env.local from .env.example"
  else
    echo ".env.local already exists"
  fi
else
  if [[ -x "$ROOT_DIR/.venv/bin/python" ]] && can_import_jsonschema "$ROOT_DIR/.venv/bin/python"; then
    PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
  elif have python3 && can_import_jsonschema "$(command -v python3)"; then
    PYTHON_BIN="$(command -v python3)"
  else
    echo "No Python runtime with jsonschema found. Run ./setup.sh to create a local validation environment." >&2
    exit 1
  fi
fi

say "Check runtime tools"
"$PYTHON_BIN" - <<'PY'
import jsonschema
print("python/jsonschema ok")
PY

if have ffmpeg; then
  echo "ffmpeg ok: $(ffmpeg -version 2>/dev/null | head -n 1)"
else
  warn "ffmpeg not found; final video assembly/export will be limited."
fi

if have node; then
  echo "node ok: $(node --version)"
else
  warn "node not found; Remotion/site checks will be skipped."
fi

if have manim; then
  echo "manim ok: $(manim --version 2>/dev/null | head -n 1)"
elif [[ -x "$ROOT_DIR/.venv/bin/manim" ]]; then
  echo "manim ok: $("$ROOT_DIR/.venv/bin/manim" --version 2>/dev/null | head -n 1)"
else
  warn "manim not found; run ./setup.sh --with-manim if you need local exact-animation rendering."
fi

say "Validate dynamic scene models"
found=0
while IFS= read -r model_path; do
  found=1
  "$PYTHON_BIN" scripts/validate_dynamic_scene_model.py "$model_path"
done < <(find examples -name dynamic_scene_model.json -print | sort)

if [[ "$found" -eq 0 ]]; then
  warn "No dynamic_scene_model.json files found."
fi

if [[ "$WITH_SITE" -eq 1 && -f site/package.json ]]; then
  say "Check optional site package"
  if have npm; then
    npm --prefix site run build
  else
    echo "npm is required for --with-site." >&2
    exit 1
  fi
fi

say "Setup complete"
echo "Next: open this repo in Trae Solo and start from docs/execution-summary.md"
