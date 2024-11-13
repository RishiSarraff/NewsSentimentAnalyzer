from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dateFormatter import formatDate
from FoxDB import insert_into_DB

def scrapePoliticsFOXSections(driver, url):
    driver.get(url)
    pagetopic = "General Politics"

    pageArticles = driver.find_elements(By.CLASS_NAME, "article")

    linkSet = set()

    for article in pageArticles:
        currLink = article.find_element(By.TAG_NAME, "a").get_attribute("href")
        if "video" not in currLink.lower() and currLink not in linkSet:
            linkSet.add(currLink)

    count = 1

    for link in linkSet:
        try:
            driver.get(link)

            title = driver.find_element(By.CLASS_NAME, "headline").text
            authorDiv = driver.find_element(By.CLASS_NAME, "author-byline")
            authorName = authorDiv.find_element(By.TAG_NAME, "a").text

            pageContent = driver.find_element(By.CLASS_NAME, "article-body")

            listOfSpeakables = pageContent.find_elements(By.TAG_NAME, "p")

            text = ""

            for innerText in listOfSpeakables:
                text += innerText.text + " "

            articleDateDiv = driver.find_element(By.CLASS_NAME, "article-date")
            articleDateTime = articleDateDiv.find_element(By.TAG_NAME, "time").text

            articleTimeArr = articleDateTime.split(" ")
            month_text = articleTimeArr[0].strip()
            year = articleTimeArr[2]
            month = formatDate(month_text)

            print(count)
            print(link)
            print(title)
            print(text)
            print(authorName)
            print(month)
            print(year)
            print()

            foxObj = {
                    "PageTopic": pagetopic,
                    "Year": year,
                    "Month": month,
                    "Title": title,
                    "Author": authorName,
                    "Content": text,
                    "Link": link
                }
            insert_into_DB(foxObj)
            count+=1
        except:
            print(link)

        driver.back()

def scrapeCongressFOXSections(driver, url):

    pass

def scrapeNewsletterFOXSections(driver, url):
    pass
