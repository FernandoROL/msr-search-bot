import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BingSearcher:
    @staticmethod
    def search(driver, query):
        driver.get('https://www.bing.com')
        time.sleep(random.uniform(1.5, 4.5))
        try:
            driver.execute_script(f"window.scrollTo(0, {random.randint(0, 400)});")
            time.sleep(random.uniform(0.2, 0.7))
        except Exception:
            pass

        search_box = driver.find_element(By.NAME, 'q')
        for char in query:
            search_box.send_keys(char)
            if random.random() > 0.7:
                driver.execute_script(f"window.scrollTo(0, {random.randint(0, 400)});")
            time.sleep(random.uniform(0.05,0.25))

        if random.random() > 0.5:
            time.sleep(random.uniform(0.2,0.7))

        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(2.5, 6.5))

        if random.random() > 0.5:
            try:
                driver.execute_script(f"window.scrollTo(0, {random.randint(400, 1200)});")
                time.sleep(random.uniform(0.5, 1.5))
            except Exception:
                pass
