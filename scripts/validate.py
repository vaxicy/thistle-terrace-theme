# -*- coding: utf-8 -*-
import json
import re
import zipfile
from pathlib import Path

from PIL import Image, ImageStat

P = Path(__file__).resolve().parents[1]
SLUG = "thistle-terrace"
VARIANTS = ["light", "dark"]

themes = {v: json.loads((P / "themes" / f"{SLUG}-{v}-color-theme.json").read_text())
          for v in VARIANTS}

# colour specification table (one column per variant)
header = "| VS Code region | " + " | ".join(v.title() for v in VARIANTS) + " |"
sep = "|---|" + "|".join(["---"] * len(VARIANTS)) + "|"
rows = ["# Thistle & Terrace Theme colour specification", "", header, sep]
for k in themes["light"]["colors"]:
    rows.append("| `" + k + "` | " +
                " | ".join("`%s`" % themes[v]["colors"][k] for v in VARIANTS) + " |")
(P / "COLOR-SPEC.md").write_text("\n".join(rows) + "\n", encoding="utf-8")

for v, t in themes.items():
    bad = [c for c in t["colors"].values()
           if not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", c)]
    assert not bad, (v, bad)

for v, t in themes.items():
    im = Image.open(P / "store-assets/screenshots/en" / f"screenshot-{v}.png").convert("RGB")
    row = ImageStat.Stat(im.crop((0, 0, im.width, 1))).mean
    col = ImageStat.Stat(im.crop((0, 0, 1, im.height))).mean
    title_expected = tuple(int(t["colors"]["titleBar.activeBackground"][i:i + 2], 16)
                          for i in [1, 3, 5])
    act = ImageStat.Stat(im.crop((10, 60, 11, im.height - 40))).mean
    act_expected = tuple(int(t["colors"]["activityBar.background"][i:i + 2], 16)
                        for i in [1, 3, 5])
    assert max(abs(a - b) for a, b in zip(row, title_expected)) < 1, (v, row, title_expected)
    assert max(abs(a - b) for a, b in zip(act, act_expected)) < 2, (v, act, act_expected)
    print(v, len(t["colors"]), "UI colors;", t["type"], "screenshot", im.size,
          "titlebar", row, "activitybar", act)

archive = P / f"{SLUG}-theme-1.0.0.vsix"
if archive.exists():
    with zipfile.ZipFile(archive) as z:
        m = json.loads(z.read("extension/package.json"))
        assert m["publisher"] == "lilinhuang" and m["version"] == "1.0.0"
        assert len(m["contributes"]["themes"]) == 2
        for t in m["contributes"]["themes"]:
            assert "extension/" + t["path"].removeprefix("./") in z.namelist()
        assert 'Version="1.0.0"' in z.read("extension.vsixmanifest").decode()
    print("VSIX manifest, publisher, version and 2 theme entries verified")




