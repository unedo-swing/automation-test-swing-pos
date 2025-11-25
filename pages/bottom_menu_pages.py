from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from locators.bottom_menu import BottomMenu
from utils.mobile_utils import *


class BottomMenuPage:
    def __init__(self, driver):
        self.driver             = driver
        self.wait               = WebDriverWait(driver, 10)

        self.menu_slots         = (By.XPATH, BottomMenu.menu_slots)         
        self.menu_items         = (By.XPATH, BottomMenu.menu_items)
        self.menu_bills         = (By.XPATH, BottomMenu.menu_bills)
        self.menu_bookings      = (By.XPATH, BottomMenu.menu_bookings)
        self.menu_more          = (By.XPATH, BottomMenu.menu_more)

    
    def open_menu_slots(self):
        click_element(self.driver,self.menu_slots)
    
    def open_menu_items(self):
        click_element(self.driver,self.menu_items)
    
    def open_menu_bills(self):
        click_element(self.driver,self.menu_bills)
    
    def open_menu_bookings(self):
        click_element(self.driver,self.menu_bookings)

    def open_menu_more(self):
        click_element(self.driver,self.menu_more)