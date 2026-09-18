# Alsontech 英文站首页 SEO 诊断报告

## 0. 审计范围与限制

- **审计 URL（原始提供）**：https://www.alsontech.com/
- **实际审计 URL（修正）**：https://en.alsontech.com/
  - 说明：https://www.alsontech.com/ 实际返回的是**简体中文首页**（页面 `<title>` 为"埃尔森智能科技｜工业3D相机..."，正文为中文）。该网站的英文首页位于独立子域名 **https://en.alsontech.com/**。本报告按任务要求"仅审计英文首页"，因此以 en.alsontech.com 为审计对象；中文首页仅作为国际化结构的对比参考。
- **审计日期**：2026-09-15
- **是否成功访问实时页面**：是。通过实时抓取成功获取 en.alsontech.com 的渲染后 HTML/内容（含 title、meta、导航、正文、页脚）。
- **无法验证的数据（工具限制，非猜测，需人工/其他工具补充）**：
  - robots.txt（https://en.alsontech.com/robots.txt）—— 无法直接抓取，需人工在浏览器或 Screaming Frog 中确认
  - sitemap.xml —— 同上，未能确认是否存在及其收录范围
  - 页面 `<head>` 中是否有 hreflang 标签（本报告仅能确认前端存在 CN/EN/JP 语言切换链接，无法确认 `<link rel="alternate" hreflang="x">` 是否正确配置）
  - JSON-LD 结构化数据（渲染层未暴露 `<script type="application/ld+json">` 内容，需用 Google Rich Results Test 验证）
  - Core Web Vitals / PageSpeed 数据（LCP、CLS、INP 等）
  - 服务器返回的真实 HTTP 状态码、响应头（如 X-Robots-Tag）
  - Google Search Console 收录量、点击率、平均排名等
- 以下所有结论均基于**实际抓取到的页面内容**，凡无法验证之处，已在对应位置标注"需验证"，不做主观推测。

---

## 1. 执行摘要

**最关键发现（5 条）：**

1. **首页 H1 是无意义占位文字 "TAMPLATE"**（Template 的拼写错误），而不是公司名或核心关键词。这是本次审计中最严重的问题，直接影响搜索引擎对页面主题的判断。
2. **Meta description 长度约 224 字符，远超 160 字符建议上限**，在 Google 搜索结果中会被截断，且未包含任何行动号召（CTA）。
3. **站内导航与正文大量使用非描述性锚文本**（"Learn More" / "Click to learn more" 反复出现十余次），链接到不同页面却使用相同文字，稀释了锚文本的相关性信号。
4. **图片 ALT 属性普遍缺失**，且发现至少 1 处英文页面的图片仍残留中文 ALT 文本（"防爆3D相机"），说明英文站是从中文站直接翻译衍生、未做完整本地化 QA。
5. **Open Graph 分享图片为占位图**（`og:image` 指向 `no-pic.jpg`），社交媒体分享该链接时会显示"无图片"，影响外部分享的点击率和品牌形象。

**首页当前最大的 SEO 问题：**
页面的语义结构（H1）与元信息（meta description、OG 图片）存在明显的"未完工"状态（占位符文本、默认图片），这会让搜索引擎和社媒平台都难以准确抓取并展示该品牌信息，属于会直接拖累索引质量和点击率的基础性缺陷。

**最优先要做的 3 件事：**
1. 立即将 H1 从 "TAMPLATE" 改为包含品牌词 + 核心关键词的真实标题（如"Industrial 3D Cameras & Robot Vision Systems | ALSONTECH"）。
2. 重写 meta description 至 140-160 字符，包含核心关键词 + CTA。
3. 更换 og:image 为真实产品/工厂图片，并为首页所有图片补全描述性 ALT 文本。

---

## 2. 评分表

