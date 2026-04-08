# Copyright 2025 GitBiao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Codex Model Switcher -- macOS menubar app for switching OpenRouter models in Codex Desktop."""

import subprocess
import threading

import rumps

from codex_switcher.config_manager import (
    get_current_model,
    get_current_reasoning_effort,
    read_config,
    set_reasoning_effort,
    switch_model,
)
from codex_switcher.models import (
    REASONING_EFFORTS,
    get_default_reasoning_effort,
    get_models,
    get_provider,
    load_switcher_config,
)
from codex_switcher.process_manager import restart_codex


class CodexSwitcherApp(rumps.App):
    def __init__(self):
        self.switcher_cfg = load_switcher_config()
        self.provider = get_provider(self.switcher_cfg)
        self.model_list = get_models(self.switcher_cfg)

        codex_doc = read_config()
        current_model = get_current_model(codex_doc)
        current_effort = get_current_reasoning_effort(codex_doc)

        short = self._short_name(current_model) if current_model else "---"
        super().__init__("Codex Switcher", quit_button=None)
        self.title = short

        self._build_menu(current_model, current_effort)

    def _short_name(self, model_id: str | None) -> str:
        if not model_id:
            return "N/A"
        for m in self.model_list:
            if m["id"] == model_id:
                return m.get("short_name", model_id)
        return model_id.split("/")[-1] if "/" in model_id else model_id

    def _build_menu(self, current_model: str | None, current_effort: str | None):
        if current_effort is None:
            current_effort = get_default_reasoning_effort(self.switcher_cfg)

        self.menu.clear()

        header = rumps.MenuItem(f"Current: {current_model or 'N/A'}")
        header.set_callback(None)
        self.menu.add(header)
        self.menu.add(rumps.separator)

        for m in self.model_list:
            item = rumps.MenuItem(m["id"], callback=self._on_model_click)
            item.state = 1 if m["id"] == current_model else 0
            self.menu.add(item)

        self.menu.add(rumps.separator)

        reasoning_menu = rumps.MenuItem("Reasoning Effort")
        for effort in REASONING_EFFORTS:
            sub = rumps.MenuItem(effort, callback=self._on_reasoning_click)
            sub.state = 1 if effort == current_effort else 0
            reasoning_menu.add(sub)
        self.menu.add(reasoning_menu)

        self.menu.add(rumps.separator)

        self.menu.add(rumps.MenuItem("Edit Models...", callback=self._on_edit_models))
        self.menu.add(rumps.MenuItem("Open config.toml", callback=self._on_open_config))
        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem("Quit", callback=rumps.quit_application))

    def _on_model_click(self, sender):
        model_id = sender.title
        if sender.state == 1:
            return

        old_title = self.title
        self.title = "..."

        def do_switch():
            try:
                switch_model(
                    model_id=model_id,
                    provider_key=self.provider["key"],
                    provider_name=self.provider["name"],
                    base_url=self.provider["base_url"],
                    env_key=self.provider["env_key"],
                    reasoning_effort=self._get_current_effort(),
                )
                restart_codex()
                self._refresh_state()
            except Exception as e:
                rumps.notification("Codex Switcher", "Error", str(e))
                self.title = old_title

        threading.Thread(target=do_switch, daemon=True).start()

    def _on_reasoning_click(self, sender):
        effort = sender.title
        reasoning_menu = self.menu["Reasoning Effort"]
        for key in reasoning_menu:
            reasoning_menu[key].state = 0
        sender.state = 1

        try:
            set_reasoning_effort(effort)
        except Exception as e:
            rumps.notification("Codex Switcher", "Error", str(e))

    def _on_edit_models(self, _sender):
        from codex_switcher.models import _DEFAULT_CONFIG_PATH
        subprocess.Popen(["open", str(_DEFAULT_CONFIG_PATH)])

    def _on_open_config(self, _sender):
        from codex_switcher.config_manager import CONFIG_PATH
        subprocess.Popen(["open", str(CONFIG_PATH)])

    def _get_current_effort(self) -> str:
        reasoning_menu = self.menu.get("Reasoning Effort")
        if reasoning_menu:
            for key in reasoning_menu:
                if reasoning_menu[key].state == 1:
                    return str(key)
        return get_default_reasoning_effort(self.switcher_cfg)

    def _refresh_state(self):
        doc = read_config()
        current_model = get_current_model(doc)
        current_effort = get_current_reasoning_effort(doc)
        self.title = self._short_name(current_model)
        self._build_menu(current_model, current_effort)


def main():
    app = CodexSwitcherApp()
    app.run()


if __name__ == "__main__":
    main()
