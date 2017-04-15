import requests
import re
from bs4 import BeautifulSoup

def downloadFromUrl(downUrl):
    print(downUrl);
    localFilename = downUrl.split('/')[-1]
    r = requests.get(downUrl, stream=True)
    with open(localFilename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print(localFilename+' Has been downloaded.');
    return localFilename

def getAndSavePDFandVideo(varUrl):
    intialUrl = requests.get(varUrl);
    parsedUrl = BeautifulSoup(intialUrl.text, 'html.parser');
    listOfAllRawLinks = parsedUrl.find_all('a');
    listOfContent = [];
    
    for partOfLink in listOfAllRawLinks:
        listOfContent.append(partOfLink.get('href'));
    linksForDownload = []
    
    for partOfLink in listOfContent[1:]:
        linksForDownload.append('http://www.maths-screencasts.org.uk/scast/'+partOfLink);

    for link in linksForDownload:
        downloadFromUrl(link);


getAndSavePDFandVideo('http://www.maths-screencasts.org.uk/scast/TaylorII.html');