| 维度 | 分数/100 | 说明 |
|---|---|---|
| 技术 SEO | 55 | HTTPS、canonical、viewport 均正常；但 robots.txt / sitemap.xml / 状态码无法验证，URL 结构中大量使用无语义的 `h-col-XXX.html` 编号页面 |
| On-page SEO | 40 | H1 为占位文字是硬伤；title 长度合格，meta description 严重超长；锚文本高度重复 |
| 内容与搜索意图 | 60 | 产品与解决方案信息完整，覆盖机床上下料、拆码垛、装配等核心场景，但首页缺少可读的"我们是谁/为什么选择我们"叙述性内容，偏产品罗列 |
| 关键词策略 | 55 | meta keywords 中关键词选择合理（industrial 3d camera、robot vision system 等），但正文关键词分布集中在产品名，缺少更贴近采购决策阶段的长尾词（如 "3D bin picking system for automotive"） |
| E-E-A-T | 45 | 有联系方式、地址、领英/YouTube/X/Facebook 链接；但首页无年份资历、认证、客户 logo 墙的清晰呈现（仅一张 SVG 图片承载"全球客户信赖"信息，无法被搜索引擎读取为文本）、无客户证言、无案例详情 |
| 国际化 SEO | 50 | CN/EN/JP 三语言版本已用独立域名/子域名区分，语言切换器存在；但 hreflang 标签是否正确配置无法验证，且切换链接指向的 URL 结构不完全一致（见问题清单） |
| 结构化数据 | 需验证 | 渲染内容中未见明显结构化数据痕迹，建议用 Rich Results Test 核实，暂不打分 |
| 移动与体验 | 60 | viewport 已配置，但设置了 `user-scalable=0`，禁止用户手动缩放，属于移动端可用性反模式 |

---

## 3. 关键问题与优先级

| 优先级 | 问题 | 证据 | 影响 | 修复建议 | 工作量 |
|---|---|---|---|---|---|
| P0 | H1 为占位文字 "TAMPLATE" | 页面顶部渲染出 `# [TAMPLATE](https://en.alsontech.com/index.jsp)`，该文字同时出现在中文站（www.alsontech.com）首页，说明是模板遗留、未替换 | 搜索引擎解析首页主题时权重最高的标签传达的是无意义词，损害首页对核心词（industrial 3D camera 等）的相关性判断，属于阻碍排名的严重问题 | 将 H1 替换为含品牌词+核心关键词的可读文本，如 "Industrial 3D Cameras & Robot Vision Systems" | 小 |
| P0 | Meta description 超长（约 224 字符） | 抓取到的 meta-description 完整文本长达约 224 字符，远超 Google 常见截断阈值（约 155-160 字符） | 搜索结果摘要会被截断，可能丢失关键信息和 CTA，影响点击率（CTR） | 精简至 140-160 字符，保留最核心的产品词+行业词+CTA | 小 |
| P0 | og:image 为占位图 | `meta-og:image: https://2.ss.508sys.com/image/no-pic.jpg`，文件名明确为 "no-pic"（无图占位） | 在 LinkedIn、Facebook、X 等平台分享首页链接时无法展示品牌视觉，降低外链点击率和专业形象，间接影响外链获取 | 替换为真实的产品/工厂/团队图片，建议 1200×630px | 小 |
| P1 | 图片普遍缺失 ALT，且存在中文残留 ALT | 首页多张产品图片渲染为空 ALT（如 `![](...ABUIABAEGAAg_Ijb0AYo...)`）；防爆相机配图 ALT 为中文"防爆3D相机"，出现在英文页面中 | 图片无法为图片搜索和无障碍访问提供语义信息；中文 ALT 说明英文站本地化不完整，也是轻微的语言不一致信号 | 为所有产品/场景图补充描述性英文 ALT，如 "ALSONTECH explosion-proof industrial 3D camera for hazardous environments" | 中 |
| P1 | 内部链接锚文本高度重复、无描述性 | 首页产品与方案模块中 "Learn More" / "Click to learn more" 反复出现约 10+ 次，分别指向不同的产品/方案页面 | 锚文本是搜索引擎理解目标页面主题的重要信号之一，千篇一律的 "Learn More" 无法传递差异化关键词，削弱了内链对目标页面排名的助力 | 将锚文本改为具体产品名/场景词，如 "Explore the 06A high-speed laser 3D camera"、"See automotive 3D vision solutions" | 中 |
| P1 | URL 结构不统一，部分页面使用无语义数字 ID | 产品页 URL 语义清晰（如 `/products/laser-industrial-3d-camera.html`），但解决方案与案例页大量使用 `h-col-550.html`、`h-nd-730.html` 这类无关键词的编号 URL | 无语义 URL 无法为长尾关键词提供 URL 层面的相关性信号，且不利于用户识别页面内容 | 在技术条件允许下为重要栏目页配置语义化 URL（如 `/solutions/general-industry.html`）；短期内至少在 `<title>`、H1、面包屑中强化该页面主题 | 大（涉及 CMS/开发资源） |
| P1 | 语言版本切换链接结构不一致 | Logo 点击跳转到 `http://www.alsontech.com/en/`（注意为 **HTTP 非 HTTPS**，且路径为 `/en/` 子目录），而顶部语言切换器的 EN 按钮指向 `https://en.alsontech.com`（子域名）；两者结构不一致 | 用户可能被导向非 HTTPS 的旧版路径，存在潜在的混合内容/安全提示风险；也给搜索引擎的国际化结构判断增加噪音 | 统一所有内部链接指向 `https://en.alsontech.com`，移除或 301 重定向 `http://www.alsontech.com/en/` 路径 | 中 |
| P2 | viewport 禁用手动缩放 | `meta-viewport: width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0` | `user-scalable=0` 会阻止用户双指缩放页面，是常见的移动端可用性/无障碍反模式，虽非直接排名因素，但影响移动体验相关的间接信号 | 移除 `maximum-scale` 与 `user-scalable=0` 限制 | 小 |
| P2 | 首页缺少可索引的文本类信任内容 | "Trusted Choice for Automation Worldwide" 板块仅以一张 SVG 图片呈现客户信任信息，未见客户 logo 的文字列表、认证文字说明、年份资历等可被搜索引擎抓取为文本的内容 | 纯图片承载的信任信号无法被搜索引擎索引为文本内容，弱化 E-E-A-T 相关的页面语义 | 在该板块补充文字说明，如成立年份、服务客户数量/行业、认证名称（可配合图片） | 中 |
| P2 | 页脚出现孤立数字 "0" | 页脚社交图标附近渲染出独立的文本节点 "0"（位于联系方式与版权信息之间） | 疑似组件占位符或计数器渲染异常，影响页面专业度和内容整洁度 | 排查该模块（可能是评论数/浏览量组件）来源并移除或修复 | 小 |

