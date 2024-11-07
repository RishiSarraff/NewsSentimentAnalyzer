from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import os
from scraperMethods import scrapeSCOTUS, scrapeCongress, scrapeFactCheck, scrapeCurrElection

cnnWebsiteUrl = "https://www.cnn.com/" # website URL

chromeDriverPath = os.getenv("locationOfChromeDriver") # pathway to our chrome driver

chromeService = webdriver.ChromeService(executable_path=chromeDriverPath) # the service for the path based on new syntax

cnnChromeOptions = Options() # lets us add options to disable and add things
cnnChromeOptions.headless = True # we want headless browsing
cnnChromeOptions.add_argument("--disable-javascript") # turn off javascript on screen
cnnChromeOptions.page_load_strategy = 'eager'  # load only the initial HTML

temp_custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
# user agents to help with excessive and quick interaction
cnnChromeOptions.add_argument(f"--user_agent={temp_custom_user_agent}")


driver = webdriver.Chrome(service=chromeService, options=cnnChromeOptions) # create our driver object to pass along

listOfSubURLs = ["politics/supreme-court", "politics/congress", "politics/fact-check", "election/2024"]
# we iterate through each of the 4 suburls of interest and based on the methods we design, we scrape them as necessary
# new comment

for subURL in listOfSubURLs:
    indexOfSlash = subURL.index("/")
    stringOfInterest = subURL[indexOfSlash+1:]
    url = cnnWebsiteUrl + subURL
    match stringOfInterest:
        case 'supreme-court':
            scrapeSCOTUS(driver, url)
        case 'congress':
            scrapeCongress(driver, url)
        case 'fact-check':
            scrapeFactCheck(driver, url)
        case '2024':
            scrapeCurrElection(driver, url)
    # a switch case for our scrapers to redirect them to modularized code.

driver.quit() # we want to end the driver ourselves
