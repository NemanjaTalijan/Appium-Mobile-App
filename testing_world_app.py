# https://www.youtube.com/watch?v=ajBrRkEPQc4
# https://www.youtube.com/watch?v=LPVhy6cJR5M
# in order to install app on VMD you need to specify system path to SDK
# set for session PATH=%PATH%;C:\Users\username\AppData\Local\Android\Sdk\platform-tools OR for permanent path set
# setx PATH=%PATH%;C:\Users\username\AppData\Local\Android\Sdk\platform-tools
# You need to check which VMD is currently running by executing following command,
#  but first go to specified sdk platform-tools path
# adb.exe devices
#     Output:
#              List of devices attached
#              emulator-5554   device
# now navigate to file where the app is located and run command:
# adb install TheTestingWorld.apk
# the app is installed now on your device
# Log by command:
#      adb logcat
# Caps used:
# {
#   "platformName": "Android",
#   "platformVersion": "8.0",
#   "deviceName": "Nexus_5X_8.0",
#   "automationName": "Appium",
#   "app": "C:\\Users\\ntalijan\\Desktop\\apps\\python\\TheTestingWorld.apk"
# }
#
# Create HTML report:
#      Download HTMLTestRunner.py
#      Run test by command:
#           python android_complex.py > result.html, this will create HTML report

import os
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
from device_time_parse import *
from appium import webdriver
import HTMLTestRunner

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):

        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '8.0',
            'deviceName': 'Android Emulator',
            'app': PATH(
                        'TheTestingWorld.apk'
                   )
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        register_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/register'))
        )
        register_button.click()
        name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/name'))
        )
        name_field.send_keys("Pera")
        assert name_field.text == 'Pera', "Name " + name_field.text + " set!"  # "Name %s set!" % name_field.text
        name_field_value = name_field.text
        last_name_field = self.driver.find_element_by_id("com.example.work.thetestingworld:id/last_name")
        last_name_field.send_keys("Peric")
        assert last_name_field.text == 'Peric', "Last name %s set!" % last_name_field.text
        employee_check_box = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Employee")')
        employee_check_box.click()
        date_of_birth = self.driver.find_element_by_id('com.example.work.thetestingworld:id/dob')
        date_of_birth.click()
        date_of_birth_year = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'android:id/date_picker_header_year'))
        )
        date_of_birth_year.click()
        for x in range(0, 4):
            self.driver.swipe(540, 550, 540, 1380, 1000)
        year_select = self.driver.find_element_by_android_uiautomator('new UiSelector().text("1988")')
        year_select.click()

        time = self.driver.device_time
        time_parsed = device_time_parse(time)
        month_num = month_string_to_num(time_parsed[1])
        count_direction = month_select_direction_click_count(month_num)
        prev_or_next_month_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, '{}'.format(prev_or_next_month(count_direction))))
        )
        for x in range(0, count_direction[0]):
            prev_or_next_month_select.click()
        sleep(1)
        birth_day = self.driver.find_element_by_android_uiautomator('new UiSelector().text("30")')
        birth_day.click()
        save_birth_data = self.driver.find_element_by_android_uiautomator('new UiSelector().text("OK")')
        save_birth_data.click()
        assert date_of_birth.text == '7-30-1988 ', "DOB set!"
        date_of_birth_value = date_of_birth.text
        specification_toggle_on_off = self.driver.find_element_by_id('com.example.work.thetestingworld:id/toggleOnOff')
        specification_toggle_on_off.click()
        assert self.driver.find_element_by_id('com.example.work.thetestingworld:id/specification').text == 'Testing', "Specification on testing set! "
        specification_value = self.driver.find_element_by_id('com.example.work.thetestingworld:id/specification').text
        self.driver.back()
        county = self.driver.find_element_by_id('com.example.work.thetestingworld:id/country')
        county.click()
        select_country = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/country_list'))
        )
        select_country.click()
        select_country_pick_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/titledialog'))
        )
        county_us = self.driver.find_element_by_android_uiautomator('new UiSelector().text("US")')
        county_us.click()
        assert county.text == 'US', "Country set!"
        county_value = county.text
        email = self.driver.find_element_by_id('com.example.work.thetestingworld:id/email')
        email.send_keys('user@mail.com')
        assert email.text == 'user@mail.com', "Email address set!"
        email_value = email.text
        self.driver.back()
        phone = self.driver.find_element_by_id('com.example.work.thetestingworld:id/mobile')
        phone.send_keys('3816612345')
        assert phone.text == '3816612345', "Phone set!"
        phone_value = phone.text
        self.driver.back()
        send_content_check_box = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Send Job '
                                                                                 'Notification")')
        send_content_check_box.click()
        self.driver.swipe(300, 1170, 300, 770, 1000)
        gender = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Male")')
        gender.click()
        submit_button = self.driver.find_element_by_id('com.example.work.thetestingworld:id/submit')
        submit_button.click()
        # result page asserts
        name_field_saved = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/name'))
        )
        thanks_for_submiting_page = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Thanks '
                                                                                    'for submiting")')
        assert thanks_for_submiting_page, "User is on the submit page"
        assert name_field_saved.text == name_field_value, "Name saved!"
        date_of_birth_saved = self.driver.find_element_by_id('com.example.work.thetestingworld:id/dob')
        assert date_of_birth_saved.text == date_of_birth_value, "DOB saved!"
        email_saved = self.driver.find_element_by_id('com.example.work.thetestingworld:id/email')
        assert email_saved.text == email_value, "Email saved!"
        country_saved = self.driver.find_element_by_id('com.example.work.thetestingworld:id/country')
        assert country_saved.text == county_value, "Country saved!"
        mobile_saved = self.driver.find_element_by_id('com.example.work.thetestingworld:id/mobile1')
        assert mobile_saved.text == phone_value, "Phone saved!"
        specification_saved = self.driver.find_element_by_id('com.example.work.thetestingworld:id/specification')
        assert specification_saved.text == specification_value, "Specification saves!"

    def test_welcome(self):
        WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'com.example.work.thetestingworld:id/register'))
                )
        title_welcome = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Welcome To Testing '
                                                                        'world")')
        self.assertIsNotNone(title_welcome)


if __name__ == '__main__':
    HTMLTestRunner.main()
