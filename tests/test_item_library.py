import pytest
from pages.bottom_menu_pages import BottomMenuPage
from pages.more_menu_pages import MoreMenuPages
from pages.item_library_pages import ItemLibraryPages

@pytest.mark.usefixtures("open_and_close_app")
class TestItemLibrary:
    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.driver         = driver
        self.bottom_menu    = BottomMenuPage(driver)
        self.more_menu      = MoreMenuPages(driver)  
        self.item_library   = ItemLibraryPages(driver)

    @pytest.mark.item_library
    @pytest.mark.parametrize("data_row_index", [0])
    def test_add_an_item_library(self, test_data_item_library, data_row_index):
        data_row = test_data_item_library[data_row_index]
        # self.bottom_menu.open_menu_more()
        # self.more_menu.open_item_library()
        # self.item_library.go_to_add_an_item()
        self.item_library.upload_add_image()
        self.item_library.type_item_name(data_row)
        self.item_library.type_item_price(data_row)
        self.item_library.choose_item_availability(data_row)
        self.item_library.click_toogle_available_player_app(data_row)
        self.item_library.save_item()

