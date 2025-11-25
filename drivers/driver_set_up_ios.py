from appium import webdriver
from appium.options.common import AppiumOptions
from utils.env_utils import get_env

def get_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": get_env("IOS_PLATFORM_NAME", "iOS"),
        "appium:platformVersion": get_env("IOS_PLATFORM_VERSION"),
        "appium:deviceName": get_env("IOS_DEVICE_NAME"),
        "appium:udid": get_env("IOS_UDID"),
        "appium:automationName": get_env("IOS_AUTOMATION_NAME", "XCUITest"),
        "appium:bundleId": get_env("IOS_BUNDLE_ID"),
        "appium:noReset": get_env("IOS_NO_RESET", "True") == "True",
        "appium:useNewWDA": get_env("IOS_USE_NEW_WDA", "False") == "True",
        "appium:newCommandTimeout": int(get_env("IOS_NEW_COMMAND_TIMEOUT", "3600")),
        "appium:showXcodeLog": True,
    })

    return webdriver.Remote("http://localhost:4723", options=options)
