#!/usr/bin/env python3
"""Final polish pass for Chinese-localized ReShade guide pages."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = list(ROOT.glob("ReshadeGuides/**/*.htm"))
HTML_FILES += [ROOT / "ReshadeGuidesShaderguides.htm", ROOT / "ReshadeGuidesAddonguides.htm"]

REPLACEMENTS = [
    # Broken local gallery/project links → framedsc.com
    ('href="../HallOfFramed"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="../HOFWallpaper"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="../framed-wrapped"', 'href="https://framedsc.com/framed-wrapped/"'),
    ('href="../../HallOfFramed"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="../../HOFWallpaper"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="../../framed-wrapped"', 'href="https://framedsc.com/framed-wrapped/"'),
    ('href="/HallOfFramed/"', 'href="https://framedsc.com/HallOfFramed/"'),
    ('href="/HOFWallpaper/"', 'href="https://framedsc.com/HOFWallpaper/"'),
    ('href="/framed-wrapped/"', 'href="https://framedsc.com/framed-wrapped/"'),
    # Addon pages: site-wide nav links should point to framedsc.com
    ('href="../../index.htm"', 'href="https://framedsc.com/index.htm"'),
    ('href="../../basics.htm"', 'href="https://framedsc.com/basics.htm"'),
    ('href="../../Gameguides.htm"', 'href="https://framedsc.com/Gameguides.htm"'),
    ('href="../../GeneralGuides/index.htm"', 'href="https://framedsc.com/GeneralGuides/index.htm"'),
    ('href="../../PhotographyGuides/index.htm"', 'href="https://framedsc.com/PhotographyGuides/index.htm"'),
    ('href="../../cheattablearchive.htm"', 'href="https://framedsc.com/cheattablearchive.htm"'),
    ('href="../../the_photomode_wishlist.htm"', 'href="https://framedsc.com/the_photomode_wishlist.htm"'),
    ('href="../../inmemoriam.htm"', 'href="https://framedsc.com/inmemoriam.htm"'),
    ('href="../../contribute.htm"', 'href="https://framedsc.com/contribute.htm"'),
    ('href="../../joinus.htm"', 'href="https://framedsc.com/joinus.htm"'),
    ('action="../../Docnet_search.htm"', 'action="https://framedsc.com/Docnet_search.htm"'),
    ('href="../../GeneralGuides/cinematic-unity-explorer.md"',
     'href="https://framedsc.com/GeneralGuides/cinematic-unity-explorer.md"'),
    ('Supports IGCS Connector', '支持 IGCS Connector'),
    # Remaining English UI chrome
    ('<i class="fa fa-info-circle"></i> Info</span>', '<i class="fa fa-info-circle"></i> 信息</span>'),
    ('title="Permalink to this headline"', 'title="永久链接至标题"'),
    ('aria-label="main navigation"', 'aria-label="主导航"'),
    ('aria-label="top navigation"', 'aria-label="顶部导航"'),
    ('aria-label="breadcrumbs navigation"', 'aria-label="面包屑导航"'),
    # Terminology consistency
    ('>LUTs</a>', '>LUT</a>'),
    ('ReShade 仓库', 'ReShade 资源库'),
    # ShaderToggler UI labels (Chinese first, English in parens)
    ('<em>List of toggle groups</em>', '<em>切换组列表（List of toggle groups）</em>'),
    ('<em>Shader Toggler</em>', '<em>Shader Toggler</em>'),
    ('<em>New</em>', '<em>新建（New）</em>'),
    ('<em>Edit</em>', '<em>编辑（Edit）</em>'),
    ('<em>Change shaders</em>', '<em>更改着色器（Change shaders）</em>'),
    ('<em>Done</em>', '<em>完成（Done）</em>'),
    # MSADOF parameter labels
    ('<em>Frames to skip</em>', '<em>跳过帧数（Frames to skip）</em>'),
    ('<em>Shape size</em>', '<em>形状大小（Shape size）</em>'),
    ('<em>Number of rings</em>', '<em>环数（Number of rings）</em>'),
    ('<em>Game Adjustments</em>', '<em>游戏调整（Game Adjustments）</em>'),
    ('<em>Additional info</em>', '<em>附加信息（Additional info）</em>'),
    ('<em>Focus distance</em>', '<em>对焦距离（Focus distance）</em>'),
    ('<em>Show focus plane</em>', '<em>显示焦平面（Show focus plane）</em>'),
    ('<em>Camera movement multiplier</em>', '<em>相机移动倍率（Camera movement multiplier）</em>'),
    # Alert type fix: info box mislabeled as 提示
    ('alert alert-info"><span class="alert-title"><i class="fa fa-info-circle"></i> 提示</span><p>要执行脚本',
     'alert alert-info"><span class="alert-title"><i class="fa fa-info-circle"></i> 说明</span><p>要执行脚本'),
]


def polish_file(path: Path) -> bool:
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
        if polish_file(path):
            print(f"polished: {path.relative_to(ROOT)}")
            changed += 1
    print(f"Polished {changed} files")


if __name__ == "__main__":
    main()
