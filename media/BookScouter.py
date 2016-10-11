from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from math import ceil

class BookScouter(object):

    def __init__(self, isbn):
        self.isbn = str(isbn)



    # def getCheggPrice(self):
    #     return self.cheggPrice

    def removeOutliers(self, lst):        #removes numbers outside 1.5 IQR of list
        outlierFree= []
        size = len(lst)
        Q1 = lst[int(size * .25)]
        Q2 = lst[int(size * .5) ]
        Q3 = lst[int(size * .75)]
        # print "Q1: ", Q1, "Q2: ", Q2 , "Q3: " , Q3

        IQR = Q1 - Q3                               #calculate IQR and Fence for numbers
        Fence = IQR * 1.5

        for item in lst:                               #remove outliers outside of fence from lst
            if item < Q1 - Fence or item > Q3 + Fence:
                print "Removed Outlier " , item
                lst.remove(item)

        return lst                          #returns list without outliers

    def getPrice(self):

        def getAmazonPrice():
            size = len(self.amazon)
            print "doing amazon stuff"
            for i in range(2, 8):
                print self.amazon[size-i]
                if self.amazon[size-i] == '$':
                    print "Found it! ", self.amazon[size - i + 1:]
                    return float(self.amazon[size - i + 1:])

        driver = webdriver.Chrome()
        url = "https://bookscouter.com/prices.php?isbn=" + self.isbn + "&searchbutton=Sell"        #url to Scrape
        driver.get(url)
        # nonlocal priceElements
        name = str(driver.find_element_by_xpath("//*[@class='search-result']/h1").text)
        # print name

        self.priceElements  = driver.find_elements_by_class_name("book-price-normal")           #Scraped list of prices
        self.amazon = str(driver.find_element_by_class_name("book-specs").text)
        amazonPrice = getAmazonPrice()

        try:                            #catch exception if chegg element cant be found
            chegg = driver.find_element_by_id("offer43").find_element_by_class_name("book-price-normal")
            self.cheggPrice = float(str(chegg.text)[1:])                                #Price from Chegg.com
        except Exception as e:          #catch exception if element cant be found
            print e
            self.cheggPrice = 0         #set cheggPrice to 0 to avoid errors


        prices = []

        for Element in self.priceElements:       #adds numeric prices to prices list
            try:
                price = float(str(Element.text)[1:])       #convert web element into string, cut first char off string, convert to float
            except ValueError:                              #Catch exception if Element cant be converted to float
                # print "Not a Number"
                continue

            if price > 0:
                prices.append(price)


        assert "No results found." not in driver.page_source
        driver.close()                        #close web driver

        if len(prices) > 4:
            prices = BookScouter.removeOutliers(self,prices)         #remove outliers for calculation

        marketAvg = sum(prices) / len(prices)              #Avg of market prices


        if marketAvg > self.cheggPrice:                     #make price < cheggPrice
            # return (marketAvg, self.cheggPrice)
            buyPrice= marketAvg
        else:
            difference = int(self.cheggPrice - marketAvg)
            print "Difference between chegg and Market is " ,difference
            buyPrice = self.cheggPrice * 1.05

            # return (buyPrice, self.cheggPrice)
        data = [self.cheggPrice, name]

        if  amazonPrice > buyPrice * 1.3 :                #ensure proift of atleast 30% or $5
            data.insert(0,ceil(buyPrice))
            return data
        elif amazonPrice * .3 > 5 :
            data.insert(0, ceil(amazonPrice * .70))
            return data
        else :
            if amazonPrice * .5 > 5:

                data.insert(0, ceil(amazonPrice *.5))
                return data
            else:
                data.insert(0,0)
                return data

        # returns list of [buyPrice, cheggPRice, name]






    # else:
    #     print prices[3]
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)


        #
        # sample = []
        # for price in prices:
        #     if price > prices[] - iqr or price < mean + iqr :
        #         sample.append(price)
        # print "Sample mean is " , sum(sample)/len(sample)
        # print "chegg Price is " + cheggPrice

        # for p in prices:
        #     print p

        # print "Statistics"
        # print "Old Mean " , sum(prices) / len(prices)


    # print BookScouter.getPrice(self)
    # print "Cheggs Price is " , getCheggPrice(self)