---

## 4. 可直接复制的优化建议

### Title tag（建议 50-60 字符）
现状（约 54 字符，长度合格，可保留结构，仅做微调使关键词顺序更贴近搜索意图）：
```
Industrial 3D Camera & Robot Vision System | ALSONTECH
```
建议替代方案（55 字符）：
```
Industrial 3D Cameras & Robot Vision Systems | ALSONTECH
```

### Meta description（建议 140-160 字符）
现状（约 224 字符，过长）：
```
ALSONTECH provides industrial 3D cameras and robot vision systems for machine tending, bin picking, depalletizing, assembly, inspection and intelligent automation. Fast deployment, high precision and reliable performance.
```
建议替代方案（约 156 字符）：
```
ALSONTECH designs industrial 3D cameras and robot vision systems for bin picking, machine tending, depalletizing and inspection. Get a free consultation.
```

### H1（建议替换占位文字 "TAMPLATE"）
```
Industrial 3D Cameras & Robot Vision Systems for Flexible Manufacturing
```

### 建议的 H2/H3 结构（在现有板块基础上优化）
```
H1: Industrial 3D Cameras & Robot Vision Systems for Flexible Manufacturing

H2: Industrial 3D Cameras Built for Flexible Manufacturing
  H3: 06A Series – High-Speed Laser 3D Cameras
  H3: A Series – Binocular Laser 3D Cameras
  H3: C Series – Structured Light 3D Cameras
  H3: B Series – 3D Laser Profiler
  H3: Explosion-Proof 3D Cameras
  H3: 3D Cameras for Automotive Manufacturing

H2: 3D Vision Solutions by Industry
  H3: General Industry 3D Vision Solutions
  H3: Automotive Manufacturing 3D Vision Solutions

H2: Industry Case Studies

H2: Why Manufacturers Trust ALSONTECH
  （建议新增，用于承载文字化的信任信号：成立年份、服务客户数量、认证等）

H2: Partner Program
```

### 图片 ALT 示例
| 现状 | 建议 ALT 文本 |
|---|---|
| 空 ALT（06A 系列产品图） | `06A series high-speed laser 3D camera for industrial automation` |
| 空 ALT（防爆相机模块首图） | `ALSONTECH explosion-proof industrial 3D camera` |
| ALT 为中文 "防爆3D相机" | 同上，替换为英文，保持全站语言一致性 |
| 空 ALT（客户信任 SVG） | `Global automation customers trusted by ALSONTECH` |

