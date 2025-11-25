import pytest
import traceback
import os


def run_flow(driver, flow_method, data_row):
    tc_id = data_row.get("TC_ID", "Unknown")

    try:
        print(f"\n🚀 Running Test Case: {tc_id}")
        flow_method()

        print(f"✅ Test Case {tc_id} PASSED\n")

    except Exception as e:
        print(f"\n❌ Test Case {tc_id} FAILED!\n")

        # Save screenshot
        screenshot_path = f"screenshots/{tc_id}.png"
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(screenshot_path)
        print(f"📸 Screenshot saved: {screenshot_path}")

        traceback.print_exc()
        pytest.fail(f"Test Case {tc_id} failed: {e}")
