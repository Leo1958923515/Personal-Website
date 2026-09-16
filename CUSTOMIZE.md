# GitHub 个人主页 README · 使用与替换指南

风格参考：<https://github.com/Lain-Ego0> —— Typing SVG 头部 + 胶囊徽章 + About Me（含中文折叠）
+ Current Work + 代表项目 + 分组技能徽章 + 联系方式 + 签名。

```
github-profile/
├── README.md          ← 最终要上传到 GitHub 的文件（主要改这里）
├── preview.html       ← 本地预览（已生成，双击即可看渲染效果）
├── build_preview.py   ← 预览生成脚本（改完 README.md 后重新运行即可刷新）
└── CUSTOMIZE.md       ← 本文件
```

## 一、怎么让它显示在 GitHub 主页上

1. 在 GitHub 新建一个仓库，**仓库名必须与你的用户名完全一致**：`Leo1958923515`
   （大小写要一致，且勾选 Public）。
2. 把本目录的 `README.md` 上传/推送到该仓库根目录。
3. 打开 <https://github.com/Leo1958923515>，README 会自动出现在主页顶部。

命令行方式：

```bash
cd github-profile
git init
git add README.md
git commit -m "docs: add profile README"
git branch -M main
git remote add origin https://github.com/Leo1958923515/Leo1958923515.git
git push -u origin main
```

> 提示：`preview.html` / `build_preview.py` / `CUSTOMIZE.md` 只是本地辅助文件，
> **不要**一起推送到 profile 仓库里，否则会显得杂乱。

## 二、本地预览

- 直接双击 `preview.html` 即可查看 GitHub 同款排版效果；
- 顶部三个按钮：**高亮占位符**（把所有 `✏️` 位置标黄，方便定位）、**深色模式**、**复制 Markdown**；
- 修改 `README.md` 后运行 `python build_preview.py` 重新生成预览。

## 三、必改项（搜索 `✏️` 逐个替换，共 14 处）

> 内容已按你的情况写成**机器人工程语境**（GMU · 机器人工程），下面是逐项说明。

