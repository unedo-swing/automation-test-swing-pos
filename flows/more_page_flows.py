import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pages.bottom_menu_pages import BottomMenuPage
from utils.excel_logger import ExcelLogger
from utils.test_step_wrapper import step
from utils.screenshot_utils import *

class MorePageFlow:
    def __init__(self, driver):
        self.driver = driver
        self.bottom_menu = BottomMenuPage(driver)
        self.logger = ExcelLogger()

    def template(self, data_row, text_global):
        try:
            steps = [
                ("Test-step", "function", "parameter function")  ## just example
                # Step - step put in here
            ]

            for description, func, arg in steps:
                if arg is not None:
                    step(self.logger, description, func, arg)
                else:
                    step(self.logger, description, func)

        except Exception as e:
            screenshot_path = take_screenshot(self.driver)
            self.logger.mark_failed(str(e), screenshot_path)
            self.logger.save("")
            raise e

        self.logger.save("")

    def as_a_user_verify_more_pages(self, data_row, text_global):
        try:
            steps = [
                ("Click More Page", self.bottom_menu.open_menu_more, None),

            ]

            for description, func, arg in steps:
                if arg is not None:
                    step(self.logger, description, func, arg)
                else:
                    step(self.logger, description, func)

        except Exception as e:
            # screenshot_path = take_screenshot(self.driver)
            # self.logger.mark_failed(str(e), screenshot_path)
            # self.logger.save("")
            raise e

        # self.logger.save("")    

