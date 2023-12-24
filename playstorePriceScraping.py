import re
from bs4 import BeautifulSoup
import requests
import datetime

key = 0
def convertTuple(tuple):
    string = ''.join(map(str, tuple))
    return string


urls = ["https://play.google.com/store/books/details/Rod_Dreher_Live_Not_by_Lies?id=JqfiDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_Romans_1_7_For_You?id=wwPPDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_Romans_8_16_For_You?id=uwTPDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_Galatians_For_You?id=7QTPDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_Judges_For_You?id=XQTPDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_On_Marriage?id=i2asDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_The_Prodigal_Prophet?id=uRpPDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_Rediscovering_Jonah?id=dcXdDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Henry_Cloud_Boundaries_Updated_and_Expanded_Editio?id=-YVDDgAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Gary_Thomas_Sacred_Marriage?id=_txoCgAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Debra_Fileta_Love_in_Every_Season?id=-eCwDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_On_Birth?id=i3ypDwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_The_Prodigal_Prophet?id=NX9ODwAAQBAJ&gl=DE",
        "https://play.google.com/store/books/details/Timothy_Keller_On_Marriage?id=znupDwAAQBAJ&gl=DE"]

for url in urls:
    livenbl = requests.get(url)
    soup = BeautifulSoup(livenbl.content, 'html.parser')

    preis = soup.find("meta", itemprop="price")
    temp = str(url).strip("''")
    title = re.findall('[A-Z]\w*', temp)
    ct = datetime.datetime.now()
    key += 1
    tuple = (key, "\t", preis["content"], "\t", title[0], "\t", ct, '\n')
    string = convertTuple(tuple)

    print(string)
