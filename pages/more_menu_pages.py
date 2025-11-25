from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.mobile_utils import *

from locators.more_menu import MoreMenu

class MoreMenuPages:
    def __init__(self, driver):
        self.driver                         = driver
        self.wait                           = WebDriverWait(driver, 10)

        self.menu_venue_management_setting  = (By.XPATH,MoreMenu.menu_venue_management_setting )
        self.menu_transaction               = (By.XPATH,MoreMenu.menu_transaction )
        self.menu_item_library              = (By.XPATH,MoreMenu.menu_item_library )
        self.menu_player_customer           = (By.XPATH,MoreMenu.menu_player_customer )
        self.menu_packages                  = (By.XPATH,MoreMenu.menu_packages )
        self.menu_balance                   = (By.XPATH,MoreMenu.menu_balance )
        self.menu_reports                   = (By.XPATH,MoreMenu.menu_reports )
        self.menu_rating_reviews            = (By.XPATH,MoreMenu.menu_rating_reviews )
        self.menu_team_role_access          = (By.XPATH,MoreMenu.menu_team_role_access )
        self.menu_contact_swing_support     = (By.XPATH,MoreMenu.menu_contact_swing_support )
        self.menu_delete_my_account         = (By.XPATH,MoreMenu.menu_delete_my_account )
        self.menu_terms_condition           = (By.XPATH,MoreMenu.menu_terms_condition )
        self.menu_privacy_policy            = (By.XPATH,MoreMenu.menu_privacy_policy )
        self.menu_logout                    = (By.XPATH,MoreMenu.menu_logout )

        #venue management & settings
        self.menu_venu_information               = (By.XPATH, MoreMenu.menu_venu_information)
        self.menu_courts_pricing                 = (By.XPATH, MoreMenu.menu_courts_pricing)
        self.menu_cancellation_policies          = (By.XPATH, MoreMenu.menu_cancellation_policies)
        self.menu_venue_terms_condition          = (By.XPATH, MoreMenu.menu_venue_terms_condition)
        self.button_x_venue_management_settings  = (By.XPATH, MoreMenu.button_x_venue_management_settings)

        self.menus = {
            "venue_management":     (By.XPATH, MoreMenu.menu_venue_management_setting),
            "transaction":          (By.XPATH, MoreMenu.menu_transaction),
            "item_library":         (By.XPATH, MoreMenu.menu_item_library),
            "player_customer":      (By.XPATH, MoreMenu.menu_player_customer),
            "packages":             (By.XPATH, MoreMenu.menu_packages),
            "balance":              (By.XPATH, MoreMenu.menu_balance),
            "reports":              (By.XPATH, MoreMenu.menu_reports),
            "rating_reviews":       (By.XPATH, MoreMenu.menu_rating_reviews),
            "team_role_access":     (By.XPATH, MoreMenu.menu_team_role_access),
            "contact_support":      (By.XPATH, MoreMenu.menu_contact_swing_support),
            "delete_my_account":    (By.XPATH, MoreMenu.menu_delete_my_account),
            "terms_condition":      (By.XPATH, MoreMenu.menu_terms_condition),
            "privacy_policy":       (By.XPATH, MoreMenu.menu_privacy_policy),
            "logout":               (By.XPATH, MoreMenu.menu_logout),
        }
        # self.menu_venue_management  = (By.XPATH,MoreMenu. )

    
    def open_venue_management_setting(self):
        click_element(self.driver, self.menu_venue_management_setting)

    def open_transaction(self):
        click_element(self.driver, self.menu_transaction)

    def open_item_library(self):
        click_element(self.driver, self.menu_item_library)

    def open_player_customer(self):
        click_element(self.driver, self.menu_player_customer)

    def open_packages(self):
        click_element(self.driver, self.menu_packages)

    def open_balance(self):
        click_element(self.driver, self.menu_balance)

    def open_reports(self):
        click_element(self.driver, self.menu_reports)

    def open_rating_reviews(self):
        click_element(self.driver, self.menu_rating_reviews)

    def open_team_role_access(self):
        click_element(self.driver, self.menu_team_role_access)

    def open_contact_swing_support(self):
        click_element(self.driver, self.menu_contact_swing_support)

    def open_delete_my_account(self):
        click_element(self.driver, self.menu_delete_my_account)

    def open_terms_condition(self):
        click_element(self.driver, self.menu_terms_condition)

    def open_privacy_policy(self):
        click_element(self.driver, self.menu_privacy_policy)

    def open_logout(self):
        click_element(self.driver, self.menu_logout)

    def verify_username(self, data):
        is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeStaticText[@name="{data['USERNAME']}"]'))
    
    def verify_roles(self, data):
        is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeStaticText[@name="{data['ROLES']}"]'))
    
    def verify_card_venue(self, data):
        is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeImage[contains(@name,"{data['VENUE_NAME']}"]'))
    
    def verify_label_section(self):
        list_label = ["Support", "Legal"]
        for label in list_label:
            is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeStaticText[@name="{label}"]'))
    
    def verify_label_version(self, data):
        is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeStaticText[@name="{data['VERSION_APPS']}"]'))

    def verify_menu_visible(self):
        failed = []
        for key, locator in self.menus.items():
            try:
                is_element_visible(self.driver, locator)
                print(f"✅ {key} is visible")
            except Exception as e:
                print(f"❌ {key} NOT visible → {e}")
                failed.append(key)

        if failed:
            raise AssertionError(f"❌ These menus are missing: {failed}")

        print("🎉 All menus are visible!")
        locator = self.menus[key]
        return is_element_visible(self.driver, locator)
    
    def open_venue_information(self):
        click_element(self.driver, self.menu_venu_information)
    
    def open_courts_pricing(self):
        click_element(self.driver,self.menu_courts_pricing)

    def open_cancellation_policied(self):
        click_element(self.driver, self.menu_cancellation_policies)
    
    def open_venue_terms_conditions(self):
        click_element(self.driver, self.menu_venue_terms_condition)
    
    def close_modal_venue_management_settings(self):
        click_element(self.driver, self.button_x_venue_management_settings)
    
    def verify_header_venue_management_settings(self, header):
        is_element_visible(self.driver, (By.XPATH, f'//XCUIElementTypeStaticText[@name="{header}"]'))
    
    def verify_menu_management_settings(self):
        list_menu = [self.menu_venu_information, self.menu_courts_pricing, self.menu_cancellation_policies, self.menu_venue_terms_condition, self.button_x_venue_management_settings]

        for menu in list_menu:
            is_element_visible(self.driver, menu)

    

    
