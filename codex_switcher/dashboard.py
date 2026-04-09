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

"""Dashboard for managing Codex Switcher configuration via a native pywebview window."""

import webview

from codex_switcher.models import (
    REASONING_EFFORTS,
    load_switcher_config,
    save_switcher_config,
)


class DashboardAPI:
    """Python API exposed to the webview JavaScript frontend."""

    def get_config(self):
        cfg = load_switcher_config()
        cfg["_reasoning_efforts"] = REASONING_EFFORTS
        return cfg

    def save_full_config(self, data: dict):
        data.pop("_reasoning_efforts", None)
        save_switcher_config(data)
        return {"ok": True}

    def add_model(self, model_id: str, short_name: str):
        cfg = load_switcher_config()
        cfg.setdefault("models", []).append(
            {"id": model_id, "short_name": short_name, "enabled": True}
        )
        save_switcher_config(cfg)
        return cfg

    def update_model(self, index: int, model_id: str, short_name: str, enabled: bool):
        cfg = load_switcher_config()
        models = cfg.get("models", [])
        if 0 <= index < len(models):
            models[index] = {"id": model_id, "short_name": short_name, "enabled": enabled}
            save_switcher_config(cfg)
        return cfg

    def delete_model(self, index: int):
        cfg = load_switcher_config()
        models = cfg.get("models", [])
        if 0 <= index < len(models):
            models.pop(index)
            save_switcher_config(cfg)
        return cfg

    def toggle_model(self, index: int):
        cfg = load_switcher_config()
        models = cfg.get("models", [])
        if 0 <= index < len(models):
            models[index]["enabled"] = not models[index].get("enabled", True)
            save_switcher_config(cfg)
        return cfg

    def update_provider(self, key: str, name: str, base_url: str, env_key: str):
        cfg = load_switcher_config()
        cfg["provider"] = {
            "key": key,
            "name": name,
            "base_url": base_url,
            "env_key": env_key,
        }
        save_switcher_config(cfg)
        return cfg

    def update_reasoning_effort(self, effort: str):
        cfg = load_switcher_config()
        cfg["default_reasoning_effort"] = effort
        save_switcher_config(cfg)
        return cfg


HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Codex Switcher Dashboard</title>
<style>
:root {
  --bg: #1e1e2e;
  --surface: #282840;
  --surface2: #313150;
  --border: #3e3e5e;
  --text: #e0e0f0;
  --text2: #a0a0c0;
  --accent: #7c6ff7;
  --accent-hover: #9488ff;
  --danger: #e05070;
  --danger-hover: #f06080;
  --success: #40c080;
  --radius: 8px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
@media (prefers-color-scheme: light) {
  :root {
    --bg: #f5f5fa;
    --surface: #ffffff;
    --surface2: #eeeef5;
    --border: #d0d0e0;
    --text: #1e1e2e;
    --text2: #606080;
    --accent: #6c5ce7;
    --accent-hover: #5a4bd6;
    --danger: #d04060;
    --danger-hover: #c03050;
    --success: #30a868;
  }
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: var(--font);
  background: var(--bg);
  color: var(--text);
  line-height: 1.5;
  overflow-x: hidden;
}
.container { max-width: 660px; margin: 0 auto; padding: 24px 20px; }
h1 { font-size: 20px; font-weight: 600; margin-bottom: 20px; }
h2 {
  font-size: 14px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.5px; color: var(--text2); margin-bottom: 12px;
}

/* Sections */
.section {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 16px;
  margin-bottom: 16px;
}
.section-header {
  display: flex; align-items: center; justify-content: space-between;
  cursor: pointer; user-select: none;
}
.section-header .arrow {
  transition: transform 0.2s;
  font-size: 12px; color: var(--text2);
}
.section-header.collapsed .arrow { transform: rotate(-90deg); }
.section-body { margin-top: 12px; }
.section-body.hidden { display: none; }

/* Form grid */
.form-grid {
  display: grid; grid-template-columns: 120px 1fr;
  gap: 8px 12px; align-items: center;
}
.form-grid label { font-size: 13px; color: var(--text2); text-align: right; }
.form-grid input, .form-grid select {
  background: var(--surface2); border: 1px solid var(--border);
  border-radius: 6px; padding: 7px 10px; color: var(--text);
  font-size: 13px; font-family: var(--font); outline: none;
  transition: border-color 0.15s;
}
.form-grid input:focus, .form-grid select:focus {
  border-color: var(--accent);
}

/* Model list */
.model-row {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 12px;
  background: var(--surface2);
  border-radius: 6px;
  margin-bottom: 6px;
  transition: opacity 0.2s;
}
.model-row.disabled { opacity: 0.5; }
.model-info { flex: 1; min-width: 0; }
.model-id { font-size: 13px; font-weight: 500; word-break: break-all; }
.model-short { font-size: 12px; color: var(--text2); }

/* Toggle switch */
.toggle { position: relative; width: 40px; height: 22px; flex-shrink: 0; }
.toggle input { opacity: 0; width: 0; height: 0; }
.toggle .slider {
  position: absolute; inset: 0; background: var(--border);
  border-radius: 11px; cursor: pointer; transition: background 0.2s;
}
.toggle .slider::before {
  content: ""; position: absolute; width: 16px; height: 16px;
  left: 3px; top: 3px; background: white; border-radius: 50%;
  transition: transform 0.2s;
}
.toggle input:checked + .slider { background: var(--success); }
.toggle input:checked + .slider::before { transform: translateX(18px); }

/* Buttons */
.btn {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 6px 14px; border: none; border-radius: 6px;
  font-size: 13px; font-family: var(--font); cursor: pointer;
  transition: background 0.15s, opacity 0.15s;
}
.btn-primary { background: var(--accent); color: white; }
.btn-primary:hover { background: var(--accent-hover); }
.btn-danger { background: transparent; color: var(--danger); padding: 6px 8px; }
.btn-danger:hover { background: var(--danger); color: white; }
.btn-ghost { background: transparent; color: var(--text2); padding: 6px 8px; }
.btn-ghost:hover { background: var(--surface2); color: var(--text); }
.btn-sm { padding: 4px 10px; font-size: 12px; }

.actions { display: flex; gap: 4px; flex-shrink: 0; }

/* Modal overlay */
.modal-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,0.5); z-index: 100;
  justify-content: center; align-items: center;
}
.modal-overlay.active { display: flex; }
.modal {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 24px; width: 400px;
  max-width: 90vw;
}
.modal h3 { font-size: 16px; margin-bottom: 16px; }
.modal-actions { display: flex; justify-content: flex-end; gap: 8px; margin-top: 20px; }

