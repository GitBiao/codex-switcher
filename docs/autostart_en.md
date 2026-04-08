# Auto-start on Login

Use a macOS LaunchAgent to start Codex Switcher automatically at login.

## Create the plist File

Save the following to `~/Library/LaunchAgents/com.codex-switcher.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.codex-switcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>-m</string>
        <string>codex_switcher.app</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/codex-switcher</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
```

> **Note**: Replace `WorkingDirectory` with the actual project path, and update the Python path in `ProgramArguments` with the output of `which python3`.

## Load the Service

```bash
launchctl load ~/Library/LaunchAgents/com.codex-switcher.plist
```

## Unload the Service

```bash
launchctl unload ~/Library/LaunchAgents/com.codex-switcher.plist
```

## Check Status

```bash
launchctl list | grep codex-switcher
```

## View Logs

For debugging, add log output paths to the plist:

```xml
<key>StandardOutPath</key>
<string>/tmp/codex-switcher.stdout.log</string>
<key>StandardErrorPath</key>
<string>/tmp/codex-switcher.stderr.log</string>
```
