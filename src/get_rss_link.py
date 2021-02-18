"Takes channel link and returns RSS link"

import requests

def convert_link(link):
    "Takes a youtube channel link as an argument and returns the RSS link for that channel"
    try:
        #Gets HTML of youtube channel, then finds RSS link
        page = requests.get(link).text
        print("Here")
        identifier = "<link rel=\"alternate\" type=\"application/rss+xml\" title=\"RSS\" href=\""
        page = page[page.find(identifier):][67:143]

        #Checks if link has been found
        if page[:8] == "https://":
            return page
        return "Failed, possibly incorrect link?"

    except:
        return "Failed, not a URL"