| # | 位置 | 现在的占位内容 | 改成 |
|---|---|---|---|
| 1 | 头部 Typing SVG 的 `lines=` | `Hi 👋, I'm Leo` / `Robotics Engineering Undergraduate` | 想滚动显示的语句（用 `;` 分隔；空格写 `+`、逗号 `%2C`、`&` 写 `%26`、`+` 写 `%2B`，如 `Learning+OpenCV+%26+Deep+Learning`） |
| 2 | 头部胶囊（`Bilibili` / `Zhihu` / `RoboMaster`） | 已填 B 站、知乎主页，以及 RoboMaster 官网 <https://www.robomaster.com/zh-CN>（配色 `0087EE` 取自该站主色） | ✅ 已填，无需改。B 站胶囊用的是**官方粉 `FB7299`**（原为官方蓝 `00A1D6`） |
| 3 | 头部 `Open_Source` 胶囊 | 已指向你的仓库列表 | ✅ 已填，无需改 |
| 4 | 头部 `Email` 胶囊 | 已删除（原先和 Bilibili / Zhihu / Open_Source 并排，与页尾邮箱重复） | 邮箱只保留在「🤝 Connect with Me」区；想加回头部胶囊，照上面任意一个 `<a>` 块的格式补即可 |
| 5 | About Me 第 1 段 | `Robotics Engineering` at `GMU` | 学校名/专业如有出入就改这里 |
| 6 | About Me 第 2 段 | 兴趣表述（把脑子里的想法变成能跑能动的实物，探索机械、电控与代码的交界；用户自撰，中英已同步） | ✅ 已填，无需改 |
| 7 | About Me 第 3 段 | 正在学什么（C/C++、Python、OpenCV、深度学习） | 换成你真实在学的内容 |
| 8 | About Me 第 4 段 | 边做边学（写完 → 跑崩 → 修好 → 记下来）+「每天进步一点点、留下可验证的作品集」（用户自撰，中英已同步） | ✅ 已填，无需改 |
| 9 | 中文折叠块 4 段 | 上面 4 段的中文版 | 与英文对应，越具体越好 |
| 10 | Basic Information 整栏 | **已删除**（2026-09-16）。原 5 条里「📺 在 B 站与知乎分享」与「🎯 今年目标」已并入 Current Work，其余三条（学校 / 方向 / 在学语言）与 About Me 完全重复 | 想加回：在 About Me 的 `---` 之后补一节 `### 📋 Basic Information`（英文条目 + `<details>` 中文折叠） |
| 11 | Current Work 4 条 | 学习清单（C/C++、OpenCV、深度学习）/ 在做的项目 / B站与知乎分享 / 年度目标（RoboMaster 实验室） | 你正在做的事；后两条原属 Basic Information，已并入 |
| 12 | Selected Projects 4 条 | 4 个 `Project Name` 示例条目 | 真实项目名 + 链接 + 一句话亮点 + 技术标签 |
| 13 | Technical Stack 徽章 | 3 组共 13 枚：语言基础（C/C++/Python）、工具环境（Git/GitHub/VS Code/Linux/Markdown）、机器人 AI（ROS 2/STM32/NumPy/PyTorch/OpenCV） | 全部启用；删徽章直接删整行，加徽章见第四节 |
| 14 | 反引号关键词行 | 已删除（原为 `Data Structures & Algorithms` · `Object-Oriented Programming` · `Mechanics Fundamentals` · `Circuit Basics` · `CAD Modeling Basics`） | 想加回来：在「💻 Languages & Fundamentals」那组徽章下方空一行补一条，词用 ` · ` 分隔 |
| 15 | GitHub Stats 区 | 已整栏删除（原为 Stats + Top Languages + Streak + 奖杯 + 活跃度图 5 张卡片） | 想加回来见下方第五节，那里保留了全部 URL 与主题说明 |
| 16 | Connect 区 | 邮箱 / GitHub / B站（`Bilibili-LeoLGC`，官方粉 `FB7299`）/ 知乎（`Zhihu-LeoLGC`，`0066FF`） | ✅ 已填；想加平台按注释里模板复制一行。徽章格式 `平台名-显示名-背景色`，改显示名只动中间那段。**原 Connect 区下方的 `Stars` / `Followers` 卡片已于 2026-09-16 删除**，加回方法见第四节 |
| 17 | 底部签名 | `𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒 𝑅𝑒𝑤𝑎𝑟𝑑𝑠 𝑒𝑞𝑢𝑎𝑙𝑠 𝑅𝑒𝑡𝑢𝑟𝑛.` + 句末 🪜（用的是 Unicode 数学斜体字符，不是 `<i>`） | ✅ 已填，无需改；原理与改法见下方「签名为什么长这样」 |
| 18 | 页脚致谢 | 签名下方灰色小字**一行**（中文「致谢」，Lain-Ego0 与 LocoWiki 均带链接）。原英文 `Thanks` 行已于 2026-09-16 删除 —— 与中文说的是同一件事，且两行加起来视觉分量比 About Me 还重 | ✅ 已填，无需改；不想保留致谢就删掉整个 `<p>` 块。想再加一行就补 `<sub>…</sub>` + `<br />` |

## 四、常用替换片段

**签名为什么长这样**（底部那句是**衬线斜体**，但不是靠 `<i>` 实现的）

GitHub 会把 markdown 里的 `style` 属性剥掉，所以没法指定 `font-family: Georgia/Times`。要让它是「真正的衬线斜体」，
只能直接用 **Unicode 数学斜体字符**（Mathematical Italic，U+1D434–U+1D467）——这些字符自带斜体衬线字形，任何平台都不依赖 CSS：

```
ASCII :  Cumulative Rewards equals Return.
斜体版:  𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒 𝑅𝑒𝑤𝑎𝑟𝑑𝑠 𝑒𝑞𝑢𝑎𝑙𝑠 𝑅𝑒𝑡𝑢𝑟𝑛.
```

要改内容：**别手打**，在搜索引擎搜「mathematical italic text generator」，把句子粘进去转换，再贴回来。
注意小写 `h` 在 Unicode 里映射到 `ℎ`（U+210E，PLANCK CONSTANT），不是 U+1D455 —— 工具会自动处理，手改容易踩坑。

