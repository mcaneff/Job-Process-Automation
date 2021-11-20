import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

query = "Software Engineer"
location = "Toronto, Ontario"


def get_links(query, location, **kwargs) -> list:
    """
    Given a query and location, return a list of links to job postings
    :param query: the job title
    :param location: the location of the job
    :param kwargs: for prototyping. Possible arguments:
        - depth: the maximum number of pages to scrape
        - step: the spaces between different depth levels. Reccomended to be 10
        - visual: selenium vs requests
    :return: relavent info about jobs
    """

    # Match the url encoding for spaces
    query = query.replace(" ", "+")
    location = location.replace(" ", "+")

    # Construct the proper url for the view we want
    base_url = "https://www.google.com"
    query_specific = f"/search?q={query}+{location}"
    careers_params = "&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&htivrt=jobs&fpstate=tldetail&start="
    url = base_url + query_specific + careers_params

    kwargs_keys = list(kwargs.keys())

    # Process params
    if kwargs_keys and "depth" in kwargs_keys:
        depth = kwargs["depth"]
    else:
        depth = 5

    if kwargs_keys and "step" in kwargs_keys:
        step = kwargs["step"]
    else:
        step = 10

    if kwargs_keys and "visual" in kwargs_keys:
        visual = kwargs["visual"]
    else:
        visual = True

    for i in range(depth):
        if visual:
            # CHANGE THIS TO YOUR DRIVER
            driver = webdriver.Chrome(ChromeDriverManager().install())

            driver.get(url + str(i*step))
            sleep(1)
            job_root = driver.find_elements_by_xpath("//div[@jsname='c6W1S']")
            for job in job_root:

                links = job.find_elements_by_xpath("//div[@jsname='haAclf']")
                for button in links:
                    link = button.find_element_by_tag_name(
                        "a").get_attribute("href")
                    print("\n")
                    print(link)
            driver.quit()


print(get_links(query, location, j=1))