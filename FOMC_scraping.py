""" Import Packages and define Input Variables """
from urllib.request import urlopen # urllib provides a high-level interface for fetching data across the World Wide Web.
from bs4 import BeautifulSoup # BeautifulSoup will extract/parse the data from the HTML or XML documents
import re # A Regular Expression Module providing regular expression matching operation
Year_Start = 2000
Year_End   = 2018
Year_Segmentation = 2013 # Notice: This variable should be updated yearly.
# The FOMC materials in years (<  Year_Segmentation) will be put in websites separately, such as https://www.federalreserve.gov/monetarypolicy/fomchistorical2011.htm
# The FOMC materials in years (>= Year_Segmentation) will be put in a website together, that is https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
base_url   ='https://www.federalreserve.gov'



''' The Variable links will get FED Minutes' links. '''
links = []
for year in range(Year_Start, Year_End+1):
    print(year)
    if year < Year_Segmentation:
        fomc_url = base_url + '/monetarypolicy/fomchistorical'+str(year)+'.htm'
    else:
        fomc_url = base_url + '/monetarypolicy/fomccalendars.htm'
    fomc_socket = urlopen(fomc_url) # urlopen(url[, data[, proxies]]) will open a network object denoted by a Universal Resource Locator (URL) for reading.
    soup = BeautifulSoup(fomc_socket, 'html.parser') # Beautiful Soup supports the HTML parser included in Python’s standard library (ex. this one), but it also supports a number of third-party Python parsers.
    statements = soup.find_all('a', href=re.compile('\A(.*?)/fomc/minutes/\d{8}.htm\Z'                    +'|'+\
                                                    '\A(.*?)/monetarypolicy/fomc'+str(year)+'\d{4}.htm\Z' +'|'+\
                                                    '\A(.*?)/monetarypolicy/fomcminutes'+str(year)+'\d{4}.htm\Z'))
    # \A and \Z are important http://blog.csdn.net/justheretobe/article/details/53152267
    temp_links = []
    for statement in statements:
        temp_link = statement.attrs['href']
        temp = temp_link.find('gov')
        if temp>0:
            temp_link = temp_link[temp+3:]
        temp_links.append(temp_link)
    links.append(temp_links)
    #statement.attrs['href'] will retrun an dictionary's value which is the related url. Take <a href="http://www.baidu.com" title="Yes me">Baidu</a>as an example, there would be {'href': 'http://www.baidu.com', 'title': 'Yes me' }.



''' The Variable dates will get Fed Minutes' dates. '''
def get_dates(links):
    dates = []
    for index1 in range(len(links)):
        temp = []
        for index2 in range(len(links[index1])):
            temp.append(int(re.compile('\d{8}').findall(links[index1][index2])[0]))
        dates.append(temp)
    return dates
dates = get_dates(links)



''' The Variable articles will get Fed Minutes' articles. '''
def get_articles(links):
    articles = []
    for index1 in range(len(links)):
        print("Getting Articles:",index1)
        temp = []
        for index2 in range(len(links[index1])):
            print(".......................",index2+1)
            statement_socket = urlopen(base_url + links[index1][index2])
            statement = BeautifulSoup(statement_socket, 'html.parser')
            paragraphs = statement.findAll('p')
            temp.append("\n\n".join([paragraph.get_text().strip() for paragraph in paragraphs]))
        articles.append(temp)
    return articles
articles = get_articles(links)



'''Below Codes for Saving the articles'''
import pickle
def Save_articles_pickle(articles,dates):
    pickle.dump(articles,open('articles.pickle','wb'))
    pickle.dump(dates,open('dates.pickle','wb'))
Save_articles_pickle(articles,dates)