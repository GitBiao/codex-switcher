.PHONY: app clean run deps

# Build macOS .app bundle (output: dist/Codex Switcher.app)
app: deps
	python3 setup.py py2app
	@echo "\n✅  Built: dist/Codex Switcher.app"

# Install Python dependencies
deps:
	pip3 install -r requirements.txt
	pip3 install py2app

# Run from source (development)
run:
	python3 -m codex_switcher.app

# Remove build artifacts
clean:
	rm -rf build dist .eggs *.egg-info