> 代价（用之前要知道）：
> - 屏幕阅读器会逐字拼读这些字符，念不顺；
> - 搜索引擎和不支持该 Unicode 块的字体可能显示成方框；
> - 复制出来是斜体码位，不是普通字母。
>
> 想换回普通文字：把 `𝐶𝑢𝑚𝑙𝑎𝑡𝑖𝑣𝑒…` 那段整体替换成 `Cumulative Rewards equals Return.`，外面套 `<i>…</i>` 即可。

**换一个图标**（句末用的是 🪜 梯子 emoji —— Unicode 里没有「楼梯」，只有梯子；想换成真正的楼梯图标见下）

```markdown
<img src="https://api.iconify.design/tabler/stairs.svg?color=2F81F7" height="18" alt="stairs" />
```

- 图标名去 <https://icon-sets.iconify.design/tabler/> 搜（如 `stairs`、`stairs-up`、`stairs-down`）。
- `color=` 后面填十六进制色值，**不要带 `#`**（带 `#` 会被 CDN 拦成 403）。
- 图标没加载出来只会显示 alt 文字，不影响整行排版。

**加一个技能徽章**（[shields.io](https://shields.io) 格式：`名称-背景色?style=flat-square&logo=图标名&logoColor=白/黑`）

```markdown
[![Java](https://img.shields.io/badge/Java-007396?style=flat-square&logo=openjdk&logoColor=white)](https://www.java.com/)
```

图标名去 <https://simpleicons.org> 查，找不到就把 `&logo=...` 整段去掉，只留纯色徽章。

> **⚠️ VS Code 图标已不可用**：图标库（simple-icons）里微软系图标已被移除，`&logo=visualstudiocode` 现在是**无效值** ——
> shields.io 不会报错，只是静默地渲染成一个**没有图标的纯色胶囊**，很难发现。当前用的是 `&logo=vscodium`
> （VSCodium 是 VS Code 的去品牌构建版，图标同源，视觉上几乎一样）。想要"纯文字胶囊"就把 `&logo=vscodium&logoColor=white`
> 整段删掉。其他已实测有效的：`git` `github` `linux` `markdown` `ros` `stmicroelectronics` `numpy` `pytorch` `opencv` `c` `c%2B%2B` `python` `dji`。
>
> **⚠️ `robomaster` 这个图标名不存在**：图标库里没有 RoboMaster 条目。头部那枚 RoboMaster 胶囊用的是 `&logo=dji`
> （RoboMaster 是 DJI 的官方赛事，用母公司标识代替；`dji` 图标本身可用，实测带图标）。想换成纯文字胶囊就把
> `&logo=dji&logoColor=white` 删掉。
>
> **怎么自己验一个图标名是否生效**：浏览器打开 `https://img.shields.io/badge/X-000?logo=你的图标名`，
> 看它有没有图标；或者量返回的 SVG 体积 —— **有图标 1000~8000 字节且含 `<image>`，没有图标恒为 459~473 字节**
> （和随便编一个假名字返回的一样大）。这一步很重要，因为 shields.io 对错误图标名**从不报错**。

**平台官方配色**（想换某枚徽章的颜色，用对应平台的品牌色最不容易出错）

| 平台 | 官方色 | 备注 |
|---|---|---|
| Bilibili | `FB7299` 粉 / `00A1D6` 蓝 | 现用**粉**（B 站标志性品牌色）；蓝色是它的第二品牌色 |
| 知乎 | `0066FF` | 现用值 |
| RoboMaster | `0087EE` | 现用值，取自 robomaster.com 主色 |
| GitHub | `181717` | 现用值 |

> 徽章底色建议配 `&logoColor=white`。注意别把**浅色图标**放在**同明度的底色**上 —— 两种官方色直接对调（例如粉色图标 + 蓝色底）对比度只有约 1.1:1，图标会几乎看不见。

**备用徽章**（这几枚之前存在、按你的清单移除了，想加回来直接抄一行）

```markdown
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=flat-square&logo=vscodium&logoColor=white)](https://code.visualstudio.com/)
[![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat-square&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](https://developer.mozilla.org/docs/Web/JavaScript)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![Fusion 360](https://img.shields.io/badge/Fusion_360-F57C00?style=flat-square&logo=autodesk&logoColor=white)](https://www.autodesk.com/products/fusion-360/)
[![SolidWorks](https://img.shields.io/badge/SolidWorks-005386?style=flat-square&logo=dassaultsystemes&logoColor=white)](https://www.solidworks.com/)
```

**加一个联系方式**（复制到 Connect 区的 `<p>` 内）

```markdown
&nbsp;<a href="https://你的主页"><img src="https://img.shields.io/badge/Portfolio-Personal_Homepage-blue?style=flat&logo=google-chrome&logoColor=white" height="25" alt="Portfolio" /></a>
```

**Stars / Followers 卡片**（2026-09-16 已从 README 删除，想加回来放这儿 —— 紧跟 Connect 区那个 `</p>` 之后）

```markdown
<p align="center">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/Leo1958923515?style=social&logo=github" />
  <img alt="GitHub followers" src="https://img.shields.io/github/followers/Leo1958923515?style=social&logo=github" />
</p>
```

> 删掉的原因：新账号上这两枚徽章会如实显示 `Stars: 0` / `Followers: 0`，对路人来说是负资产。**等仓库有 star / 有 follower 之后再加回来。**

**加一个项目条目**（保持与其他条目同样的四段式结构）

```markdown
- **[项目名](仓库链接)** — 它解决什么问题、有什么亮点。 `技术标签` `技术标签`
```

## 五、数据卡片（已从 README 删除，需要时可参考本节加回）

> 2026-09-16：用户要求整栏删除 `### 📊 GitHub Stats`，README 里已无任何数据卡片。
> 本节内容保留作备用 —— 想加回来时，把下面的 URL 拼进 `<div align="center">…</div>` 即可。

原本用了 4 个公开服务共 5 张卡片（主题统一 `tokyonight`，深蓝，与头部 `#2F81F7` 呼应）：

```html
<!-- 并排两张：个人统计 + 最常用语言 -->
<img height="180em" src="https://github-readme-stats.vercel.app/api?username=Leo1958923515&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Leo1958923515&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top Languages" />

<!-- 连续贡献 -->
<img src="https://streak-stats.demolab.com?user=Leo1958923515&theme=tokyonight&hide_border=true" alt="Streak" />

<!-- 奖杯 -->
<img src="https://github-profile-trophy.vercel.app/?username=Leo1958923515&theme=tokyonight&no-frame=true&no-bg=true&column=7&margin-w=8" alt="Trophies" />

<!-- 活跃度热力图 -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=Leo1958923515&theme=tokyo-night&hide_border=true&area=true" alt="Activity Graph" width="100%" />
```

想换风格，把 URL 里的 `theme=tokyonight` 整体替换即可，常用值：

| 取值 | 观感 |
|---|---|
| `tokyonight` | 深蓝（原用值） |
| `github_dark` | GitHub 官方深色 |
| `radical` | 高饱和粉紫 |
| `default` | 浅色简洁（README 想走纯白风格时用它） |

- 首次访问数据卡片可能显示为空，等 CDN 缓存几秒后刷新即可（这是服务端渲染的图片）。
- `count_private=true` 只统计公开数据；要统计私有仓库提交需部署自己的
  github-readme-stats 实例并配 token，个人使用可忽略。
- 注：活跃度图服务的主题名与其他几个不同 —— 它用 `tokyo-night`（带连字符），不是 `tokyonight`。

## 六、常见问题

- **排版没生效 / 徽章不显示**：GitHub 会缓存图片，等几分钟或强刷（Ctrl+F5）；也可能是
  shields.io 临时波动，稍后再试。
- **`<details>` 折叠块不展开**：GitHub 只支持 `<details>` + `<summary>` 这一种写法，不要改成别的标签。
- **想加仓库置顶卡片**：用 `https://github-readme-stats.vercel.app/api/pin/?username=Leo1958923515&repo=仓库名&theme=tokyonight`。
- **想加访问量统计**：在底部插入
  `![Visitors](https://komarev.com/ghpvc/?username=Leo1958923515&color=2F81F7&style=flat&label=Visitors)`。
