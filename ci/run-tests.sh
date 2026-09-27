#!/usr/bin/env bash
# Lancé par android-emulator-runner une fois l'émulateur démarré.
set -euo pipefail

adb wait-for-device
adb install -r mda.apk

adb shell wm size
adb shell wm density

pytest tests/ -v --alluredir=allure-results
