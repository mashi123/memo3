import os

from optparse import OptionParser
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--enable-javascript")

def make_screenshot(url, output):

    driver = webdriver.Remote(
        command_executor = 'http://selenium:4444/wd/hub',
        options=chrome_options,
    )

    try:
        driver.get(url)
        driver.save_screenshot(output)
    except Exception as e:
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    usage = "usage: %prog [options] <url> <output>"
    parser = OptionParser(usage=usage)

    (options, args) = parser.parse_args()

    if len(args) < 2:
        parser.error("please specify a URL and an output")

    print(args)
    make_screenshot(args[0], args[1])
