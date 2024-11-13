from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os
from scraperMethods import scrapePoliticsFOXSections, scrapeCongressFOXSections, scrapeNewsletterFOXSections


foxWebsiteUrl = "https://www.foxnews.com/" # website URL

chromeDriverPath = os.getenv("locationOfChromeDriver") # pathway to our chrome driver

chromeService = webdriver.ChromeService(executable_path=chromeDriverPath) # the service for the path based on new syntax

foxChromeOptions = Options() # lets us add options to disable and add things
foxChromeOptions.headless = True # we want headless browsing
foxChromeOptions.add_argument("--disable-javascript") # turn off javascript on screen
foxChromeOptions.page_load_strategy = 'eager'# load only the initial HTML
foxChromeOptions.add_experimental_option("detach", True)


temp_custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# user agents to help with excessive and quick interaction
foxChromeOptions.add_argument(f"--user_agent={temp_custom_user_agent}")


driver = webdriver.Chrome(service=chromeService, options=foxChromeOptions) # create our driver object to pass along

listOfSubURLs = ["politics/", "category/us/congress/", "category/columns/elections-newsletter"]
# we iterate through each of the 7 suburls of interest and based on the methods we design, we scrape them as necessary
# new comment

for subURL in listOfSubURLs:
    indexOfSlash = subURL.index("/")
    stringOfInterest = subURL[indexOfSlash+1:]
    url = foxWebsiteUrl + subURL

    match stringOfInterest:
        case "":
            scrapePoliticsFOXSections(driver, url)
        case "us/congress/":
            scrapeCongressFOXSections(driver, url)
        case "columns/elections-newsletter":
            scrapeNewsletterFOXSections(driver, url)

driver.quit() # we want to end the driver ourselves