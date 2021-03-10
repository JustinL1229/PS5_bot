from selenium import webdriver
import time
from twilio.rest import Client

restart = True

while restart = True:
    client = Client("AC7192d9489d41b4ec95ed47c3990b1a4f", "96da055a9c4d31d777c2040ca3965b69")
    driver = webdriver.Chrome('/Users/justinlaughlin/Documents/chromedriver')
    driver.get('https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816')
    classes = []
    for i in driver.find_elements_by_class_name('sony-text-body-1'):
        classes.append(i.text)

    while 'Out of Stock' in classes:
        time.sleep(2)   
        driver.refresh()
        classes = []
        for i in driver.find_elements_by_class_name('sony-text-body-1'):
            classes.append(i.text)

    client.messages.create(to="+12073182885", 
                        from_="+15165888077", 
                        body="https://direct.playstation.com/en-us/consoles/console/playstation5-console.3005816")
    
    