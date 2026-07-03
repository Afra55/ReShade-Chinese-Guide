#!/usr/bin/env python3
"""Apply shared Chinese UI translations to Reshade guide HTML pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HTML_FILES = list(ROOT.glob("ReshadeGuides/**/*.htm"))
HTML_FILES += [ROOT / "ReshadeGuidesShaderguides.htm", ROOT / "ReshadeGuidesAddonguides.htm"]

# Order matters: longer phrases first
REPLACEMENTS = [
    # Search & chrome
    ('placeholder="Search docs"', 'placeholder="搜索文档"'),
    ('lang="en"', 'lang="zh-CN"'),
    ('&copy 2019-2026 FRAMED. All rights reserved.', '&copy 2019-2026 FRAMED. 保留所有权利。'),
    ('<a href="https://github.com/FransBouma/DocNet" target="_blank">Made with <i class="fa fa-github"></i> DocNet</a>',
     '<a href="https://github.com/FransBouma/DocNet" target="_blank">由 <i class="fa fa-github"></i> DocNet 生成</a>'),
    # Reshade nav section
    ('Reshade guides', 'ReShade 指南'),
    ('Setting up reshade', '安装与配置 ReShade'),
    ('Shaders Catalogue', '着色器目录'),
    ('LUT Generation', 'LUT 生成'),
    ('Injecting ReShade in UWP games', '向 UWP 游戏注入 ReShade'),
    ('Exporting Depth Buffers with Reshade', '使用 ReShade 导出深度缓冲'),
    ('Using RLE to hide temporal issues', '使用 RLE 隐藏时序问题'),
    ('Shader guides', '着色器指南'),
    ('Addon guides', '插件指南'),
    # Shader guide entries
    ('Cinematic DOF', '电影感景深'),
    ('Height Fog', '高度雾'),
    # Addon guide entries
    ('ShaderToggler', 'ShaderToggler'),
    ('MSADOF', 'MSADOF'),
    # Page-specific sidebar TOC
    ('>Video</a>', '>视频教程</a>'),
    ('>Setting up Reshade for the game</a>', '>为游戏安装 ReShade</a>'),
    ('>Configuring Reshade</a>', '>配置 ReShade</a>'),
    (">Changing a technique's parameters</a>", '>调整效果技法的参数</a>'),
    ('>Checking depth buffer access</a>', '>检查深度缓冲访问</a>'),
    ('>Shader duplication</a>', '>着色器复制</a>'),
    ('>Depth buffer on online games</a>', '>联网游戏中的深度缓冲</a>'),
    ('>Using reshade alongisde other injectable mods</a>', '>与其他可注入模组同时使用 ReShade</a>'),
    ('>Further information</a>', '>延伸阅读</a>'),
    ('>Custom shader repositories</a>', '>自定义着色器仓库</a>'),
    ('>Recommended Shader Settings</a>', '>推荐着色器设置</a>'),
    ('>Example Usage</a>', '>使用示例</a>'),
    ('>Video Example</a>', '>视频示例</a>'),
    ('>Tools</a>', '>工具</a>'),
    ('>How to inject ReShade into an UWP game</a>', '>如何向 UWP 游戏注入 ReShade</a>'),
    ('>Preparation</a>', '>准备工作</a>'),
    ('>Find the game executable and Application ID</a>', '>查找游戏可执行文件与应用程序 ID</a>'),
    ('>Create your PowerShell injection script</a>', '>创建 PowerShell 注入脚本</a>'),
    ('>ReShade Repository</a>', '>ReShade 资源库</a>'),
    ('>Depth Slice</a>', '>深度切片</a>'),
    ('>Graded Depth Range</a>', '>分级深度范围</a>'),
    ('>High-range Depth Export</a>', '>高范围深度导出</a>'),
    ('>Tutorial: Adding fog using a depth map</a>', '>教程：使用深度图添加雾效</a>'),
    ('>Aligning the fog</a>', '>对齐雾效</a>'),
    ('>Tweaking the fog</a>', '>调整雾效</a>'),
    ('>Why would I want to use a LUT?</a>', '>为什么要使用 LUT？</a>'),
    ('>Installation</a>', '>安装</a>'),
    ('>Example usage: HUD removal</a>', '>使用示例：HUD 隐藏</a>'),
    ('>Repository</a>', '>文件库</a>'),
    # Breadcrumbs & titles
    ('FRAMED. Screenshot Community', 'FRAMED 截图社区'),
    ('>Home</a>', '>首页</a>'),
    ('>The Basics</a>', '>基础知识</a>'),
    ('>Game guides</a>', '>游戏指南</a>'),
    ('>General guides</a>', '>通用指南</a>'),
    ('>Photography guides</a>', '>摄影指南</a>'),
    ('>Cheat Table Archive</a>', '>作弊表存档</a>'),
    ('>The Photomode Wishlist</a>', '>拍照模式愿望清单</a>'),
    ('>In Memoriam</a>', '>纪念</a>'),
    ('>Contribute to the site!</a>', '>参与贡献！</a>'),
    ('<span class="navigationgroup">Galleries</span>', '<span class="navigationgroup">画廊</span>'),
    ('<span class="navigationgroup">Projects</span>', '<span class="navigationgroup">项目</span>'),
    ('>Hall of FRAMED</a>', '>FRAMED 名人堂</a>'),
    ('>HoF Wallpaper</a>', '>名人堂壁纸</a>'),
    ('>A Year of FRAMED</a>', '>FRAMED 年度回顾</a>'),
    # Alert labels
    ('<span class="alert-title"><i class="fa fa-info-circle"></i> Tip</span>',
     '<span class="alert-title"><i class="fa fa-info-circle"></i> 提示</span>'),
    ('<span class="alert-title"><i class="fa fa-warning"></i> Important!</span>',
     '<span class="alert-title"><i class="fa fa-warning"></i> 重要！</span>'),
    ('<span class="alert-title"><i class="fa fa-warning"></i> Warning</span>',
     '<span class="alert-title"><i class="fa fa-warning"></i> 警告</span>'),
    ('<span class="alert-title"><i class="fa fa-info-circle"></i> Note</span>',
     '<span class="alert-title"><i class="fa fa-info-circle"></i> 说明</span>'),
    ('<i class="fa fa-info-circle"></i> Info</span>', '<i class="fa fa-info-circle"></i> 信息</span>'),
    ('title="Permalink to this headline"', 'title="永久链接至标题"'),
    ('>LUTs</a>', '>LUT</a>'),
    ('ReShade 仓库', 'ReShade 资源库'),
    ('href="../HallOfFramed"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="../HOFWallpaper"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="../framed-wrapped"', 'href="https://framedsc.com/framed-wrapped/"'),
    ('href="../../HallOfFramed"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="../../HOFWallpaper"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="../../framed-wrapped"', 'href="https://framedsc.com/framed-wrapped/"'),
    ('href="/HallOfFramed/"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="/HOFWallpaper/"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="/framed-wrapped/"', 'href="https://framedsc.com/framed-wrapped/"'),
]


def translate_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for path in sorted(HTML_FILES):
        if translate_file(path):
            print(f"UI: {path.relative_to(ROOT)}")
            changed += 1
    print(f"Updated UI in {changed} files")


if __name__ == "__main__":
    main()
