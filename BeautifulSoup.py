from bs4 import BeautifulSoup
import requests
import re

SITE_LINK = "https://www.kooora.com"
LIST_OF_LINKS = []


def extract_links(site_link):
    r = requests.get(site_link)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        # for link in soup.find_all(['a', 'link']):
        #     if link.get('href'):
        #         formatted_link = format_link(link.get('href'), SITE_LINK)
        #         if formatted_link not in LIST_OF_LINKS:
        #             f.write(formatted_link + '\n')
        #             print(formatted_link)
        #             LIST_OF_LINKS.append(formatted_link)
        for link in soup.findAll('script'):
            print(link)


    r.close()

    # return


def format_link(link,SITE_LINK):
    if not link.startswith('http'):
        link = SITE_LINK + link
    return link


f = open("result.txt", "w")

extract_links(SITE_LINK)

# for line in LIST_OF_LINKS:
#     extract_links(line)

f.close()
