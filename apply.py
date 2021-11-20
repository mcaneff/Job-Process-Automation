from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import os  # to get the resume file
import time  # to sleep
#import get_links

# sample application links if we don't want to run get_links.py
URL_l2 = 'https://boards.greenhouse.io/doordash/jobs/3393928?gh_jid=3393928&rx_c=corp---canada&rx_campaign=indeed144&rx_group=129152&rx_job=3393928&rx_r=none&rx_source=Indeed&rx_ts=20211120T140008Z&rx_p=FGY5TRVQOV&rx_viewer=704eae0e2d0a11ec85ec9fccc13cdfd51924a10d0f42408aa10bf7cd9b4a6e67'
URL_l3 = 'https://boards.greenhouse.io/asana/jobs/2344893'
URL_l4 = 'https://boards.greenhouse.io/asana/jobs/3644497'
URL_l6 = 'https://boards.greenhouse.io/asana/jobs/3644690'
URL_l8 = 'https://jobs.lever.co/bolt/46e30240-63fb-4e10-af10-dad7e355c635'
URL_l9 = 'https://jobs.lever.co/bolt/e73884bc-f2c1-4069-b496-2b9564390520'
URL_g1 = 'https://jobs.lever.co/bolt/b286df9b-0df5-45af-8080-7b59e22d7171'
URL_g2 = 'https://jobs.lever.co/bolt/04d798cf-65eb-49b6-b526-329e00c98b9c'

# there's probably a prettier way to do all of this
# test URLs so we don't have to call get_links
URLS = [URL_g2, URL_g1, URL_l4, URL_l9, URL_l8, URL_l2]
#URLS= get_links
# Fill in this dictionary with your personal details!
JOB_APP = {
    "first_name": "Michael",
    "last_name": "Caneff",
    "email": "M.Caneff@outlook.com",
    "phone": "647-237-2810",
    "org": "Team Lead",
    "resume": "resume.pdf",
    "resume_textfile": "resume_short.txt",
    "linkedin": "https://www.linkedin.com/in/michael-caneff-324281108/",
    "website": "N/a",
    "github": "https://github.com/mcaneff",
    "twitter": "N/a",
    "location": "San Francisco, California, United States",
    "grad_month": '06',
    "grad_year": '2021',
    "university": "Western University"
}

# Greenhouse has a different application form structure than Lever, and thus must be parsed differently


def greenhouse(driver):

    # basic info
    driver.find_element_by_id('first_name').send_keys(JOB_APP['first_name'])
    time.sleep(1)
    driver.find_element_by_id('last_name').send_keys(JOB_APP['last_name'])
    time.sleep(1)
    driver.find_element_by_id('email').send_keys(JOB_APP['email'])
    time.sleep(1)
    driver.find_element_by_id('phone').send_keys(JOB_APP['phone'])
    time.sleep(1)

    # This doesn't exactly work, so a pause was added for the user to complete the action
    try:
        loc = driver.find_element_by_id('job_application_location')
        loc.send_keys(JOB_APP['location'])
        loc.send_keys(Keys.DOWN)  # manipulate a dropdown menu
        loc.send_keys(Keys.DOWN)
        loc.send_keys(Keys.RETURN)

    except NoSuchElementException:
        pass

    # Upload Resume as a Text File
    # driver.find_elements_by_xpath('//*[@id="main_fields"]/div[8]/div/div[3]/a[1]').click()

    # driver.find_element_by_css_selector("[data-source='paste']").click()
    # with open(JOB_APP['resume_textfile']) as f:
    #    lines = f.readlines()  # add each line of resume to the text area
    #    for line in lines:
    #        resume_zone.send_keys(line.decode('utf-8'))

    # add linkedin

    try:
        driver.find_element_by_xpath(
            '//input[@name="job_application[answers_attributes][0][text_value]"]').send_keys(JOB_APP['linkedin'])
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'LinkedIn')]").click()
    except NoSuchElementException:
        pass

    # add graduation year
    try:
        driver.find_element_by_xpath("//select/option[text()='2021']").click()
    except NoSuchElementException:
        pass

    # add university
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'Harvard')]").click()
    except NoSuchElementException:
        pass

    # add degree
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'Bachelor')]").click()
    except NoSuchElementException:
        pass

    # add major
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'Computer Engineering')]").click()
    except NoSuchElementException:
        pass

    # add how did you hear about this job?
    try:
        driver.find_element_by_xpath(
            "//label[contains(.,'How did you hear about this job?')]").send_keys("Glass Door")
    except NoSuchElementException:
        pass

    # add website
    try:
        driver.find_element_by_xpath(
            "//label[contains(.,'Website')]").send_keys(JOB_APP['website'])
    except NoSuchElementException:
        pass

    # add work authorization
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'any employer')]").click()
    except NoSuchElementException:
        pass

    # add Gender
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'Male')]").click()
    except NoSuchElementException:
        pass

    # add Race
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'White')]").click()
    except NoSuchElementException:
        pass

    # add disability
    try:
        driver.find_element_by_xpath(
            '//*[@id="job_application_disability_status"]/option[3]').click()
    except NoSuchElementException:
        pass
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'I don't have a disability')]").click()
    except NoSuchElementException:
        pass

    # add Veteran Status
    try:
        driver.find_element_by_xpath(
            "//select/option[contains(.,'I am not a protected veteran')]").click()
    except NoSuchElementException:
        pass

    time.sleep(3)
    driver.find_element_by_id("submit_app").click()


