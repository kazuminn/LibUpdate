# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

username = "" #username
password = "" #password

class Sel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "https://opac.lib.u-ryukyu.ac.jp/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sel(self):
        driver = self.driver
        driver.get(self.base_url + "/cgi-bin/portallogin.cgi?plang=jpn")
        driver.find_element_by_css_selector("input.button").click()
        driver.find_element_by_id("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text(u"確認する").click()
        driver.find_element_by_id("lending_line").click()
        driver.find_element_by_name("lending_line1").click()
        driver.find_element_by_name("lending_line2").click()
        driver.find_element_by_name("lending_line3").click()
        driver.find_element_by_name("lending_line4").click()
        driver.find_element_by_name("lending_line5").click()
        driver.find_element_by_name("lending_line6").click()
        driver.find_element_by_name("lending_line7").click()
        driver.find_element_by_name("lending_line8").click()
        driver.find_element_by_name("lending_line9").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
        driver.find_element_by_css_selector("input[type=\"button\"]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
