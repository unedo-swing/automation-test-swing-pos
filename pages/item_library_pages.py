from locators.item_library import ItemLibrary
from pages.base_pages import BasePages

class ItemLibraryPages(BasePages):
    def __init__(self, driver):
        super().__init__(driver)
        self.input_search_item                   = self.page_locator(ItemLibrary.input_item_price)
        self.button_add_an_item                  = self.page_locator(ItemLibrary.button_add_an_item)
        self.button_add_image                    = self.page_locator(ItemLibrary.button_add_image)
        self.input_item_name                     = self.page_locator(ItemLibrary.input_item_name)
        self.input_item_price                    = self.page_locator(ItemLibrary.input_item_price)
        self.button_dropdown_category            = self.page_locator(ItemLibrary.button_dropdown_category)
        self.button_avaliable                    = self.page_locator(ItemLibrary.button_avaliable)
        self.button_unavaliable                  = self.page_locator(ItemLibrary.button_unavaliable)
        self.toggle_avaliable_on_player_app      = self.page_locator(ItemLibrary.toggle_avaliable_on_player_app)
        self.button_save_item                    = self.page_locator(ItemLibrary.button_save_item)
        self.input_search_categories             = self.page_locator(ItemLibrary.input_search_categories)
        self.button_edit_item                    = self.page_locator(ItemLibrary.button_edit_item)  
        self.button_delete_item                  = self.page_locator(ItemLibrary.button_delete_item)
        self.button_x_item_information           = self.page_locator(ItemLibrary.button_x_item_information)
        self.button_update_item                  = self.page_locator(ItemLibrary.button_update_item)

    def input_search_name_item(self, data):
        self.type(self.input_search_item, data['ITEM_NAME'])
        self.press_action_keyboard()
    
    def verify_list_item(self, data):
        self.is_visible(self.page_locator(f'//XCUIElementTypeImage[contains(@name,"{data['ITEM_NAME']}")]'))
    
    def verify_name_item(self, data):
        list_items = self.get_text(self.page_locator(f'//XCUIElementTypeImage[contains(@name,"{data['ITEM_NAME']}")]')).split("\n")
        assert list_items[0] == data["ITEM_NAME"]
    
    def verify_price_item(self, data):
        list_items = self.get_text(self.page_locator(f'//XCUIElementTypeImage[contains(@name,"{data['ITEM_NAME']}")]')).split("\n")
        assert list_items[1] == data["ITEM_PRICE"]
    
    def verify_status_list_item(self, data):
        list_items = self.get_text(self.page_locator(f'//XCUIElementTypeImage[contains(@name,"{data['ITEM_NAME']}")]')).split("\n")
        assert list_items[2] == data["ITEM_STATUS"]
    
    def go_to_item(self, data):
        self.click(self.page_locator(f'//XCUIElementTypeImage[contains(@name,"{data['ITEM_NAME']}")]/following-sibling::XCUIElementTypeButton'))
    
    def verify_header_item_information(self, data):
        self.is_visible(self.page_locator(f'//XCUIElementTypeStaticText[@name="{data['ITEM_NAME']}"]'))
    
    def verify_price_item_information(self, data):
        self.is_visible(self.page_locator(f'//XCUIElementTypeStaticText[@name="{data['ITEM_PRICE']}"]'))
    
    def go_to_edit_item(self):
        self.click(self.button_edit_item)

    def delete_item(self):
        self.click(self.button_delete_item)

    def close_bottom_sheet_item_information(self):
        self.click(self.button_x_item_information)   

    def go_to_add_an_item(self):
        self.click(self.button_add_an_item)

    def upload_add_image(self):
        self.click(self.button_add_image)
        self.upload_first_image()
    
    def type_item_name(self, data):
        self.type(self.input_item_name, data["ITEM_NAME"])
    
    def type_item_price(self, data):
        self.type(self.input_item_price, data["ITEM_PRICE"])
    
    def go_to_modal_category(self):
        self.click(self.button_dropdown_category)
    
    def choose_item_availability(self, data):
        match data["ITEM_AVAILABILITY"]:
            case "AVAILABLE":
                self.click(self.button_avaliable)
            case "UNAVAILABLE":
                self.click(self.button_unavaliable)
            case _:
                print(f'Status Availablity is not recognized')
    
    def click_toogle_available_player_app(self, data):
        if(data["AVAILABLE_PLAYER_APP"] != self.get_value(self.toggle_avaliable_on_player_app)):
            self.click(self.toggle_avaliable_on_player_app)
    
    def update_item(self):
        self.click(self.button_update_item)
    
    def save_item(self):
        self.click(self.button_save_item)
