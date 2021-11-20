from selenium import webdriver, common
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time
import os

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))


class Greenhouse:
    def __init__(self, url, title, location, company) -> None:
        self.url = url
        self.title = title
        self.location = location
        self.company = company
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def open_window(self):
        self.driver.get(self.url)

    def apply(self, data, resume_route, cover_letter_route):
        # self.driver.find_element_by_xpath('//*[@id="apply-button"]').click()
        time.sleep(2)
        self.driver.find_element_by_id(
            'first_name').send_keys(data['first_name'])
        self.driver.find_element_by_id(
            'last_name').send_keys(data['last_name'])
        self.driver.find_element_by_id('email').send_keys(data['email'])
        self.driver.find_element_by_id('phone').send_keys(data['phone'])

        try:
            loc = self.driver.find_element_by_id('job_application_location')
            loc.send_keys(data['location'])
            loc.send_keys(common.keys.Keys.DOWN)  # manipulate a dropdown menu
            loc.send_keys(common.keys.Keys.DOWN)
            loc.send_keys(common.keys.Keys.RETURN)

        except common.exceptions.NoSuchElementException:
            pass

        # add linkedin

        try:
            self.driver.find_element_by_xpath(
                '//input[@name="job_application[answers_attributes][0][text_value]"]').send_keys(data['linkedin'])
        except common.exceptions.NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'LinkedIn')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add graduation year
        try:
            self.driver.find_element_by_xpath(
                "//select/option[text()='2021']").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add university
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'Harvard')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add degree
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'Bachelor')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add major
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'Computer Engineering')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add how did you hear about this job?
        try:
            self.driver.find_element_by_xpath(
                "//label[contains(.,'How did you hear about this job?')]").send_keys("Glass Door")
        except common.exceptions.NoSuchElementException:
            pass

        # add website
        try:
            self.driver.find_element_by_xpath(
                "//label[contains(.,'Website')]").send_keys(data['website'])
        except common.exceptions.NoSuchElementException:
            pass

        # add work authorization
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'any employer')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add Gender
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'Male')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add Race
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'White')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add disability
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="job_application_disability_status"]/option[3]').click()
        except common.exceptions.NoSuchElementException:
            pass
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'I don't have a disability')]").click()
        except common.exceptions.NoSuchElementException:
            pass

        # add Veteran Status
        try:
            self.driver.find_element_by_xpath(
                "//select/option[contains(.,'I am not a protected veteran')]").click()
        except common.exceptions.NoSuchElementException:
            pass
        cover_letter = self.driver.find_element_by_id(
            "s3_upload_for_cover_letter").find_element_by_xpath('//*[@type="file"]')
        cover_letter.send_keys(
            os.path.join(__location__, cover_letter_route))
        time.sleep(3)
        resume = self.driver.find_element_by_id(
            "s3_upload_for_resume").find_element_by_xpath('//*[@type="file"]')
        resume.send_keys(
            os.path.join(__location__, resume_route))
        self.driver.find_element_by_id("submit_app").click()
