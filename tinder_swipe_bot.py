#*#*#*#*# Huy Kieu #*#*#*#*#

from selenium import webdriver
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException

from login_info import name, pwd

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        def check_exists_by_xpath(xpath):
            try:
                element = self.driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                return None
            return element

        self.driver.get('https://tinder.com')

        sleep(4)

        check_more_options = check_exists_by_xpath('//button[text()="More Options"]')
        if (check_more_options != None):
            check_more_options.click()

        sleep(2)

        fb_btn = self.driver.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(name)

        pwd_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pwd_in.send_keys(pwd)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(4)

        popup_1 = self.driver.find_element_by_css_selector('button[aria-label="Allow"]')
        popup_1.click()

        sleep(2)

        popup_2 = self.driver.find_element_by_css_selector('button[aria-label="Not interested"]')
        popup_2.click()

        sleep(30)

        self.auto_swipe()

    def like(self):
        like_btn = self.driver.find_element_by_css_selector('button[aria-label="Like"]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('button[aria-label="Nope"]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            i = randint(1, 10)
            sleep(i)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.close_tinder_plus()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//span[text()="Not interested"]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//a[text()="Keep Swiping"]')
        match_popup.click()

    def close_tinder_plus(self):
        tinder_plus_popup =  self.driver.find_element_by_xpath('//span[text()="No Thanks"]')
        tinder_plus_popup.click()
        self.driver.quit()
        exit(0)

tinder = TinderBot()
tinder.login()