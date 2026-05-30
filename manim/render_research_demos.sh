#!/usr/bin/env bash
set -euo pipefail

SCRIPT="research_video_demos.py"
OUTPUT_ROOT="../site/public/videos"
QUALITY="${2:--ql}"

MANIM_BIN="manim"
if [[ -x "../.venv/bin/manim" ]]; then
  MANIM_BIN="../.venv/bin/manim"
fi

FFMPEG_BIN="ffmpeg"

usage() {
  cat <<'USAGE'
Usage:
  ./render_research_demos.sh [all|adam|ddpm|nerf] [-ql|-qm|-qh]

Outputs:
  ../site/public/videos/adam-optimizer-demo.mp4
  ../site/public/videos/ddpm-denoising-demo.mp4
  ../site/public/videos/nerf-volume-rendering-demo.mp4
USAGE
}

scene_for_target() {
  case "$1" in
    adam) echo "AdamOptimizerDemo" ;;
    ddpm) echo "DDPMDenoisingDemo" ;;
    nerf) echo "NeRFVolumeRenderingDemo" ;;
    *) return 1 ;;
  esac
}

video_for_target() {
  case "$1" in
    adam) echo "adam-optimizer-demo.mp4" ;;
    ddpm) echo "ddpm-denoising-demo.mp4" ;;
    nerf) echo "nerf-volume-rendering-demo.mp4" ;;
    *) return 1 ;;
  esac
}

poster_for_target() {
  case "$1" in
    adam) echo "adam-optimizer-demo-poster.jpg" ;;
    ddpm) echo "ddpm-denoising-demo-poster.jpg" ;;
    nerf) echo "nerf-volume-rendering-demo-poster.jpg" ;;
    *) return 1 ;;
  esac
}

quality_dir_for_flag() {
  case "$1" in
    -ql) echo "480p15" ;;
    -qm) echo "720p30" ;;
    -qh) echo "1080p60" ;;
    *) return 1 ;;
  esac
}

render_one() {
  local target="$1"
  local scene
  local video
  local poster
  local rendered
  local tmp_video
  local quality_dir
  scene="$(scene_for_target "$target")"
  video="$(video_for_target "$target")"
  poster="$(poster_for_target "$target")"
  quality_dir="$(quality_dir_for_flag "$QUALITY")"

  echo "Rendering $scene ($QUALITY) ..."
  "$MANIM_BIN" "$QUALITY" --disable_caching "$SCRIPT" "$scene"

  rendered="media/videos/research_video_demos/${quality_dir}/${scene}.mp4"
  if [[ ! -f "$rendered" ]]; then
    echo "Could not locate expected rendered MP4: $rendered" >&2
    exit 1
  fi

  mkdir -p "$OUTPUT_ROOT"
  tmp_video="$OUTPUT_ROOT/.${video}.tmp.mp4"
  "$FFMPEG_BIN" -y -hide_banner -loglevel error \
    -i "$rendered" \
    -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2,fps=30" \
    -c:v libx264 -profile:v main -pix_fmt yuv420p -movflags +faststart \
    -an "$tmp_video"
  mv "$tmp_video" "$OUTPUT_ROOT/$video"

  "$FFMPEG_BIN" -y -hide_banner -loglevel error \
    -ss 00:00:07 \
    -i "$OUTPUT_ROOT/$video" \
    -frames:v 1 -q:v 3 "$OUTPUT_ROOT/$poster"

  echo "Wrote $OUTPUT_ROOT/$video"
  echo "Wrote $OUTPUT_ROOT/$poster"
}

TARGET="${1:-all}"
case "$TARGET" in
  all)
    render_one adam
    render_one ddpm
    render_one nerf
    ;;
  adam|ddpm|nerf)
    render_one "$TARGET"
    ;;
  -h|--help|help)
    usage
    ;;
  *)
    usage
    exit 1
    ;;
esac
