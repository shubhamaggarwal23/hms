from random import randrange
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from typing import Self
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def wait(cls):
    def _wait(func):
        def wrapper(instance:Self,locator,**kwargs):
            w = WebDriverWait(instance.driver,10)
            v = visibility_of_element_located(locator)
            w.until(v)
            return func(instance,locator,**kwargs)
        return wrapper
    for key, value in cls.__dict__.items():
        if callable(value):
            if key not in ("__init__", "pagedown", "takescreenshot","alert_text","get_text"):
                setattr(cls,key,_wait(value))
    return cls

@wait
class SeleniumWrapper:

    def __init__(self,driver):
        self.driver = driver


    def enter_text(self,locator:tuple[str,str],value:str):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def click_element(self,locator:tuple[str,str]):
        sleep(3)
        self.driver.find_element(*locator).click()


    def select_element(self,locator,item):
        ele = self.driver.find_element(*locator)
        s = Select(ele)
        s.select_by_visible_text(item)


    def mouse_hover(self,locator):
        action = ActionChains(self.driver)
        ele = self.driver.find_element(*locator)
        action.move_to_element(ele).perform()

    def takescreenshot(self):
        self.driver.save_screenshot(f"./screenshots/ss{randrange(1,2000)}.png")

    def pagedown(self):
        action = ActionChains(self.driver)
        for _ in range(30):
            action.send_keys(Keys.PAGE_DOWN).perform()


    def alert_text(self):
        _text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        return _text


    def get_text(self,locator):
        return self.driver.find_element(*locator).text