# Handle a Lever form
def lever(driver):
    # navigate to the application page
    driver.find_element_by_class_name('template-btn-submit').click()

    # basic info
    first_name = JOB_APP['first_name']
    last_name = JOB_APP['last_name']
    # f string didn't work here, but that's the ideal thing to do
    full_name = first_name + ' ' + last_name
    driver.find_element_by_name('name').send_keys(full_name)
    driver.find_element_by_name('email').send_keys(JOB_APP['email'])
    driver.find_element_by_name('phone').send_keys(JOB_APP['phone'])
    driver.find_element_by_name('org').send_keys(JOB_APP['org'])

    # socials
    driver.find_element_by_name(
        'urls[LinkedIn]').send_keys(JOB_APP['linkedin'])
    driver.find_element_by_name('urls[Twitter]').send_keys(JOB_APP['twitter'])
    try:  # try both versions
        driver.find_element_by_name(
            'urls[Github]').send_keys(JOB_APP['github'])
    except NoSuchElementException:
        try:
            driver.find_element_by_name(
                'urls[GitHub]').send_keys(JOB_APP['github'])
        except NoSuchElementException:
            pass
    driver.find_element_by_name(
        'urls[Portfolio]').send_keys(JOB_APP['website'])

    # add university
    try:
        driver.find_element_by_class_name('application-university').click()
        search = driver.find_element_by_xpath("//*[@type='search']")
        search.send_keys(JOB_APP['university'])  # find university in dropdown
        search.send_keys(Keys.RETURN)
    except NoSuchElementException:
        pass

    # add how you found out about the company
    try:
        driver.find_element_by_class_name('application-dropdown').click()
        search = driver.find_element_by_xpath(
            "//select/option[text()='Glassdoor']").click()
    except NoSuchElementException:
        pass

    # submit resume last so it doesn't auto-fill the rest of the form
    # since Lever has a clickable file-upload, it's easier to pass it into the webpage
    driver.find_element_by_name('resume').send_keys(os.getcwd()+"/resume.pdf")
    driver.find_element_by_class_name('template-btn-submit').click()


if __name__ == '__main__':
    Successes = 0
    Failures = 0
    # call get_links to automatically scrape job listings from glassdoor
    # This is where the get_links gets called such that all of them are saved
    aggregatedURLs = URLS  # get_links.getURLs #getURLs()
    print(f'Job Listings: {aggregatedURLs}')
    print('\n')

    #driver = webdriver.Chrome(executable_path='/Users/MCane/chromedriver/chromedriver.exe')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for url in aggregatedURLs:
        print('\n')

        if 'greenhouse' in url:
            driver.get(url)
            try:
                greenhouse(driver)
                print(f'SUCCESS FOR: {url}')
                Successes += 1
            except Exception:
                print(f"FAILED FOR {url}")
                Failures += 1
                continue

        elif 'lever' in url:
            driver.get(url)
            try:
                lever(driver)
                print(f'SUCCESS FOR: {url}')
                Successes += 1
            except Exception:
                print(f"FAILED FOR {url}")
                Failures += 1
                continue
        # i dont think this else is needed
        else:
            # print(f"NOT A VALID APP LINK FOR {url}")
            continue

        # can lengthen this as necessary (for captcha, for example)
        time.sleep(20)

    driver.close()
    print("In total there were ", Successes,
          "Successes and ", Failures, "Failures \n")