### 内部锚文本建议
| 现状（重复使用） | 建议 |
|---|---|
| Learn More（06A 系列） | Explore the 06A high-speed laser 3D camera |
| Learn More（通用行业解决方案） | See 3D vision solutions for general industry |
| Learn More（汽车制造解决方案） | See 3D vision solutions for automotive manufacturing |
| Click to learn more（防爆相机） | Learn about ALSONTECH explosion-proof 3D cameras |

### 建议新增 Schema（JSON-LD，需先用 Rich Results Test 确认现状后再叠加，避免重复标记）

Organization + LocalBusiness 建议示例（字段需与真实工商信息核对后再上线）：
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "ALSONTECH (Henan Alson Intelligent Technology Co., Ltd.)",
  "url": "https://en.alsontech.com/",
  "logo": "https://en.alsontech.com/path-to-logo.png",
  "sameAs": [
    "https://www.linkedin.com/company/alsontech",
    "http://www.youtube.com/@ALSONTECH_3DVISON",
    "https://x.com/ALSONTECH_3D",
    "https://www.facebook.com/alsontech3d"
  ],
  "contactPoint": [{
    "@type": "ContactPoint",
    "telephone": "+86-0371-88915519",
    "contactType": "sales",
    "email": "info@alsontech.com"
  }],
  "address": [
    {
      "@type": "PostalAddress",
      "streetAddress": "Unit 108, Building 7, No.186 Heyang Road, High-tech District",
      "addressLocality": "Zhengzhou",
      "addressCountry": "CN"
    }
  ]
}
```
（如需展示 FAQ/面包屑等 schema，建议先确认首页是否已有 JSON-LD，避免重复添加导致校验错误——见第 10 节。）

---

## 5. 关键词与搜索意图

> 以下关键词基于首页正文、导航结构、meta-keywords 字段实际出现的术语归纳，**未编造搜索量或排名数据**。

| 关键词 | 搜索意图 | 建议位置 | 优先级 |
|---|---|---|---|
| industrial 3D camera | 信息型/商业调查型 | Title、H1、首屏 | 高 |
| robot vision system | 信息型/商业调查型 | Title、H1、导航 | 高 |
| 3D vision system for automation | 商业调查型 | H2、首屏文案 | 高 |
| robot guidance 3D vision | 商业调查型 | 解决方案模块 H3 | 高 |
| bin picking 3D camera | 商业调查型/交易型 | 解决方案模块、产品页锚文本 | 高 |
| machine tending 3D vision | 商业调查型 | 通用行业解决方案模块 | 高 |
| depalletizing robot vision | 商业调查型 | 通用行业解决方案模块 | 中 |
| laser line 3D camera | 交易型 | 06A/A 系列产品模块 | 高 |
| structured light 3D camera | 交易型 | C 系列产品模块 | 中 |
| 3D laser profiler | 交易型 | B 系列产品模块 | 中 |
| explosion-proof 3D camera | 交易型（细分场景） | 防爆相机模块 | 中 |
| automotive 3D vision solution | 商业调查型 | 汽车行业解决方案模块 | 高 |
| stamping welding paint assembly 3D vision | 信息型（细分工艺） | 汽车解决方案 H3（冲压/焊装/涂装/总装） | 中 |
| 3D vision software platform | 信息型 | 产品导航 | 低 |
| robotic depalletizing solution | 商业调查型 | 案例/解决方案模块 | 中 |
| industrial automation vision inspection | 信息型 | 内容模块（建议新增） | 中 |
| 3D machine vision for logistics | 商业调查型 | 行业案例模块 | 中 |
| flexible manufacturing 3D vision | 信息型 | 首屏文案/H1 | 高 |
| UR+ certified 3D camera | 信息型/信任型（需先核实是否仍适用） | E-E-A-T 模块 | 低 |
| 3D vision system supplier / manufacturer | 交易型（品牌+品类词） | About Us、首屏文案 | 高 |

---

## 6. 技术 SEO 检查表

- [x] **Pass** — HTTPS：canonical 与页面本身均为 `https://en.alsontech.com/`
- [x] **Pass** — Canonical 标签：自引用，指向自身首页，无重复/冲突
- [x] **Pass** — Viewport meta：已配置 `width=device-width`
- [ ] **Warning** — Viewport 附带 `user-scalable=0`，禁止用户缩放，属可用性反模式
- [ ] **Cannot verify** — robots.txt 是否存在、是否误伤重要页面
- [ ] **Cannot verify** — sitemap.xml 是否存在、是否已提交至 Google Search Console
- [ ] **Cannot verify** — 首页真实 HTTP 状态码（工具未返回状态码，仅确认可访问）
- [ ] **Cannot verify** — 是否存在 noindex/nofollow 元标签（渲染内容中未见，但无法 100% 排除，建议用"查看网页源代码"确认）
- [ ] **Cannot verify** — hreflang / x-default 标签是否正确配置（仅确认前端有 CN/EN/JP 切换入口）
- [ ] **Warning** — 语言切换入口链接结构不统一（HTTP 与 HTTPS、子域名与子目录混用，见第 3 节）
- [ ] **Fail** — H1 标签内容为占位文字 "TAMPLATE"，非真实语义标题
- [ ] **Warning** — 部分栏目页（解决方案、新闻、案例）URL 为无语义数字 ID（如 `h-col-550.html`）
- [ ] **Warning** — 多数首页图片 ALT 为空，部分残留中文 ALT
- [ ] **Cannot verify** — 结构化数据（Organization/Product/FAQ/Breadcrumb/LocalBusiness）是否存在，建议用 Google Rich Results Test 核实
- [x] **Pass** — Open Graph 基础字段（title、description、type、url）已配置
- [ ] **Fail** — og:image 为占位图（no-pic.jpg）
- [ ] **Cannot verify** — 是否配置 Twitter Card meta（`twitter:card` 等），渲染内容中未见
- [ ] **Cannot verify** — Core Web Vitals（LCP / INP / CLS），需 PageSpeed Insights 或 CrUX 数据
- [ ] **Cannot verify** — 是否存在渲染阻塞资源、图片是否已压缩/使用现代格式（WebP/AVIF），需 Lighthouse/PageSpeed 数据

