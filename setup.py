"""py2app build configuration for Codex Switcher.

Build:
    python3 setup.py py2app

The resulting .app will be in dist/Codex Switcher.app
"""

from setuptools import setup

from codex_switcher import __version__

APP = ["main.py"]

OPTIONS = {
    "argv_emulation": False,
    "iconfile": "resources/icon.icns",
    "plist": {
        "CFBundleName": "Codex Switcher",
        "CFBundleDisplayName": "Codex Switcher",
        "CFBundleIdentifier": "com.gitbiao.codex-switcher",
        "CFBundleVersion": __version__,
        "CFBundleShortVersionString": __version__,
        "LSUIElement": True,
        "NSHighResolutionCapable": True,
        "NSHumanReadableCopyright": "Copyright © 2025 GitBiao. All rights reserved.",
    },
    "packages": ["codex_switcher"],
    "includes": ["rumps", "tomlkit", "webview", "bottle", "proxy_tools"],
    "resources": ["codex_switcher/switcher_config.json"],
}

setup(
    name="Codex Switcher",
    version=__version__,
    app=APP,
    options={"py2app": OPTIONS},
)
