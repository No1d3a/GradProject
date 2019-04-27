from bs4 import BeautifulSoup
import requests
import re
import tldextract

SITE_LINK = "https://www.filgoal.com/"

LIST_OF_LINKS = []
ext = tldextract.extract(SITE_LINK)
domain = "{}.{}".format(ext.domain, ext.suffix)


def extract_links(site_link):
    r = requests.get(site_link)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all(['a', 'link']):
            if link.get('href'):
                formatted_link = format_link(link.get('href'), SITE_LINK)
                if in_scope(formatted_link):
                    if formatted_link not in LIST_OF_LINKS:
                        f.write(formatted_link + '\n')
                        print(formatted_link)
                        LIST_OF_LINKS.append(formatted_link)
            # for link in soup.findAll('script'):
            #     print(link)

        r.close()

    # return


def format_link(link,SITE_LINK):
    if not link.startswith('http'):
        link = SITE_LINK + link
    return link


def in_scope(f_link):
    result = re.search(domain, f_link)
    if result:
        return True
    else:
        return False


f = open("result.txt", "w", encoding="utf-8")

extract_links(SITE_LINK)
for link in LIST_OF_LINKS:
    extract_links(link)

f.close()

