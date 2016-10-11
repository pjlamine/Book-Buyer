from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import floor

def getPrice(isbn, urgency):

    driver = webdriver.Chrome()
    url = "http://www.bookfinder.com/search/?isbn="+ str(isbn) + "&title=&author=&lang=en&mode=textbook&st=sr&ac=qr  "    #url to Scrape
    driver.get(url)

    pe = driver.find_element_by_xpath("//*[@id='bd-isbn']/div/table/tbody/tr/td[5]")        #Used Book Section
    priceElements = pe.find_elements_by_class_name("results-price")                         #price results elements

    prices = []
    for element in priceElements:
        print element.text
        prices.append(float(str(element.text)[1:]) )                                        #convert string to Numbers

    # for p in prices:
    #     print p

    # print "original avg: " , sum(prices)/len(prices)

    # def removeOutliers( lst):        #removes numbers outside 1.5 IQR of list
    #     outlierFree= []
    #     size = len(lst)
    #     Q1 = lst[int(size * .25)]
    #     Q2 = lst[int(size * .5) ]
    #     Q3 = lst[int(size * .75)]
    #     # print "Q1: ", Q1, "Q2: ", Q2 , "Q3: " , Q3
    #
    #     IQR = Q1 - Q3                               #calculate IQR and Fence for numbers
    #     Fence = IQR * 1.5
    #
    #     for item in lst:                               #remove outliers outside of fence from lst
    #         if item > Q3 + Fence:
    #             print "Removed Outlier " , item
    #             lst.remove(item)
    #
    #     return lst                          #returns list without outliers

    # prices = removeOutliers(prices)
    prices = prices[0 : len(prices) / 2]
    #
    # for p in prices:
    #     print p
    if urgency == 3:
        sellPrice = sum(prices)/len(prices)
    if urgency == 2:
        sellPrice = floor(prices[3])
    if urgency == 1:
        sellPrice = floor(prices[0])

    return sellPrice