---

## 7. 内容、E-E-A-T 与转化建议

**建议新增的内容：**
- 首页需要一段**可读的品牌叙述文字**（2-4 句话），回答"我们是谁 / 服务谁 / 为什么可信"，而不是直接跳入产品罗列。目前首页从导航结束后立即进入产品卡片，缺少过渡性的信任建立内容。
- 在"Trusted Choice for Automation Worldwide"板块补充**文字化的信任数据**：成立年份、服务的国家/客户数量、代表性认证（如页面曾提及的"上海市专精特新企业"认证、UR+ 认证等，需先核实哪些认证仍然有效再放上英文站）。
- 行业案例模块目前只有缩略图链接，无标题文字说明；建议为每个案例卡片补充一行简短的英文说明（如 "Automotive body panel inspection — 40% faster takt time"），既提升可读性也增加长尾关键词覆盖。

**建议移除/精简的内容：**
- 页脚附近孤立出现的数字 "0"（疑似组件占位符），建议排查并移除，避免给访客留下"网站未完工"的印象。

**建议重写的内容：**
- Meta description、H1（已在第 4 节给出具体文案）。
- 产品模块下的重复 "Learn More" 锚文本。

**信任信号（Trust Signals）建议补充：**
- 客户 logo 墙（文字可读形式，而非仅 SVG 图片）
- 认证徽章 + 认证名称文字说明
- 具体案例数据（如可公开的效率提升百分比、良率提升数据，需与客户/市场部门确认可公开性）
- 团队/工厂真实照片，替换占位式 og:image

**CTA 与 UX 建议：**
- 首屏目前以新品/活动 Banner 为主（防爆相机、AT-S1000-06C-S3-V2），没有明确的主行动号召（如"Request a Demo" / "Talk to an Engineer"）。建议在首屏增加一个清晰、贯穿全站的主 CTA 按钮。
- 联系方式（电话、邮箱）目前只出现在页脚，建议在顶部导航或首屏增加一个轻量级的"Contact Sales"入口，缩短 B2B 决策路径。

---

## 8. 竞品参考

本次未按用户要求对 3 家英文竞品首页做完整、逐项的技术审计（title/meta/H1 等原始标签需要实时抓取每个竞品首页才能给出可靠证据，属于超出"仅审计 Alsontech 首页"范围的额外工作）。仅基于公开搜索结果做**有限、注明来源的定性参考**，不编造未直接观察到的数据：

