# PaperMotion Trae Install Prompt

Use this prompt when installing PaperMotion from GitHub inside Trae Solo.

```text
你是 Trae Solo。请把下面这个 GitHub 仓库作为 PaperMotion skill pack / SKU 安装到本地工作区：

<PASTE_GITHUB_REPO_URL_HERE>

安装步骤：

1. Clone 仓库，进入仓库根目录。
2. 阅读 `papermotion.sku.json`、`README.md`、`docs/install.md`、`docs/execution-summary.md`。
3. 以 `papermotion.sku.json.skills[]` 作为唯一权威 skill 列表；不要用目录 glob 代替 SKU。
4. 对 `skills[]` 里的每个 `SKILL.md`，读取 frontmatter 的 `name` 和 `description`，并用这些元数据注册或加载 Trae skill。
5. root skill 是：
   `skills/papermotion-research-video/SKILL.md`
6. 当 `skills[]` 中的 skill 已成功注册或可按需加载，并且 root skill 可用时，PaperMotion 安装完成。
7. 安装完成后可运行 post-install validation：
   `./setup.sh --check-only`
8. 只有在需要创建或刷新本地验证环境时，才运行完整 validation backend：
   `./setup.sh`
9. 如果用户需要本地数学动画渲染，再运行：
   `./setup.sh --with-manim`
10. 如果用户需要检查可选网页展示层，再运行：
   `./setup.sh --with-site`
11. 完成后，把以下内容告诉用户：
   - repo 安装路径
   - `papermotion.sku.json.skills[]` 中每个 skill 的注册/加载状态
   - root skill 是否可用
   - post-install validation 是否运行及是否成功
   - 已发现的 examples
   - 可用 skills
   - 下一步建议

重要约束：

- 不要把网站当作默认产品路径。
- 默认目标是科研视频 skill workflow / skill pack。
- 使用 `docs/dynamic-scene-model.md` 和 `contracts/dynamic_scene_model.schema.json` 来生成或修复 `dynamic_scene_model.json`。
- 精确公式、标签、坐标轴、矩阵、图结构必须交给确定性 renderer。
- AI video provider 只能用于非精确 cinematic support。
- 所有阶段都要落到 repo 文件里，不要只保留在对话里。
```
