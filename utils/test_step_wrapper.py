from utils.excel_logger import ExcelLogger

logger = ExcelLogger()

def step(logger, description, func, *args, **kwargs):
    logger.add_step(description)
    try:
        result = func(*args, **kwargs)
        return result

    except Exception as e:
        screenshot_path = ""  # or: take_screenshot(driver)

        logger.mark_failed(
            message=f"{description}: {str(e)}",
            screenshot_path=screenshot_path
        )
        return None

