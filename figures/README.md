# 图

用 [archify](https://github.com/tt-a1i/archify) 生成的交互式 HTML 图（内联 SVG，含明暗主题、搜索聚焦、关系追踪、导出）。

| 图 | 类型 | 源 | 被谁引用 |
|---|---|---|---|
| [radar-structure.html](radar-structure.html) | architecture | [radar-structure.architecture.json](radar-structure.architecture.json) | [../README.md](../README.md#结构四条腿) |
| [deeplesion-lineage.html](deeplesion-lineage.html) | dataflow | [deeplesion-lineage.dataflow.json](deeplesion-lineage.dataflow.json) | [../sources/radar-vs-medsam.md](../sources/radar-vs-medsam.md) |

## SSoT

**JSON 是唯一的图源，HTML 是产物。** 不要手改 HTML，也不要在 markdown 里另写一份 ASCII 版——那会立刻变成第二份会过期的真相。

改图：

```bash
S=~/.claude/skills/archify
node $S/bin/archify.mjs validate architecture radar-structure.architecture.json --quality showcase --json
node $S/bin/archify.mjs deliver  architecture radar-structure.architecture.json radar-structure.html --quality showcase --json
node $S/bin/archify.mjs visual-check radar-structure.html --json
```

两张图都通过了 showcase 全部 9 项 artifact 检查（0 错误 0 警告），以及 1440×900 / 1600×1000 / 1920×1080 三档桌面视口的浏览器 overflow 检查。
**浏览器自动化证据 ≠ 人眼审美复核** —— 后者没做。

## 已知取舍

- 中文副标题被压到 6–9 个字，是为了满足 archify 的 6px 最小投影字号要求；被删掉的细节（比如 DeepLesion 的完整作者名单）移进了图下方的卡片。
- 图里的 SVG 用的是文档级 CSS 类，**单独抽出 `.svg` 会掉样式**，所以没有导出静态图。要 PNG/SVG 请在浏览器里打开 HTML 用自带的导出。
