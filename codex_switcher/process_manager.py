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

"""Manage the Codex Desktop process lifecycle (kill & relaunch)."""

import subprocess
import time

CODEX_APP_PATH = "/Applications/Codex.app"
CODEX_PROCESS_NAME = "Codex"
RESTART_DELAY_SECONDS = 1.5


def is_codex_running() -> bool:
    result = subprocess.run(
        ["pgrep", "-x", CODEX_PROCESS_NAME],
        capture_output=True,
    )
    return result.returncode == 0


def kill_codex() -> bool:
    """Kill all Codex processes. Returns True if at least one was running."""
    was_running = is_codex_running()
    subprocess.run(["killall", CODEX_PROCESS_NAME], capture_output=True)
    return was_running


def launch_codex() -> None:
    subprocess.Popen(["open", CODEX_APP_PATH])


def restart_codex() -> None:
    """Kill Codex Desktop, wait for cleanup, then relaunch."""
    kill_codex()
    time.sleep(RESTART_DELAY_SECONDS)
    launch_codex()
