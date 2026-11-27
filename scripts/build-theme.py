# -*- coding: utf-8 -*-
"""Build the Thistle & Terrace Theme (two variants) from one base table.

    py -3 scripts/build-theme.py

Variants: light / dark.
The shared table carries the chrome (borders, ansi, diagnostics); each variant
overrides the identity keys - surfaces, accent, status bar - from a small set
of primitives.
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "thistle-terrace-theme"
SLUG = "thistle-terrace"
DISPLAY = "Thistle & Terrace Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/thistle-terrace-theme"

# shared winter chrome: (light, dark)
UI = {
    "foreground": ("#2A3440", "#E2E9F1"),
    "editor.foreground": ("#2A3440", "#E2E9F1"),
    "terminal.foreground": ("#2A3440", "#E2E9F1"),
    "input.foreground": ("#24303C", "#E6ECF2"),
    "dropdown.foreground": ("#24303C", "#E6ECF2"),
    "quickInput.foreground": ("#24303C", "#E6ECF2"),
    "editorWidget.foreground": ("#24303C", "#E6ECF2"),
    "editorHoverWidget.foreground": ("#24303C", "#E6ECF2"),
    "editorSuggestWidget.foreground": ("#24303C", "#E6ECF2"),
    "notifications.foreground": ("#24303C", "#E6ECF2"),
    "descriptionForeground": ("#6F7A86", "#93A3B3"),
    "input.placeholderForeground": ("#6F7A86", "#93A3B3"),
    "focusBorder": ("#3F6BA6", "#94B4C1"),
    "inputOption.activeBorder": ("#35609A", "#A9C4CF"),
    "input.border": ("#D2D1C8", "#28405A"),
    "dropdown.border": ("#D2D1C8", "#28405A"),
    "editor.background": ("#E9E9E4", "#17293D"),
    "tab.activeBackground": ("#E9E9E4", "#17293D"),
    "titleBar.activeBackground": ("#DEDDD6", "#122031"),
    "titleBar.activeForeground": ("#2A3440", "#E2E9F1"),
    "titleBar.inactiveBackground": ("#D7D6CE", "#0E1926"),
    "titleBar.inactiveForeground": ("#9AA4AE", "#64788B"),
    "activityBar.background": ("#E1E0D9", "#0F1D2C"),
    "activityBar.foreground": ("#3F6BA6", "#94B4C1"),
    "activityBar.activeBorder": ("#3F6BA6", "#94B4C1"),
    "activityBar.inactiveForeground": ("#9AA4AE", "#5C7183"),
    "sideBar.background": ("#EDEDE8", "#1D3149"),
    "sideBar.foreground": ("#2A3440", "#D8E1EA"),
    "sideBarSectionHeader.background": ("#E0DFD7", "#223850"),
    "sideBarSectionHeader.foreground": ("#46525E", "#D3DDE7"),
    "panel.background": ("#EBEBE6", "#152538"),
    "terminal.background": ("#EBEBE6", "#152538"),
    "panel.border": ("#D2D1C8", "#28405A"),
    "editorGroup.border": ("#D2D1C8", "#28405A"),
    "tab.border": ("#D2D1C8", "#28405A"),
    "sideBar.border": ("#D2D1C8", "#28405A"),
    "titleBar.border": ("#D2D1C8", "#28405A"),
    "statusBar.background": ("#3F6BA6", "#94B4C1"),
    "statusBar.noFolderBackground": ("#3F6BA6", "#94B4C1"),
    "statusBar.foreground": ("#F4F7FB", "#0E1926"),
    "statusBar.noFolderForeground": ("#F4F7FB", "#0E1926"),
    "statusBarItem.hoverBackground": ("#35609A", "#A9C4CF"),
    "statusBar.debuggingBackground": ("#A2642A", "#E0B48A"),
    "statusBar.debuggingForeground": ("#F7F8FA", "#14232F"),
    "editorGroupHeader.tabsBackground": ("#E1E0D9", "#132235"),
    "tab.inactiveBackground": ("#E1E0D9", "#132235"),
    "tab.activeForeground": ("#2A3440", "#E8EEF4"),
    "tab.activeBorderTop": ("#3F6BA6", "#94B4C1"),
    "tab.inactiveForeground": ("#6F7A86", "#8496A6"),
    "tab.hoverBackground": ("#E2E1D9", "#21374F"),
    "tab.activeModifiedBorder": ("#A2642A", "#E8C27E"),
    "tab.inactiveModifiedBorder": ("#A2642A", "#E8C27E"),
    "list.hoverBackground": ("#E2E1D9", "#21374F"),
    "list.activeSelectionBackground": ("#CBD6E4", "#2E4A66"),
    "editorSuggestWidget.selectedBackground": ("#CBD6E4", "#2E4A66"),
    "list.activeSelectionForeground": ("#24303C", "#E8EEF4"),
    "list.inactiveSelectionForeground": ("#24303C", "#E8EEF4"),
    "editorSuggestWidget.selectedForeground": ("#24303C", "#E8EEF4"),
    "list.inactiveSelectionBackground": ("#DDE3EA", "#254058"),
    "list.highlightForeground": ("#35609A", "#A9C4CF"),
    "list.focusHighlightForeground": ("#35609A", "#A9C4CF"),
    "tree.indentGuidesStroke": ("#D2D1C8", "#28405A"),
    "editorLineNumber.foreground": ("#9AA4AE", "#5C7183"),
    "editorLineNumber.activeForeground": ("#3F6BA6", "#94B4C1"),
    "editor.lineHighlightBackground": ("#F0F0EB", "#1C3149"),
    "editor.lineHighlightBorder": ("#DAD9D0", "#22384F"),
    "editorCursor.foreground": ("#3F6BA6", "#94B4C1"),
    "selection.background": ("#CBD6E4", "#2E4A66"),
    "editor.selectionBackground": ("#CBD6E4", "#2E4A66"),
    "terminal.selectionBackground": ("#CBD6E4", "#2E4A66"),
    "editor.inactiveSelectionBackground": ("#DDE3EA", "#254058"),
    "editor.wordHighlightBackground": ("#CBD6E480", "#3D5F8099"),
    "editor.wordHighlightStrongBackground": ("#CBD6E480", "#3D5F8099"),
    "editor.selectionHighlightBackground": ("#CBD6E466", "#3D5F8088"),
    "editor.findMatchHighlightBackground": ("#DCE6F0", "#35567A"),
    "editor.findMatchBackground": ("#BFD3E8", "#4E76A3"),
    "editor.findMatchBorder": ("#35609A", "#A9C4CF"),
    "editorBracketMatch.background": ("#E4E7EF", "#21374F"),
    "editorBracketMatch.border": ("#3F6BA6", "#94B4C1"),
    "editorIndentGuide.background1": ("#DAD9D0", "#22384F"),
    "editorIndentGuide.activeBackground1": ("#9AA4AE", "#4A6480"),
    "editorWhitespace.foreground": ("#DAD9D0", "#22384F"),
    "editorRuler.foreground": ("#E2E1D9", "#1C3149"),
    "textLink.foreground": ("#35609A", "#A9C4CF"),
    "textLink.activeForeground": ("#3F6BA6", "#C2D8E2"),
    "editorLink.activeForeground": ("#3F6BA6", "#C2D8E2"),
    "quickInput.background": ("#F3F3EE", "#1B2F44"),
    "editorHoverWidget.background": ("#F3F3EE", "#1B2F44"),
    "notifications.background": ("#F3F3EE", "#1B2F44"),
    "input.background": ("#F6F6F1", "#14243A"),
    "dropdown.background": ("#F6F6F1", "#14243A"),
    "editorWidget.background": ("#F3F3EE", "#1B2F44"),
    "editorSuggestWidget.background": ("#F3F3EE", "#1B2F44"),
    "editorWidget.border": ("#CFCEC4", "#2C4459"),
    "editorHoverWidget.border": ("#CFCEC4", "#2C4459"),
    "editorSuggestWidget.border": ("#CFCEC4", "#2C4459"),
    "notifications.border": ("#CFCEC4", "#2C4459"),
    "button.background": ("#3F6BA6", "#94B4C1"),
    "button.foreground": ("#F4F7FB", "#0E1926"),
    "button.hoverBackground": ("#35609A", "#A9C4CF"),
    "button.secondaryBackground": ("#E0DFD7", "#21374F"),
    "button.secondaryForeground": ("#2A3440", "#D8E1EA"),
    "button.secondaryHoverBackground": ("#CBD6E4", "#2E4A66"),
    "badge.background": ("#35609A", "#94B4C1"),
    "activityBarBadge.background": ("#35609A", "#94B4C1"),
    "badge.foreground": ("#F4F7FB", "#0E1926"),
    "activityBarBadge.foreground": ("#F4F7FB", "#0E1926"),
    "scrollbarSlider.background": ("#9AA4AE66", "#64788B88"),
    "scrollbarSlider.hoverBackground": ("#6F7A8688", "#8496A699"),
    "scrollbarSlider.activeBackground": ("#3F6BA699", "#94B4C199"),
    "errorForeground": ("#B3402F", "#F0928A"),
    "editorError.foreground": ("#B3402F", "#F0928A"),
    "problemsErrorIcon.foreground": ("#B3402F", "#F0928A"),
    "gitDecoration.deletedResourceForeground": ("#B3402F", "#F0928A"),
    "editorGutter.deletedBackground": ("#B3402F", "#F0928A"),
    "editorWarning.foreground": ("#A2642A", "#E8C27E"),
    "problemsWarningIcon.foreground": ("#A2642A", "#E8C27E"),
    "editorInfo.foreground": ("#3F6B84", "#9CC3DC"),
    "problemsInfoIcon.foreground": ("#3F6B84", "#9CC3DC"),
    "gitDecoration.addedResourceForeground": ("#3F7A52", "#8FC9A0"),
    "gitDecoration.untrackedResourceForeground": ("#3F7A52", "#8FC9A0"),
    "editorGutter.addedBackground": ("#3F7A52", "#8FC9A0"),
    "gitDecoration.modifiedResourceForeground": ("#A2642A", "#E8C27E"),
    "editorGutter.modifiedBackground": ("#A2642A", "#E8C27E"),
    "diffEditor.insertedTextBackground": ("#CFE4D5AA", "#2E4A3A66"),
    "diffEditor.removedTextBackground": ("#F2D5D8AA", "#5A2A3366"),
    "diffEditor.insertedLineBackground": ("#CFE4D566", "#2E4A3A44"),
    "diffEditor.removedLineBackground": ("#F2D5D866", "#5A2A3344"),
    "terminal.ansiBlack": ("#2A3440", "#132235"),
    "terminal.ansiRed": ("#B3402F", "#F0928A"),
    "terminal.ansiGreen": ("#3F7A52", "#8FC9A0"),
    "terminal.ansiYellow": ("#A2642A", "#E8C27E"),
    "terminal.ansiBlue": ("#2F5FA8", "#86B4F0"),
    "terminal.ansiMagenta": ("#6A4C93", "#C0A6EA"),
    "terminal.ansiCyan": ("#2E6E6A", "#8FD0C4"),
    "terminal.ansiWhite": ("#6F7A86", "#D8E1EA"),
    "terminal.ansiBrightBlack": ("#5C6874", "#5C7183"),
    "terminal.ansiBrightRed": ("#CC5B54", "#F5AEA6"),
    "terminal.ansiBrightGreen": ("#5E9A6E", "#A9DDB8"),
    "terminal.ansiBrightYellow": ("#BC8C2E", "#F2D89A"),
    "terminal.ansiBrightBlue": ("#4A79C0", "#A8C9F0"),
    "terminal.ansiBrightMagenta": ("#8363A6", "#D4BDEE"),
    "terminal.ansiBrightCyan": ("#3E8E88", "#A8E0DC"),
    "terminal.ansiBrightWhite": ("#24303C", "#E8EEF4"),
}

# per-variant primitives; the identity keys are derived from these
VARIANTS = {
    "light": dict(
        dark=False, label="Thistle & Terrace Light",
        bg="#ACCFC5", chrome="#A6C8BF", chrome_inactive="#9DBFB5",
        sidebar="#B5D4CB", sidebar_hdr="#A8C9C0", panel="#B8D6CD",
        tabs="#A6C8BF", activity="#A6C8BF",
        fg="#2B1C2F", fg_dim="#6B5570", fg_faint="#9A88A0",
        border="#93B7AD", hover="#A6C8BF", sel="#D9C4DD",
        sel_inactive="#C7DFD7", line_hl="#DCEAE5", line_hl_border="#A2C4BA",
        accent="#7E4E88", accent_hi="#6F4278", accent_lo="#96639F",
        accent_fg="#F8F1E6", widget="#F1E3C4", widget_border="#9FBFB5",
        input="#E9F2ED"),
    "dark": dict(
        dark=True, label="Thistle & Terrace Dark",
        bg="#301A2A", chrome="#200F1A", chrome_inactive="#1A0D16",
        sidebar="#2D1424", sidebar_hdr="#33192A", panel="#2A1523",
        tabs="#1B0E16", activity="#1B1019",
        fg="#EFE3EE", fg_dim="#BBA2BF", fg_faint="#8D778F",
        border="#3A1C2B", hover="#33192A", sel="#4A2A40",
        sel_inactive="#301827", line_hl="#2E1624", line_hl_border="#3A1C2B",
        accent="#AF8EB1", accent_hi="#C2A2C4", accent_lo="#987B9A",
        accent_fg="#241627", widget="#2A1523", widget_border="#3A1C2B",
        input="#24111D"),
}

def overrides(p):
    """Derive the identity keys from a variant's primitives."""
    return {
        "foreground": p["fg"],
        "editor.foreground": p["fg"],
        "terminal.foreground": p["fg"],
        "input.foreground": p["fg"],
        "dropdown.foreground": p["fg"],
        "quickInput.foreground": p["fg"],
        "editorWidget.foreground": p["fg"],
        "editorHoverWidget.foreground": p["fg"],
        "editorSuggestWidget.foreground": p["fg"],
        "notifications.foreground": p["fg"],
        "descriptionForeground": p["fg_dim"],
        "input.placeholderForeground": p["fg_dim"],
        "focusBorder": p["accent"],
        "inputOption.activeBorder": p["accent_hi"],
        "input.border": p["border"],
        "dropdown.border": p["border"],
        "editor.background": p["bg"],
        "tab.activeBackground": p["bg"],
        "titleBar.activeBackground": p["chrome"],
        "titleBar.activeForeground": p["fg"],
        "titleBar.inactiveBackground": p["chrome_inactive"],
        "titleBar.inactiveForeground": p["fg_faint"],
        "activityBar.background": p["activity"],
        "activityBar.foreground": p["accent"],
        "activityBar.activeBorder": p["accent"],
        "activityBar.inactiveForeground": p["fg_faint"],
        "sideBar.background": p["sidebar"],
        "sideBar.foreground": p["fg"],
        "sideBarSectionHeader.background": p["sidebar_hdr"],
        "sideBarSectionHeader.foreground": p["fg_dim"],
        "panel.background": p["panel"],
        "terminal.background": p["panel"],
        "panel.border": p["border"],
        "editorGroup.border": p["border"],
        "tab.border": p["border"],
        "sideBar.border": p["border"],
        "titleBar.border": p["border"],
        "statusBar.background": p["accent"],
        "statusBar.noFolderBackground": p["accent"],
        "statusBar.foreground": p["accent_fg"],
        "statusBar.noFolderForeground": p["accent_fg"],
        "statusBarItem.hoverBackground": p["accent_hi"],
        "editorGroupHeader.tabsBackground": p["tabs"],
        "tab.inactiveBackground": p["tabs"],
        "tab.activeForeground": p["fg"],
        "tab.activeBorderTop": p["accent"],
        "tab.inactiveForeground": p["fg_dim"],
        "tab.hoverBackground": p["hover"],
        "list.hoverBackground": p["hover"],
        "list.activeSelectionBackground": p["sel"],
        "editorSuggestWidget.selectedBackground": p["sel"],
        "list.activeSelectionForeground": p["fg"],
        "list.inactiveSelectionForeground": p["fg"],
        "editorSuggestWidget.selectedForeground": p["fg"],
        "list.inactiveSelectionBackground": p["sel_inactive"],
        "list.highlightForeground": p["accent_hi"],
        "list.focusHighlightForeground": p["accent_hi"],
        "tree.indentGuidesStroke": p["border"],
        "editorLineNumber.foreground": p["fg_faint"],
        "editorLineNumber.activeForeground": p["accent"],
        "editor.lineHighlightBackground": p["line_hl"],
        "editor.lineHighlightBorder": p["line_hl_border"],
        "editorCursor.foreground": p["accent"],
        "selection.background": p["sel"],
        "editor.selectionBackground": p["sel"],
        "terminal.selectionBackground": p["sel"],
        "editor.inactiveSelectionBackground": p["sel_inactive"],
        "editor.wordHighlightBackground": p["sel"] + "80",
        "editor.wordHighlightStrongBackground": p["sel"] + "80",
        "editor.selectionHighlightBackground": p["sel"] + "66",
        "editorBracketMatch.background": p["hover"],
        "editorBracketMatch.border": p["accent"],
        "editorIndentGuide.background1": p["line_hl_border"],
        "editorIndentGuide.activeBackground1": p["fg_faint"],
        "editorWhitespace.foreground": p["line_hl_border"],
        "editorRuler.foreground": p["hover"],
        "textLink.foreground": p["accent_hi"],
        "textLink.activeForeground": p["accent"],
        "editorLink.activeForeground": p["accent"],
        "quickInput.background": p["widget"],
        "editorHoverWidget.background": p["widget"],
        "notifications.background": p["widget"],
        "input.background": p["input"],
        "dropdown.background": p["input"],
        "editorWidget.background": p["widget"],
        "editorSuggestWidget.background": p["widget"],
        "editorWidget.border": p["widget_border"],
        "editorHoverWidget.border": p["widget_border"],
        "editorSuggestWidget.border": p["widget_border"],
        "notifications.border": p["widget_border"],
        "button.background": p.get("button", p["accent"]),
        "button.foreground": p["accent_fg"],
        "button.hoverBackground": p.get("button_hover", p["accent_hi"]),
        "button.secondaryBackground": p["hover"],
        "button.secondaryForeground": p["fg"],
        "button.secondaryHoverBackground": p["sel"],
        "badge.background": p["accent_hi"],
        "activityBarBadge.background": p["accent_hi"],
        "badge.foreground": p["accent_fg"],
        "activityBarBadge.foreground": p["accent_fg"],
        "scrollbarSlider.background": p["fg_faint"] + "66",
        "scrollbarSlider.hoverBackground": p["fg_dim"] + "88",
        "scrollbarSlider.activeBackground": p["accent"] + "99",
    }


