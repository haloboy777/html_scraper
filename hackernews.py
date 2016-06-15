from lxml import html
import requests

page = requests.get('https://news.ycombinator.com/')
tree = html.fromstring(page.content)

#This will create a list of headings and links:
heading = tree.xpath('//a[@class="storylink"]/text()')
links = tree.xpath('//td[@class="title"]/a/@href')

x = open('Today\'s News.txt','w')

for i in range(len(heading)):
    print(i+1,heading[i],"*",links[i],"*", file=x)

x.close()