from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dateFormatter import formatDate
from CNNDB import insert_into_DB


def scrapeSCOTUS(driver, url):
    # TO:DO
    driver.get(url)
    pagetopic = "SCOTUS"

    # there are three list of links
    listOfLinks1 = driver.find_elements(By.CLASS_NAME, "container__field-links")

    childLink = []

    for parent_element in listOfLinks1:
        listOfChildren = parent_element.find_elements(By.CLASS_NAME, "container__item")
        for child in listOfChildren:
            linkUrl = child.find_elements(By.TAG_NAME, "a")[0].get_attribute("href")
            if "videos" not in linkUrl:
                childLink.append(linkUrl)

    for link in childLink:
        driver.get(link)

        title = driver.find_element(By.CLASS_NAME, "headline__text").text
        try:
            author = driver.find_element(By.CLASS_NAME, "byline__name").text
        except:
            author = ""

        dateElement = driver.find_element(By.CLASS_NAME, "timestamp").text.split(', ')
        month, year = formatDate(dateElement)

        content = driver.find_element(By.CLASS_NAME, "article__content").text

        cnnObject = {
                     "PageTopic": pagetopic,
                     "Year": year,
                     "Month": month,
                     "Title": title,
                     "Author": author,
                     "Content": content,
                     "Link": link
                     }
        insert_into_DB(cnnObject)

        driver.back()

def scrapeCongress(driver, url):
    # TO:DO
    driver.get(url)
    print("Congress")

def scrapeFactCheck(driver, url):
    # TO:DO
    driver.get(url)
    print("Fact Check")

def scrapeCurrElection(driver, url):
    # TO:DO
    driver.get(url)
    print("2024 Election")