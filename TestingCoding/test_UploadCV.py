from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os  # to get the resume file
import time  # to sleep

__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))

# sample application links if we don't want to run get_links.py
URL_l2 = 'https://boards.greenhouse.io/doordash/jobs/3393928?gh_jid=3393928&rx_c=corp---canada&rx_campaign=indeed144&rx_group=129152&rx_job=3393928&rx_r=none&rx_source=Indeed&rx_ts=20211120T140008Z&rx_p=FGY5TRVQOV&rx_viewer=704eae0e2d0a11ec85ec9fccc13cdfd51924a10d0f42408aa10bf7cd9b4a6e67'
URL_l3 = 'https://boards.greenhouse.io/asana/jobs/2344893'
URL_l4 = 'https://boards.greenhouse.io/asana/jobs/3644497'
URL_l6 = 'https://boards.greenhouse.io/asana/jobs/3644690'
URL_l8 = 'https://jobs.lever.co/bolt/46e30240-63fb-4e10-af10-dad7e355c635'
URL_l9 = 'https://jobs.lever.co/bolt/e73884bc-f2c1-4069-b496-2b9564390520'
URL_g1 = 'https://jobs.lever.co/bolt/b286df9b-0df5-45af-8080-7b59e22d7171'
URL_g2 = 'https://jobs.lever.co/bolt/04d798cf-65eb-49b6-b526-329e00c98b9c'

URLS = [URL_l2, URL_l3, URL_l4, URL_l6, URL_l9, URL_g1, URL_g2]


def greenhouse(driver):
    print("found the attach")
    # os.curdir()
    time.sleep(8)
    # send_keys(os.path.join(__location__, 'Michael_Caneff_Resume_V3.pdf'))

    # Get the secret location for cover letter
    cover_letter = driver.find_element_by_id(
        "s3_upload_for_cover_letter").find_element_by_xpath('//*[@type="file"]')
    cover_letter.send_keys(
        "/Users/andrew/Desktop/Work-Code/Job-Process-Automation/TestingCoding/cover.pdf")
    time.sleep(2)

    # Get the secret location for resume
    resume = driver.find_element_by_id(
        "s3_upload_for_resume").find_element_by_xpath('//*[@type="file"]')
    resume.send_keys(
        "/Users/andrew/Desktop/Work-Code/Job-Process-Automation/TestingCoding/Michael_Caneff_Resume_V3.pdf")
    print("sub")

    time.sleep(5)
    return print("success")


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print('\n')

    driver.get("https://boards.greenhouse.io/asana/jobs/2344893")
    greenhouse(driver)
