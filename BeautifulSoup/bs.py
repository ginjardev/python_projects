import requests
from bs4 import BeautifulSoup
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# an entry URL to begin web scraping 
start_url = "https://amzn.to/3DJ1ubJ"

next_page_url = ''
bestsellers_list = []

def start_page(link):
    """ This returns a BeautifulSoup document from a given link """
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def get_title(doc):
    """ This takes a parsed element and returns the title for each book """
    try:
        title = doc.select("ul li")[0].select("span > span")[0].string.strip()
    except IndexError:
        title = None
    return title

def get_rating(doc):
    """ This takes a parsed element and returns the rating for each book """
    try:
        rating = doc.select("ul li")[1].select("span > span")[0].string.split(" ")[0]
    except IndexError:
        rating = None
    return rating

def get_price(doc):
    """ This takes a parsed element and returns the price for each book """
    try:
        price = doc.select("div ul *")[-2].string
    except IndexError:
        price = None
    return price

def get_img_url(doc):
    """ This takes a parsed element and returns the image URL for each book """
    try:
        img_url = doc.select("div > div > img")[0]["src"]
    except IndexError:
        img_url = None
    return img_url

def get_next_page_url(soup):
    """ This takes a soup and returns the URL for the next page """
    global next_page_url
    try:
        next_page_url = soup.select('.a-last > a')[0]['href']
        next_page_url = 'https://amazon.com' + next_page_url
    except IndexError:
        next_page_url = next_page_url
    return next_page_url

def next_page(link):
    """ This takes a link and moves the scraper function to the next page """
    if next_page_url == '':
        scrape_page_content(link)
    else:
        try: 
            if next_page_url:
                scrape_page_content(next_page_url)
        except IndexError:
            return f'That\'s the end!'


# the actual scraping of data happens here
counter = 1
def scrape_page_content(link):
    """ This scrapes a given page for the title, rating, price, image URL
    and next page URL. 
    """
    soup = start_page(link)
    # the div containing required info is picked out
    div = soup.find_all("div", class_="a-section browse-grid-view-item-unit")
    global counter
    global next_page_url
    for d in div:
        title = get_title(d)
        rating = get_rating(d)
        price = get_price(d)
        img_url = get_img_url(d)

        # a Python dict is added to the bestsellers list
        bestsellers_list.append({"s/n": counter,"title":title,"rating":rating,"price":price, "image URL" :img_url})
        counter += 1
    
    next_page_url = get_next_page_url(soup)


#for loop to scrape across multiple pages
for i in range(5):
    next_page(start_url)


#the bestseller list is written to a JSON file
json_file = json.dumps(bestsellers_list, indent=2)
with open('data.json', 'w') as f:
    f.write(json_file)



