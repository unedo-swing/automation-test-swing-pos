from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy
import re
import pytest

def tap_coordinates(driver, x, y):
    """
    Tap on a specific screen coordinate in a native iOS app.

    Args:
        driver: Appium WebDriver instance
        x (int|float): X coordinate
        y (int|float): Y coordinate
    """
    try:
        # Attempt to tap using mobile: tap (preferred for iOS)
        driver.execute_script('mobile: tap', {'x': x, 'y': y})
        print(f"Tapped on coordinates ({x}, {y}) using mobile: tap")
    except Exception as e:
        print(f"[WARN] Could not tap using mobile: tap. Trying TouchAction fallback... Error: {e}")
        try:
            # Fallback using TouchAction
            action = ActionBuilder(driver)
            action.tap(None, x, y).perform()
            print(f"Tapped on coordinates ({x}, {y}) using TouchAction fallback")
        except Exception as err:
            print(f"[ERROR] Could not tap on coordinates ({x}, {y}): {err}")


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def get_text_element(driver, locator, timeout=10):
    time.sleep(2)
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    text_element = element.get_attribute("name")##element.text()
    return text_element

def get_value_element(driver, locator, timeout=10):
    time.sleep(1)
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    text_element = element.get_attribute("value")##element.text()
    return text_element

def click_element(driver, locator, timeout=10):
    # locator = '//XCUIElementTypeImage[@name="AUTOMATION3"]'
    scroll_to_element(driver, locator)
    print(f'{locator}')
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()
    return element

def input_text(driver, locator, text, timeout=10):
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.clear()
    element.send_keys(text)
    return element

def is_element_visible(driver, locator, timeout=10):
    scroll_to_element(driver, locator, 5)
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except Exception:
        pytest.fail(f"❌ Element not visible: {locator}")

def is_element_visible_skiprate(driver, locator, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return True
    except Exception:
        return False
    
def is_element_enabled(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element.is_enabled()
    except:
        return False
    
def is_element_disabled(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return not element.is_enabled()
    except:
        return False


def press_keyboard_action(driver, action="return"):
    try:
        driver.execute_script('mobile: performEditorAction', {'action': action})
        print(f"Pressed iOS keyboard key: {action}")
    except Exception as e:
        print(f"[WARN] Could not perform editor action '{action}'. Trying fallback...")
        # Fallback to Keys.RETURN
        try:
            driver.switch_to.active_element.send_keys(Keys.RETURN)
            print("Pressed RETURN key as fallback.")
        except Exception as err:
            print(f"[ERROR] Could not send RETURN key: {err}")


def scroll_to_element_and_click(driver, locator, max_scrolls=5, direction="up"):
    platform = driver.capabilities.get("platformName", "").lower()

    for i in range(max_scrolls):
        try:
            # Check if element is visible
            element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))
            print(f"✅ Element visible after {i} scroll(s). Clicking it now.")
            time.sleep(3)
            element.click()
            return True

        except Exception:
            print(f"🔍 Scrolling {direction}... (attempt {i + 1}/{max_scrolls})")

            if platform == "ios":
                _ios_scroll(driver, direction)
            else:
                # Placeholder for Android scroll
                # _android_scroll(driver, direction)
                pass

    raise NoSuchElementException(f"❌ Element not found after {max_scrolls} scrolls: {locator}")

def scroll_to_element(driver, locator, max_scrolls=6):
    platform = driver.capabilities.get("platformName", "").lower()
    print(f"XPath: {locator}")

    scroll_up_first = True  # prioritaskan scroll ke atas dulu

    for i in range(max_scrolls):

        # 1️⃣ Cek apakah element sudah visible di layar
        try:
            element = WebDriverWait(driver, 2).until(
                EC.visibility_of_element_located(locator)
            )
            print(f"✅ Element is visible after {i} scroll(s)")
            return True

        except Exception:
            pass

        # 2️⃣ Tentukan arah scroll
        if scroll_up_first:
            direction = "up"
        else:
            direction = "down"

        print(f"🔍 Scrolling {direction}... (attempt {i+1}/{max_scrolls})")

        if platform == "ios":
            _ios_scroll(driver, direction)

        # Setelah 2 scroll ke atas, ganti scroll ke bawah
        if i == 1:
            scroll_up_first = False

    raise NoSuchElementException(f"❌ Element not found after {max_scrolls} scrolls: {locator}")




def _ios_scroll(driver, direction="down"):
    size = driver.get_window_size()
    width = size['width']
    height = size['height']

    # Define swipe start/end coordinates based on direction
    if direction == "down":
        start_x = width / 2
        start_y = height * 0.3
        end_x = width / 2
        end_y = height * 0.7
    elif direction == "up":
        start_x = width / 2
        start_y = height * 0.7
        end_x = width / 2
        end_y = height * 0.3
    elif direction == "left":
        start_x = width * 0.8
        start_y = height / 2
        end_x = width * 0.2
        end_y = height / 2
    else:  # right
        start_x = width * 0.2
        start_y = height / 2
        end_x = width * 0.8
        end_y = height / 2

    try:
        driver.execute_script("mobile: swipe", {
            "direction": direction,
            "fromX": int(start_x),
            "fromY": int(start_y),
            "toX": int(end_x),
            "toY": int(end_y),
            "velocity": 1000
        })
        print(f"📱 iOS swiped {direction}")
    except Exception as e:
        print(f"[WARN] iOS swipe failed: {e}")

def get_list_card_venue(driver):
    predicate = 'type == "XCUIElementTypeImage" AND name CONTAINS "from your location"'
    elements = driver.find_elements(AppiumBy.IOS_PREDICATE, predicate)
    list_location = []

    for i, el in enumerate(elements):
        name = el.get_attribute('name')
        if not name:
            continue
            
        lines = name.split("\n")
        if len(lines) < 2:
            continue
            
        location = lines[0]

        match = re.search(r'(\d+)', lines[-1])
        distance = int(match.group(1)) if match else None

        list_location.append({
            "name": location,
            "distance": distance
        })

    # Extract distances
    distances = [loc['distance'] for loc in list_location]

    # Assert ascending order
    assert distances == sorted(distances), f"Distances are not sorted"

    return list_location




def select_first_photo(driver):
    locator = (By.XPATH, '//XCUIElementTypeImage[@name="PXGGridLayout-Info"][1]')
    element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator))
    element.click()

    