TOKENS = [
    ("comment", ("#7E8A96", "#7C8A98"), "italic"),
    (("keyword", "storage"), ("#2F5FA8", "#86B4F0"), None),
    ("string", ("#3F7A52", "#96D3A6"), None),
    (("entity.name.function", "support.function"), ("#6A4C93", "#C0A6EA"), None),
    (("entity.name.type", "support.type", "support.class"), ("#8A5A2B", "#E0B48A"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#A2642A", "#E8C27E"), None),
    ("variable", ("#2A3440", "#E2E9F1"), None),
    ("variable.parameter", ("#5A6675", "#AFBBC9"), None),
    (("variable.other.property", "support.variable.property"), ("#7A5236", "#D6B396"), None),
    ("keyword.operator", ("#6B7684", "#9AA6B4"), None),
    ("punctuation", ("#8A94A0", "#8A94A0"), None),
    ("entity.name.tag", ("#2F5FA8", "#86B4F0"), None),
    ("entity.other.attribute-name", ("#A2642A", "#E8C27E"), None),
    ("string.regexp", ("#A64B6A", "#EFA0B8"), None),
    ("constant.character.escape", ("#A2642A", "#E8C27E"), None),
    ("markup.heading", ("#1E2A38", "#F2F6FA"), "bold"),
    ("markup.bold", ("#1E2A38", "#F2F6FA"), "bold"),
    ("markup.italic", ("#1E2A38", "#F2F6FA"), "italic"),
    ("invalid", ("#B3402F", "#F0928A"), None),
]

SEMANTIC = {
    "variable": "#2A3440|#E2E9F1",
    "parameter": "#5A6675|#AFBBC9",
    "property": "#7A5236|#D6B396",
    "function": "#6A4C93|#C0A6EA",
    "method": "#6A4C93|#C0A6EA",
    "type": "#8A5A2B|#E0B48A",
    "class": "#8A5A2B|#E0B48A",
    "interface": "#8A5A2B|#E0B48A",
    "variable.readonly": "#A2642A|#E8C27E",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "Thistle purple over a sage terrace, in a light and a dark cut.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "purple", "thistle", "terrace", "sage", "mauve", "lilac"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#2E1F31", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": p["label"],
             "uiTheme": "vs-dark" if p["dark"] else "vs",
             "path": f"./themes/{SLUG}-{name}-color-theme.json"}
            for name, p in VARIANTS.items()
        ]
    },
}


def build(name, p):
    index = 1 if p["dark"] else 0
    over = overrides(p)
    colors = {key: over.get(key, pair[index]) for key, pair in UI.items()}

    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})

    theme = {
        "name": p["label"],
        "type": "dark" if p["dark"] else "light",
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{name}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors", theme["type"])


def main():
    THEMES.mkdir(exist_ok=True)
    for name, p in VARIANTS.items():
        build(name, p)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json with", len(VARIANTS), "themes")


if __name__ == "__main__":
    main()








