#!/usr/bin/env python3
"""Entry point for Codex Switcher (used by py2app and direct invocation)."""

import sys


def main():
    if "--dashboard" in sys.argv:
        # Override LSUIElement *before* pywebview touches Cocoa
        try:
            from AppKit import NSApplication, NSApplicationActivationPolicyRegular

            NSApplication.sharedApplication().setActivationPolicy_(
                NSApplicationActivationPolicyRegular
            )
        except Exception:
            pass

        from codex_switcher.dashboard import run_dashboard

        run_dashboard()
    else:
        from codex_switcher.app import main as app_main

        app_main()


if __name__ == "__main__":
    main()
