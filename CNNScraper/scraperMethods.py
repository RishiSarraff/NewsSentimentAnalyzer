from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from dateFormatter import formatDate
from CNNDB import insert_into_DB

def scrapeCNNSections(driver, url, topicOfInterest):
    driver.get(url)
    pagetopic = ""
    match topicOfInterest:
        case "":
            pagetopic = "General Politics"
        case "supreme-court":
            pagetopic = "SCOTUS"
        case "congress":
            pagetopic = "Congress"
        case "fact-check":
            pagetopic = "Fact Check"
        case "2024":
            pagetopic = "2024 Elections"
        case "europe/ukraine":
            pagetopic = "Ukraine"
        case "middleeast/israel":
            pagetopic = "Isreal"

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
        try:
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
            print(cnnObject)

        except:
            print(link)

        driver.back()