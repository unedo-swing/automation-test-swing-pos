import sys
import os
import time
import pytest
import traceback
from utils.excel_utils import *
from drivers.driver_set_up_ios import get_driver
from pages.book_tee_time_page import BookTeeTime
from pages.activity_page import Activity
from utils.mobile_utils import *

# Add parent directory for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

EXCEL_FILE = "dataFiles/test_data.xlsx"
SHEET_NAME = "Book Tee Time"

# Load data
test_data = read_excel_data(EXCEL_FILE, SHEET_NAME)
text_global = read_localization_data("dataFiles/COPYWRITING.xlsx", "Sheet1")

@pytest.mark.parametrize("data_row_index", [0])
def test_book_tee_time(data_row_index):
    row_num = data_row_index + 2  
    data_row = test_data[data_row_index]

    driver = get_driver()
    test_steps = []
    result = "Failed"
    message = ""

    try:
        print("template")

    except Exception as e:
        message = str(e)
        print(f"\n❌ Terjadi Kegagalan di row {row_num}: {e}")
        traceback.print_exc()
        pytest.fail(f"Test gagal karena error: {e}", pytrace=False)

    finally:
        steps_str = "\n".join(test_steps)
        write_excel_result(EXCEL_FILE, SHEET_NAME, row_num, result, steps_str, message)
        driver.quit()

