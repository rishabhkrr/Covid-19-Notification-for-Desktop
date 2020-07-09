from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\Risabh\\Desktop\\work\\python-ex\\corona\\corona.ico",
        timeout = 20
    )

def getUrl(url):
    req = requests.get(url)
    return req.text

if __name__ == '__main__':
    # notifyMe("Rishabh...", "notification")
    while True:
        htmldata = getUrl("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(htmldata, "html.parser")
        # print(soup.prettify())

        myData = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myData += tr.get_text()
        dataList = myData.split("\n\n")

        states = ["Bihar", "Maharashtra", "Jharkhand"]

        for item in dataList[0:35]:
            newDataList = item.split("\n")
            if newDataList[1] in states:
                print(newDataList)
                Title = "Case caused by Covid-19"
                Text = f"State:{newDataList[1]}:ActiveCases: {newDataList[2]}\nCured/Discharged: {newDataList[3]}\nDeaths: {newDataList[4]}\nTotalCases: {newDataList[5]}"
                notifyMe(Title, Text)
                time.sleep(2)
        time.sleep(10)