# ReShade-Chinese-Guide

ReShade 中文指南 — 基于 [FRAMED. Screenshot Community](https://framedsc.com/) 的 Reshade Guides 整理，计划逐步汉化。

## 内容来源

原文来自 [framedsc.com/ReshadeGuides](https://framedsc.com/ReshadeGuides/index.htm)，版权归原作者所有。

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