/* Footer bar */
.footer {
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 8px;
}

/* Drag region for native title bar feel */
.drag-region {
  -webkit-app-region: drag;
  padding: 8px 0;
}
.drag-region * { -webkit-app-region: no-drag; }

/* Save button animation */
.btn-save-ok { background: var(--success) !important; }
</style>
</head>
<body>
<div class="container">
  <div class="drag-region"><h1>Codex Switcher Dashboard</h1></div>

  <!-- Provider Section -->
  <div class="section">
    <div class="section-header" onclick="toggleSection(this)">
      <h2 style="margin:0">Provider</h2>
      <span class="arrow">&#9660;</span>
    </div>
    <div class="section-body" id="providerBody">
      <div class="form-grid">
        <label>Key</label>
        <input id="provKey" placeholder="openrouter">
        <label>Name</label>
        <input id="provName" placeholder="OpenRouter">
        <label>Base URL</label>
        <input id="provUrl" placeholder="https://...">
        <label>Env Key</label>
        <input id="provEnv" placeholder="OPENROUTER_API_KEY">
      </div>
      <div style="margin-top:12px; text-align:right">
        <button class="btn btn-primary btn-sm" onclick="saveProvider()">Save Provider</button>
      </div>
    </div>
  </div>

  <!-- Models Section -->
  <div class="section">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px">
      <h2 style="margin:0">Models</h2>
      <button class="btn btn-primary btn-sm" onclick="openAddModal()">+ Add Model</button>
    </div>
    <div id="modelList"></div>
  </div>

  <!-- Reasoning Effort -->
  <div class="section">
    <div class="form-grid">
      <label>Reasoning</label>
      <select id="reasoningEffort" onchange="saveReasoning()"></select>
    </div>
  </div>
</div>

<!-- Add / Edit Modal -->
<div class="modal-overlay" id="modalOverlay">
  <div class="modal">
    <h3 id="modalTitle">Add Model</h3>
    <div class="form-grid">
      <label>Model ID</label>
      <input id="modalId" placeholder="provider/model-name">
      <label>Short Name</label>
      <input id="modalShort" placeholder="model-name">
    </div>
    <div class="modal-actions">
      <button class="btn btn-ghost" onclick="closeModal()">Cancel</button>
      <button class="btn btn-primary" id="modalSave" onclick="saveModal()">Save</button>
    </div>
  </div>
</div>

<script>
let config = {};
let editIndex = -1;

async function init() {
  config = await pywebview.api.get_config();
  render();
}

