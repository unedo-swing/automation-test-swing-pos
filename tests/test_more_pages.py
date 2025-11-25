import pytest
from pages.bottom_menu_pages import BottomMenuPage
from pages.more_menu_pages import MoreMenuPages


@pytest.mark.usefixtures("open_and_close_app")
class TestMorePages:
    @pytest.fixture(autouse=True)
    def setup_pages(self, driver):
        self.driver         = driver
        self.bottom_menu    = BottomMenuPage(driver)
        self.more_menu      = MoreMenuPages(driver)   
        self.data = {
                "USERNAME"      : "Alvin Lianto",
                "ROLES"         : "Admin",
                "VENUE_NAME"    : "Go Padel BSD",
                "VERSION_APPS"  : "VERSION 0.0.7.20251123 (1763902409)"
            }

    @pytest.mark.current_running
    def test_verify_more_pages(self):
        self.bottom_menu.open_menu_more()
        self.more_menu.verify_menu_visible()
        self.more_menu.verify_username(self.data)
        self.more_menu.verify_roles(self.data)
        self.more_menu.verify_label_version(self.data)
        self.more_menu.verify_label_section()
        
        # assertion kalau perlu
    @pytest.mark.current_running
    def test_click_menu_venue_management_settings(self):
        self.bottom_menu.open_menu_more()
        self.more_menu.open_venue_management_setting()
        self.more_menu.verify_header_venue_management_settings("Venue management & settings")
        self.more_menu.verify_menu_management_settings()
