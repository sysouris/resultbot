import bs4
import requests
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)
import time

def getResultDeclaredStatus(link, holyword) :
    url = link
    driver = browser.get(url)
    #time.sleep(0.7)
    gethtml = browser.page_source

    thepage = bs4.BeautifulSoup(gethtml, 'html.parser')
    #with open('response2.html','w') as file:
        #file.write(str(thepage))
        
    resultcontainer = thepage.select('.content')
    
    holyword1 = holyword    
    flength = len(holyword1)
    resultout = False
    status = "❌ Result NOT declared"
    
    for word in resultcontainer:
        for i in range(len(word.text)):
            chunk = word.text[i:i+flength].lower()
            if chunk == holyword1:
                resultout = True
                status = "✅ IIM-B has declared PGP 2023-25 Final Results!"
                #requests.get("https://api.telegram.org/bot6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc/sendMessage?chat_id=-1001832409595&text={}".format(status))
                break
        if resultout == True:
            break

    return status
    #requests.get("https://api.telegram.org/bot6009163802:AAHxItimxRZmeJCfi9VbO3IoTkvlKFoWWGc/sendMessage?chat_id=1862428631&text={}".format(status))
    browser.close()
    browser.quit()
    
#link = 'https://www.iimb.ac.in/pgp-admissions'
#print(getResultDeclaredStatus(link))