function render() {
  // Provider
  const p = config.provider || {};
  document.getElementById("provKey").value = p.key || "";
  document.getElementById("provName").value = p.name || "";
  document.getElementById("provUrl").value = p.base_url || "";
  document.getElementById("provEnv").value = p.env_key || "";

  // Reasoning effort
  const sel = document.getElementById("reasoningEffort");
  sel.innerHTML = "";
  (config._reasoning_efforts || []).forEach(e => {
    const opt = document.createElement("option");
    opt.value = e; opt.textContent = e;
    if (e === config.default_reasoning_effort) opt.selected = true;
    sel.appendChild(opt);
  });

  // Models
  const list = document.getElementById("modelList");
  list.innerHTML = "";
  (config.models || []).forEach((m, i) => {
    const enabled = m.enabled !== false;
    const row = document.createElement("div");
    row.className = "model-row" + (enabled ? "" : " disabled");
    row.innerHTML = `
      <label class="toggle">
        <input type="checkbox" ${enabled ? "checked" : ""} onchange="toggleModel(${i})">
        <span class="slider"></span>
      </label>
      <div class="model-info">
        <div class="model-id">${esc(m.id)}</div>
        <div class="model-short">${esc(m.short_name)}</div>
      </div>
      <div class="actions">
        <button class="btn btn-ghost btn-sm" onclick="openEditModal(${i})">Edit</button>
        <button class="btn btn-danger btn-sm" onclick="deleteModel(${i})">Del</button>
      </div>
    `;
    list.appendChild(row);
  });
}

function esc(s) {
  const d = document.createElement("div");
  d.textContent = s || "";
  return d.innerHTML;
}

function toggleSection(header) {
  header.classList.toggle("collapsed");
  header.nextElementSibling.classList.toggle("hidden");
}

async function toggleModel(i) {
  config = await pywebview.api.toggle_model(i);
  render();
}

async function deleteModel(i) {
  config = await pywebview.api.delete_model(i);
  render();
}

async function saveProvider() {
  config = await pywebview.api.update_provider(
    document.getElementById("provKey").value,
    document.getElementById("provName").value,
    document.getElementById("provUrl").value,
    document.getElementById("provEnv").value
  );
  flashBtn(event.target);
}

async function saveReasoning() {
  const val = document.getElementById("reasoningEffort").value;
  config = await pywebview.api.update_reasoning_effort(val);
}

function openAddModal() {
  editIndex = -1;
  document.getElementById("modalTitle").textContent = "Add Model";
  document.getElementById("modalId").value = "";
  document.getElementById("modalShort").value = "";
  document.getElementById("modalOverlay").classList.add("active");
  document.getElementById("modalId").focus();
}

function openEditModal(i) {
  editIndex = i;
  const m = config.models[i];
  document.getElementById("modalTitle").textContent = "Edit Model";
  document.getElementById("modalId").value = m.id;
  document.getElementById("modalShort").value = m.short_name;
  document.getElementById("modalOverlay").classList.add("active");
  document.getElementById("modalId").focus();
}

function closeModal() {
  document.getElementById("modalOverlay").classList.remove("active");
}

async function saveModal() {
  const id = document.getElementById("modalId").value.trim();
  const short = document.getElementById("modalShort").value.trim();
  if (!id) return;

  if (editIndex < 0) {
    config = await pywebview.api.add_model(id, short || id.split("/").pop());
  } else {
    const enabled = config.models[editIndex].enabled !== false;
    config = await pywebview.api.update_model(editIndex, id, short || id.split("/").pop(), enabled);
  }
  closeModal();
  render();
}

function flashBtn(btn) {
  btn.classList.add("btn-save-ok");
  setTimeout(() => btn.classList.remove("btn-save-ok"), 800);
}

// Handle Enter key in modal
document.addEventListener("keydown", e => {
  if (e.key === "Enter" && document.getElementById("modalOverlay").classList.contains("active")) {
    saveModal();
  }
  if (e.key === "Escape") closeModal();
});

window.addEventListener("pywebviewready", init);
</script>
</body>
</html>
"""


def _set_dashboard_app_name() -> None:
    try:
        import os

        from AppKit import NSApplication, NSApplicationActivationPolicyRegular, NSImage
        from Foundation import NSBundle

        app = NSApplication.sharedApplication()
        app.setActivationPolicy_(NSApplicationActivationPolicyRegular)

        info = NSBundle.mainBundle().infoDictionary()
        info["CFBundleName"] = "Codex Switcher"
        info["CFBundleShortVersionString"] = "0.0.2"
        info["NSHumanReadableCopyright"] = "Copyright © 2025 GitBiao. All rights reserved."

        icon_path = os.path.normpath(
            os.path.join(os.path.dirname(__file__), os.pardir, "resources", "icon_1024.png")
        )
        if os.path.exists(icon_path):
            icon = NSImage.alloc().initWithContentsOfFile_(icon_path)
            if icon:
                app.setApplicationIconImage_(icon)
    except Exception:
        pass


def run_dashboard():
    _set_dashboard_app_name()
    api = DashboardAPI()
    window = webview.create_window(
        "Codex Switcher Dashboard",
        html=HTML,
        js_api=api,
        width=700,
        height=620,
        resizable=True,
        min_size=(500, 400),
    )
    webview.start()


if __name__ == "__main__":
    run_dashboard()
