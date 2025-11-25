import os
import sys
import pytest
from utils.env_utils import get_env

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from drivers.driver_set_up_ios import get_driver
from utils.excel_utils import read_excel_data, read_localization_data


EXCEL_FILE = "DataFiles/test_data.xlsx"
COPYWRITING_FILE = "DataFiles/COPYWRITING.xlsx"

# Load once for all tests
@pytest.fixture(scope="session")
def test_data_item_library():
    return read_excel_data(EXCEL_FILE, "Item Library")


# Load once for all tests
@pytest.fixture(scope="session")
def test_data():
    return read_excel_data(EXCEL_FILE, "Book Tee Time")


@pytest.fixture(scope="session")
def text_global():
    return read_localization_data(COPYWRITING_FILE, "Sheet1")


# Driver fixture (open app before test, close after)
@pytest.fixture
def driver(request):
    driver_instance = get_driver()
    print("🟢 iOS App Started.")

    yield driver_instance

    # ===== TEARDOWN SECTION =====
    bundle_id = get_env("IOS_BUNDLE_ID")

    try:
        print(f"🔴 Terminating iOS app → {bundle_id}")
        # driver_instance.terminate_app(bundle_id)
    except Exception as e:
        print("⚠️ Failed to terminate app:", e)

    try:
        driver_instance.quit()
        print("🟡 Driver quit OK")
    except Exception:
        pass


@pytest.fixture
def open_and_close_app(driver):
    bundle_id = get_env("IOS_BUNDLE_ID")
    
    # ===== BEFORE EACH TEST =====
    print("🟢 Launching iOS App...")
    driver.activate_app(bundle_id)     # paling stabil untuk iOS

    yield

    # ===== AFTER EACH TEST =====
    print("🔴 Terminating iOS App...")
    try:
        print("🔴 Terminating iOS App...")
        # driver.terminate_app(bundle_id)
    except Exception as e:
        print("⚠️ Failed to terminate app:", e)
