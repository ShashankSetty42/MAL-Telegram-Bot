from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq


def scrape_page(anime_name):
    #dictonary to store anime info
    dict_data = {
        "Title": "",
        "Image": "",
        "Score": "",
        "Episodes": "",
        "Genre": "",
        "Duration": "",
        "MAL": "",
    }
    #replace %20 with spaces to URL
    url = "https://myanimelist.net/search/all?q=" + anime_name.replace(" ", "%20")
    #make connection to URL and obtain the HTML code
    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")

    #get title and link for the anime
    containers = page_soup.findAll("div", {"class": "picSurround di-tc thumb"})
    dict_data["Title"] = str([containers[0].a.img["alt"]])
    url = str(containers[0].a["href"])
    dict_data["MAL"] = url
    #navigate to the first result by re-initializing the URL value to the first result URL and connect
    uclient = ureq(url)
    page_html = uclient.read()
    uclient.close()
    page_soup = soup(page_html, "html.parser")

    #obtain rating, score, image link, episodes and duration
    rating = page_soup.find("span", {"itemprop": "ratingValue"})
    dict_data["Score"] = str(rating.text)
    img_link = page_soup.find("meta", {"property": "og:image"})
    dict_data["Image"] = str(img_link["content"])
    info = page_soup.findAll("div", {"class": "spaceit"})
    dict_data["Episodes"] = str(info[0].text).replace(' ', '').replace('Episodes:', '').replace('\n', '')
    dict_data["Duration"] = str(info[5].text).replace('Duration:', '').replace('\n', '').replace(' ', '').replace('min.','min ').replace('perep.', 'per ep.')
    #obtain generes and concat into readable string
    temp_string = page_soup.findAll("span", {"itemprop": "genre"})
    genre = ""
    for items in temp_string:
        genre += items.text + ", "
    dict_data["Genre"] = genre[:-1]
    #return the resultant dictonary value
    return dict_data



