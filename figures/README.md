# 图

用 [archify](https://github.com/tt-a1i/archify) 生成的交互式 HTML 图（内联 SVG，含明暗主题、搜索聚焦、关系追踪、演示模式、导出）。
markdown 里内嵌的是静态 PNG 导出；要交互版就本地打开对应的 `.html`。

| 图 | 类型 | 图源（唯一真源） | 静态导出 | 被谁引用 |
|---|---|---|---|---|
| [radar-structure.html](radar-structure.html) | architecture | [radar-structure.architecture.json](radar-structure.architecture.json) | `radar-structure.{light,dark}.png` | [../README.md](../README.md#结构四条腿) |
| [deeplesion-lineage.html](deeplesion-lineage.html) | dataflow | [deeplesion-lineage.dataflow.json](deeplesion-lineage.dataflow.json) | `deeplesion-lineage.{light,dark}.png` | [../sources/radar-vs-medsam.md](../sources/radar-vs-medsam.md) |

## SSoT

**JSON 是唯一图源；HTML 和 PNG 都是产物。** 不要手改 HTML 或 PNG，也不要在 markdown 里另写一份 ASCII 版 —— 那会立刻变成第二份会过期的真相。

改图三步：

```bash
S=~/.claude/skills/archify
node $S/bin/archify.mjs validate architecture radar-structure.architecture.json --quality showcase --json
node $S/bin/archify.mjs deliver  architecture radar-structure.architecture.json radar-structure.html --quality showcase --json
node $S/bin/archify.mjs visual-check radar-structure.html --json
python3 export-png.py radar-structure          # 重新导出 PNG
```

## PNG 是怎么导的

`archify` 的导出是浏览器里的 viewer 功能，没有 CLI 接口。[export-png.py](export-png.py) 的做法是：
复制一份 HTML → 注入 CSS 隐掉 viewer 外壳（工具栏、导览条、各种浮层）并强制 `data-theme` →
Chrome headless `--screenshot`（`--force-device-scale-factor=2` 出 2× 高清）→ PIL 自动裁掉四周留白。

⚠️ 每张图的导出窗口宽度写在脚本的 `WINDOW` 表里。**窗口比图宽会在面板右侧留下一条空白**，
换了 viewBox 宽高就要同步调这个值，然后肉眼看一眼。

## 验收状态

两张图都通过 archify showcase 的全部 9 项 artifact 检查（0 错误 0 警告），以及
1440×900 / 1600×1000 / 1920×1080 / 2048×1320 四档桌面视口的浏览器 overflow 检查（`*.visual-check.json` 是收据）。

**自动化浏览器证据 ≠ 人眼审美复核。** 后者我做了（看了导出的 PNG），并因此改掉了谱系图第一版
两行之间空一整条、标题折两行的问题 —— 这类问题自动检查全过，只有看图才能发现。

## 已知取舍

- 中文副标题被压到 6–9 个字，是为了满足 archify 的 6px 最小投影字号要求；被删掉的细节
  （比如 DeepLesion 的完整作者名单）移进了图下方的卡片，没有丢。
- 谱系图里**故意不画** DeepLesion → RADAR 的箭头：画了就暗示有数据通路，而事实是只有人跨过去。
- `*.visual-check.*.png` 与 `*.visual-check.html` 是可重生的副产品，已在 `.gitignore` 里排除。
