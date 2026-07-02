# ReShade-Chinese-Guide

ReShade 中文指南 — 基于 [FRAMED. Screenshot Community](https://framedsc.com/) 的 Reshade Guides 整理，计划逐步汉化。

## 内容来源

原文来自 [framedsc.com/ReshadeGuides](https://framedsc.com/ReshadeGuides/index.htm)，版权归原作者所有。

## 在线浏览（GitHub Pages）

推送至 `main` 后会自动部署。首次需手动开启（仅需一次）：

1. 打开仓库 [Settings → Pages](https://github.com/Afra55/ReShade-Chinese-Guide/settings/pages)
2. **Build and deployment → Source** 选择 **GitHub Actions**
3. 到 [Actions](https://github.com/Afra55/ReShade-Chinese-Guide/actions/workflows/pages.yml) 页面，点击 **Run workflow** 重新部署

部署完成后访问：

| 页面 | 地址 |
|------|------|
| 首页（自动跳转） | https://afra55.github.io/ReShade-Chinese-Guide/ |
| 指南入口 | https://afra55.github.io/ReShade-Chinese-Guide/ReshadeGuides/index.htm |

之后每次推送到 `main` 都会自动更新网站。

## 本地浏览

在仓库根目录启动一个本地 HTTP 服务器后，打开 Reshade 指南首页：

```bash
python3 -m http.server 8080
```

浏览器访问：http://localhost:8080/ReshadeGuides/index.htm

## 目录结构

```
ReshadeGuides/                    # 主指南目录
├── index.htm                       # 指南首页
├── setupreshade.htm                # 安装配置
├── shaderscatalogue.htm            # 着色器目录
├── lutgenguide.htm                 # LUT 生成
├── reshadeuwp.htm                  # UWP 游戏注入
├── depthguide.htm                  # 深度缓冲导出
├── RealLongExposure.htm            # RLE 长曝光
├── Shaders/                        # 着色器专题
│   ├── cinematicdof.htm
│   └── heightfog.htm
└── Addons/                         # 插件专题
    ├── shader_toggler_repository.htm
    └── MSADOF.htm

ReshadeGuidesShaderguides.htm       # 着色器指南索引
ReshadeGuidesAddonguides.htm        # 插件指南索引

Images/                             # 图片资源
css/                                # 站点样式
js/                                 # 站点脚本
fontawesome/                        # 图标字体
ShaderTogglers/                     # ShaderToggler 配置文件
scripts/mirror_assets.py            # 资源镜像脚本
```

## 更新镜像

如需从源站重新拉取资源：

```bash
python3 scripts/mirror_assets.py
```

## 汉化计划

- [ ] 翻译各指南正文
- [ ] 保留原有 HTML 结构与图片路径
- [ ] 在页面中标注原文链接
