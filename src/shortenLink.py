from time import daylight
import requests
from dotenv import load_dotenv
from os import environ

# load environment variables


def shortenLink(link):
    load_dotenv()
    server_url = environ["SHORTURL_SERVER"]
    reqData = {
        'LongURL': link
    }

    r = requests.post(f"https://{server_url}", reqData)
    return r.text