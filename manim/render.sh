#!/usr/bin/env bash
# PaperMotion – Manim render helper
# Usage:
#   ./render.sh demo     # render one stitched rough demo scene
#   ./render.sh          # render all 5 transparent scene layers at low quality
#   ./render.sh hq       # render at 1080p60 high quality
#   ./render.sh s01      # render a single scene

set -euo pipefail
cd "$(dirname "$0")"

SCRIPT="attention_demo.py"
OUTPUT_ROOT="../site/public/videos/scenes"
SCENES=(
  TokensAskForContext
  QKVRoles
  SimilarityHeatmap
  SoftmaxToWeights
  WeightedValuesBecomeContext
)

if [[ $# -eq 0 ]]; then
  QUALITY="-ql"
  TARGET="all"
elif [[ "$1" == "demo" ]]; then
  QUALITY="-ql"
  TARGET="demo"
elif [[ "$1" == "hq" ]]; then
  QUALITY="-qh"
  TARGET="all"
else
  QUALITY="-ql"
  TARGET="$1"
fi

mkdir -p "$OUTPUT_ROOT" "../site/public/videos/assembled"

render_scene() {
  local scene="$1"
  local output_name="$2"
  echo "Rendering $scene ($QUALITY) ..."
  manim $QUALITY --disable_caching --transparent --format=webm "$SCRIPT" "$scene"
  local rendered
  rendered="$(find media/videos/attention_demo -type f -name "${scene}.webm" -print | sort | tail -n 1 || true)"
  if [[ -n "$rendered" ]]; then
    cp "$rendered" "$OUTPUT_ROOT/${output_name}.webm"
    echo "Copied $scene to $OUTPUT_ROOT/${output_name}.webm"
  else
    echo "Rendered $scene, but no webm output was found under media/videos/attention_demo."
  fi
}

if [[ "$TARGET" == "all" ]]; then
  render_scene TokensAskForContext s01_tokens_context
  render_scene QKVRoles s02_qkv_roles
  render_scene SimilarityHeatmap s03_similarity_heatmap
  render_scene SoftmaxToWeights s04_softmax_weights
  render_scene WeightedValuesBecomeContext s05_weighted_values
  echo ""
  echo "All scene layers rendered. Synced copies live in: $OUTPUT_ROOT/"
elif [[ "$TARGET" == "demo" ]]; then
  echo "Rendering AttentionDemo rough pass ($QUALITY) ..."
  manim $QUALITY --disable_caching "$SCRIPT" AttentionDemo
  demo_rendered="$(find media/videos/attention_demo -type f -name "AttentionDemo.mp4" -print | sort | tail -n 1 || true)"
  if [[ -n "$demo_rendered" ]]; then
    cp "$demo_rendered" "../site/public/videos/attention-demo.mp4"
    echo "Copied AttentionDemo to ../site/public/videos/attention-demo.mp4"
  else
    echo "AttentionDemo rendered, but no mp4 output was found under media/videos/attention_demo."
  fi
else
  case "$TARGET" in
    s01|TokensAskForContext)
      render_scene TokensAskForContext s01_tokens_context
      ;;
    s02|QKVRoles)
      render_scene QKVRoles s02_qkv_roles
      ;;
    s03|SimilarityHeatmap)
      render_scene SimilarityHeatmap s03_similarity_heatmap
      ;;
    s04|SoftmaxToWeights)
      render_scene SoftmaxToWeights s04_softmax_weights
      ;;
    s05|WeightedValuesBecomeContext)
      render_scene WeightedValuesBecomeContext s05_weighted_values
      ;;
    *)
      render_scene "$TARGET" "$TARGET"
      ;;
  esac
fi
