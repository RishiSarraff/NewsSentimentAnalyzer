from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from dateFormatter import formatDate
from FoxDB import insert_into_DB


def articleProcessing(driver, linkSet, pagetopic):
    count = 1
    for link in linkSet:
        try:
            driver.get(link)

            title = driver.find_element(By.CLASS_NAME, "headline").text

            try:
                authorDiv = driver.find_element(By.CLASS_NAME, "author-byline")
                authorName = authorDiv.find_element(By.TAG_NAME, "a").text
            except NoSuchElementException:
                authorName = "Unknown"

            pageContent = driver.find_element(By.CLASS_NAME, "article-body")

            listOfSpeakables = pageContent.find_elements(By.TAG_NAME, "p")

            text = ""

            for innerText in listOfSpeakables:
                text += innerText.text + " "


            try:
                articleDateDiv = driver.find_element(By.CLASS_NAME, "article-date")
                articleDateTime = articleDateDiv.find_element(By.TAG_NAME, "time").text
            except:
                articleDateTime= "   "

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

    articleProcessing(driver, linkSet, pagetopic)


def click_on_load_more(driver, num_clicks=20):
    for i in range(num_clicks):
        try:
            loadMore_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "load-more"))
            )
            loadMore_button.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(e)
            break

        except Exception as e:
            time.sleep(3)


def scrapeCongressFOXSections(driver, url):
    driver.get(url)
    pagetopic = "Congress"
    # before we get into it, I want to simulate clicking the Show More button 20 times
    click_on_load_more(driver, 20)

    articleList = driver.find_elements(By.CLASS_NAME, "article")

    linkSet = set()

    for article in articleList:
        try:
            linkDiv = article.find_element(By.CLASS_NAME, "m")
            link = linkDiv.find_element(By.TAG_NAME, "a").get_attribute("href")

            if "video" not in link:
                linkSet.add(link)
        except:
            print(article)

    for link in linkSet:
        print(link)

    articleProcessing(driver, linkSet, pagetopic)


def scrapeNewsletterFOXSections(driver, url):
    driver.get(url)

    pagetopic = "Newsletter"
    # before we get into it, I want to simulate clicking the Show More button 20 times
    click_on_load_more(driver, 20)

    articleList = driver.find_elements(By.CLASS_NAME, "article")

    linkSet = set()

    for article in articleList:
        try:
            linkDiv = article.find_element(By.CLASS_NAME, "m")
            link = linkDiv.find_element(By.TAG_NAME, "a").get_attribute("href")

            if "video" not in link:
                linkSet.add(link)
        except:
            print(article)

    for link in linkSet:
        print(link)

    articleProcessing(driver, linkSet, pagetopic)