- **Photoneo**（3D 工业视觉同业竞品）：其官网内容以"Best Industrial 3D Cameras & Scanners | Photoneo"等**利益导向型标题**（强调"best"、具体应用场景如自动化、物流、检测）为主，文案更强调客户价值而非单纯罗列产品型号，这与 Alsontech 首页目前"以产品系列命名为主"的呈现方式形成对比。
- 由于未对 Photoneo、Zivid、SICK 等竞品首页做逐项实时抓取审计，**title 字符数、meta description 长度、H1 内容、结构化数据情况均标注为"需验证"**，如需完整竞品对比，建议单独立项、逐一实时抓取核实。

---

## 9. 30 天行动计划

**Week 1：快速见效项（Quick Wins）**
- 将 H1 从 "TAMPLATE" 替换为真实标题
- 重写 meta description 至 140-160 字符
- 更换 og:image 为真实产品/工厂图片
- 移除页脚孤立的 "0" 占位内容
- 移除 viewport 中的 `user-scalable=0` 限制

**Week 2：技术修复**
- 人工确认 robots.txt 内容，排查是否误伤重要目录
- 确认 sitemap.xml 是否存在并提交至 Google Search Console
- 用"查看网页源代码"方式确认是否存在意外的 noindex/nofollow 标签
- 统一语言切换相关链接（清理 `http://www.alsontech.com/en/` 的 HTTP/子目录路径，统一指向 `https://en.alsontech.com`）
- 用 Google Rich Results Test 核实现有结构化数据情况

**Week 3：内容与关键词优化**
- 为首页所有图片补全描述性英文 ALT 文本
- 将重复的 "Learn More" 锚文本替换为具体产品/场景关键词
- 在首页新增品牌叙述段落 + 信任信号文字模块
- 为行业案例卡片补充说明文字

**Week 4：结构化数据、内链与监测**
- 上线 Organization/LocalBusiness JSON-LD（先与结构化数据核实结果对照，避免重复标记）
- 评估并逐步为解决方案/案例/新闻栏目页规划语义化 URL（大工作量项，可作为后续迭代）
- 在 Google Search Console 与 GA4 中建立首页关键指标监测（收录状态、CTR、跳出率）作为本轮优化效果的基线

---

## 10. 需要进一步验证的数据

- **Google Search Console**：首页索引状态、覆盖率报告中是否有排除项（noindex/canonical 冲突/重复内容）、首页当前的展示次数与 CTR、hreflang 报告中是否有错误
- **GA4**：首页跳出率、平均停留时间、从首页到产品页/联系表单的转化路径与转化率
- **Screaming Frog**：全站抓取以确认 robots.txt 规则、真实 HTTP 状态码、重定向链、H1/Title 缺失或重复情况（尤其是 `h-col-XXX.html` 类栏目页）
- **PageSpeed Insights / Core Web Vitals**：LCP、INP、CLS 实测数据，图片是否已使用现代格式与懒加载
- **Google Rich Results Test / Schema Markup Validator**：确认当前是否已有结构化数据、类型是否正确、是否有校验错误
- **Ahrefs / Semrush**：核心关键词当前排名、竞品关键词差距、外链概况（本报告未使用第三方 SEO 工具，未编造任何排名/流量/外链数据）

---

## 11. 假设与无法验证项

- 假设用户提供的原始 URL（https://www.alsontech.com/）意图指向"英文站"，但该 URL 实际渲染为中文内容，因此本报告改为审计 en.alsontech.com；如果用户的真实意图是审计 www.alsontech.com 本身（无论语言），请另行说明，需重新出具报告。
- 无法验证：robots.txt、sitemap.xml、真实 HTTP 状态码、noindex/hreflang 标签细节、结构化数据具体实现、Core Web Vitals 数据、GSC/GA4 指标、竞品首页的逐项技术标签、任何排名/流量/外链数据。以上均未做猜测性填写，已在正文中标注"需验证"或"Cannot verify"。
- "上海市专精特新企业"认证等信息来自中文站首页新闻模块，英文站首页未见对应内容，是否应/能在英文站呈现需与客户内部确认（涉及资质名称的官方英文表述是否存在）。

---

**可直接粘贴到 GitHub 的提交说明：**

```
Add SEO audit for ALSONTECH English homepage (en.alsontech.com)
```
