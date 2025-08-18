import allure
import json
import pytest
import subprocess
import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Global process handles
emulator_process = None
appium_process = None


def start_emulator():
    global emulator_process
    emulator_path = r"C:\Users\nmaheshw\AppData\Local\Android\Sdk\emulator\emulator.exe"
    avd_name = "Pixel5"
    emulator_process = subprocess.Popen([emulator_path, "-avd", avd_name])
    print(f"Starting emulator: {avd_name}", flush=True)
    time.sleep(30)


def stop_emulator():
    print("Stopping emulator...", flush=True)
    subprocess.call(["adb", "emu", "kill"])


def start_appium_server():
    global appium_process
    appium_path = r"C:\Users\nmaheshw\AppData\Roaming\npm\appium.cmd"
    appium_process = subprocess.Popen([appium_path, "--base-path", "/wd/hub"])
    print("Starting Appium server...", flush=True)
    time.sleep(10)


def stop_appium_server():
    print("Stopping Appium server...", flush=True)
    if appium_process:
        appium_process.terminate()
        appium_process.wait()


@pytest.fixture(scope="class")
def driver(request):
    start_emulator()
    start_appium_server()

    with open("config/capabilities.json") as f:
        caps = json.load(f)

    options = UiAutomator2Options()
    for key, value in caps.items():
        setattr(options, key, value)

    options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    options.app_wait_activity = "com.saucelabs.mydemoapp.android.view.activities.*"

    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    request.cls.driver = driver
    yield
    driver.quit()
    stop_appium_server()
    stop_emulator()


# Hook to capture screenshot on test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            screenshot_dir = os.path.join("allure-results","screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved to {screenshot_path}")

            allure.attach.file(screenshot_path,name="Screenshot on failure", attachment_type=allure.attachment_type.PNG)
