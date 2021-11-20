import csv, json, requests, string
from bs4 import BeautifulSoup
import re
from urllib.request import Request, urlopen
PREFERENCES = {
    "position_title": "Software Engineering Intern",
    "location": "San Francisco"
    } 
internFlag = 0
def greenGet(job_boards):
    homeL = "https://boards.greenhouse.io/"
    all_positions = []

    for job_board in job_boards:
        tempText=homeL + job_board["Company"].replace(" ", "").lower()
        
        page = requests.get(homeL + job_board["Company"].replace(" ", "").lower()) if "Link" not in job_board else requests.get(homeL + job_board["Link"])
        sections = BeautifulSoup(page.text, 'html.parser').find_all("section", {"class": "level-0"})

        if len(sections) == 0:
            print("ERROR:", job_board["Company"], "could not be scraped!")
        else:
            for section in sections:
                for position in section.find_all("div", {"class": "opening"}):
                    all_positions.append({
                        "Company": job_board["Company"],
                        "Title": position.find("a").getText().strip(),
                        "Link": ("" if position.find("a")['href'].startswith("https") else homeL[:-1]) + position.find("a")['href'],
                        "Location": position.find("span", {"class": "location"}).getText().strip()
                    })


    return all_positions


def leverGet(job_boards):
    homeL = "https://jobs.lever.co/"
    all_positions = []

    for job_board in job_boards:
    

        page = requests.get(homeL + job_board["Company"].replace(" ", "").lower()) if "Link" not in job_board else requests.get(homeL + job_board["Link"])
        positions = BeautifulSoup(page.text, 'html.parser').find_all("div", {"class": "posting"})

        if len(positions) == 0:
            print("ERROR:", job_board["Company"], "could not be scraped!")
        else:
            for position in positions:
                if position.find("span", {"class": "sort-by-commitment"}):
                    all_positions.append({
                        "Company": job_board["Company"],
                        "Title": position.find("h5").getText() + " (" + position.find("span", {
                            "class": "sort-by-commitment"}).getText() + ")",
                        "Link": position.find("a", {"class": "posting-title"})['href'],
                        "Location": position.find("span", {"class": "sort-by-location"}).getText()
                    })
                else:
                    all_positions.append({
                        "Company": job_board["Company"],
                        "Title": position.find("h5").getText(),
                        "Link": position.find("a", {"class": "posting-title"})['href'],
                        "Location": position.find("span", {"class": "sort-by-location"}).getText()
                    })


    return all_positions



def extract_key(elem, key):
    if isinstance(elem, dict):
        if key in elem:
            return elem[key]
        for k in elem:
            item = extract_key(elem[k], key)
            if item is not None:
                return item
    elif isinstance(elem, list):
        for k in elem:
            item = extract_key(k, key)
            if item is not None:
                return item
    return None


def get_request_to_dict(link, company_name):
    req = Request(link)
    req.add_header("Accept", "application/json,application/xml")

    try:
        raw_page = urlopen(req).read().decode()
        page_dict = json.loads(raw_page)
    except:
        print("ERROR:", company_name, "could not be scraped!")
        page_dict = {}

    return page_dict



def workGet(job_boards):
    all_positions = []

    for job_board in job_boards:
        print("\tScraping for " + job_board["Company"] + "...", end=" ", flush=True)

        postings_page_dict = get_request_to_dict(job_board["Link"], job_board["Company"])
        if len(postings_page_dict) > 0:
            base_url = job_board["Link"][:job_board["Link"].index('.com') + 4]
            pagination_end_point = base_url
            for end_point in extract_key(postings_page_dict, 'endPoints'):
                if end_point['type'] == "Pagination":
                    pagination_end_point += end_point['uri'] + '/'
                    break

            while True:
                postings_list = extract_key(postings_page_dict, 'listItems')
                if postings_list is None:
                    break

                paginated_urls = []
                for position in postings_list:
                    paginated_urls.append({
                        "Company": job_board["Company"],
                        "Title": position["title"]["instances"][0]["text"],
                        "Link": base_url + position["title"]["commandLink"],
                        "Location": position["subtitles"][0]["instances"][0]["text"] if ", More..." not in position["subtitles"][0]["instances"][0]["text"] else position["subtitles"][0]["instances"][0]["text"][:position["subtitles"][0]["instances"][0]["text"].index(", More...")]
                    })

                all_positions += paginated_urls
                postings_page_dict = get_request_to_dict(pagination_end_point + str(len(all_positions)), job_board["Company"])

            

    return all_positions





def remove_punctuation(str):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""

    for char in str:
        if char not in punctuation:
            no_punct += char

    return no_punct


def filterByName(positions, required_keywords):
    filtered_list = []

    for position in positions:
        if len(required_keywords) > 0:
            if True in [(True if (keyword.lower() in position["Title"].lower()) else False) for keyword in required_keywords]:
                filtered_list.append(position)

    return filtered_list



def export_to_csvWorkday(positions, filename):
    f = open(f"{filename}.csv", "w")
    writer = csv.DictWriter(
        f, fieldnames=["Company", "Title", "Link", "Location"])
    writer.writeheader()
    filt=[]
    for pos in positions:
        arrX= PREFERENCES["location"].split(" ")
        if re.search(f'{arrX[0]}-{arrX[1]}', pos["Link"], re.IGNORECASE):

            filt.append(pos)
    writer.writerows(positions)
    f.close()

def export_to_csv(positions, filename):
    f = open(f"{filename}.csv", "w")
    writer = csv.DictWriter(
        f, fieldnames=["Company", "Title", "Link", "Location"])
    writer.writeheader()
    filt=[]
    for pos in positions:
        
        if re.search(PREFERENCES["location"], pos["Location"], re.IGNORECASE):
            if internFlag==1:
                if re.search("software", pos["Title"], re.IGNORECASE):
                    filt.append(pos)
            else:
                filt.append(pos)


    writer.writerows(filt)
    f.close()


def export_to_csv(positions, filename):
    f = open(f"{filename}.csv", "w")
    writer = csv.DictWriter(
        f, fieldnames=["Company", "Title", "Link", "Location"])
    writer.writeheader()
    filt=[]
    for pos in positions:
        
        if re.search(PREFERENCES["location"], pos["Location"], re.IGNORECASE):

            filt.append(pos)
    writer.writerows(filt)
    f.close()


def getBoard(all_companies,required_keywords):
  
    greenPost = greenGet(all_companies["greenhouse"])


    leverPost = leverGet(all_companies["lever"])
   
    greenPost = filterByName(greenPost, required_keywords)
    leverPost = filterByName(leverPost, required_keywords)
    
   

    export_to_csv(greenPost,"greenPost")
    export_to_csv(leverPost,"leverPost")
    workPost = workGet(all_companies['workday'])
    ##print(workPost)
    workPost = filterByName(workPost, required_keywords)
    export_to_csvWorkday(workPost,"workPost")

def scr():
    all_companies = {
        "greenhouse": json.load(open('resources/greenhouse_companies.json')),
        "lever": json.load(open('resources/lever_companies.json')),
        "workday": json.load(open('resources/workday_companies.json'))
    }
    tempV=PREFERENCES["position_title"].split(" ")
     
    if len(tempV)>2:
            internFlag=1
            getBoard(
                all_companies,
                
                 ["intern"]
            )
    else :
            getBoard(
                all_companies,
               ["software"]
            )


