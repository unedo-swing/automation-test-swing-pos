from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators.venue_information import VenueInformation
from pages.base_pages import BasePages



class VenueInformationPages(BasePages):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.button_change_logo                 = (By.XPATH, VenueInformation.button_change_logo)
        self.input_venue_name                   = (By.XPATH, VenueInformation.input_venue_name)
        self.text_area_about_venue              = (By.XPATH, VenueInformation.text_area_about_venue)
        self.button_edit_venue_location         = (By.XPATH, VenueInformation.button_edit_venue_location)
        self.image_venue                        = (By.XPATH, VenueInformation.image_venue)
        self.button_x_venue_image               = (By.XPATH, VenueInformation.button_x_venue_image)
        self.icon_maps_location                 = (By.XPATH, VenueInformation.icon_maps_location)
        self.button_save_venue_information      = (By.XPATH, VenueInformation.button_save_venue_information)
        self.icon_image                         = (By.XPATH, VenueInformation.icon_image)



    def click_change_logo(self):
        self.click(self.button_change_logo)

    def set_venue_name(self, data):
        self.type(self.input_venue_name, data["VENUE_NAME"])

    def set_about_venue(self, data):
        self.type(self.text_area_about_venue, data["VENUE_ABOUT"])

    def click_edit_venue_location(self):
        self.click(self.button_edit_venue_location)

    def delete_venue_image(self):
        self.click(self.button_x_venue_image)

    def click_save_information(self):
        self.click(self.button_save_venue_information)

    # ===== VERIFICATIONS =====

    def verify_page_loaded(self, data):
        self.is_visible((By.XPATH, f'//XCUIElementTypeOther[@name="{data['HEADER_VENUE_INFORMATION']}"]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeOther[@name="{data['HEADER_VENUE_INFORMATION']}"]/preceding-sibling::XCUIElementTypeButton[1]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Basic information"]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Show the players what your venue is all about."]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Recommended logo 128px x 128px"]'))
        self.is_visible(self.icon_image)
        self.is_visible(self.button_change_logo)
        self.is_visible(self.input_venue_name)
        self.is_visible(self.text_area_about_venue)
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Basic information"]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Basic information"]'))
        self.is_visible((By.XPATH, f'//XCUIElementTypeStaticText[@name="Basic information"]'))
        
        self.is_visible(self.button_edit_venue_location)

    def verify_venue_images_visible(self):
        self.is_visible(self.image_venue)

    def verify_location_map_visible(self):
        self.is_visible(self.icon_maps_location)
