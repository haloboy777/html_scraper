from bs4 import BeautifulSoup
from single_page_download import getAndSavePDFandVideo
import requests
initalUrl = requests.get('http://www.maths-screencasts.org.uk/topics.html');
parsedUrl = BeautifulSoup(initalUrl.text, 'html.parser');
listOfAllRawLinks = parsedUrl.find_all('a');
listOfContent =[]
for partOfLink in listOfAllRawLinks:
    listOfContent.append(partOfLink.get('href'));
topicLink = []
for link in listOfContent:
    if 'scast' in link:
        topicLink.append(link);

for link in topicLink:
    getAndSavePDFandVideo('http://www.maths-screencasts.org.uk/'+link);
