import random
import time
from phrases.generator import PhraseGenerator
from browser.driver import BrowserFactory
from browser.cookies import CookieManager
from browser.search import BingSearcher

def main():
    try:
        num_searches = int(input("How many times would you like to search? "))
    except Exception:
        num_searches = 10

    driver = BrowserFactory.create_driver()
    CookieManager.load_bing_cookies(driver)

    generator = PhraseGenerator()

    for _ in range(num_searches):
        phrase = generator.generate_short_phrases(1)[0]
        BingSearcher.search(driver, phrase)
        if random.random() > 0.3:
            time.sleep(random.uniform(3, 7))
        else:
            time.sleep(random.uniform(7, 12))
        if random.random() > 0.8:
            driver.refresh()
            time.sleep(random.uniform(1,3))

    driver.quit()

if __name__ == '__main__':
    main()
