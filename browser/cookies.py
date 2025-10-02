import json
import os
import random
import time

class CookieManager:
    @staticmethod
    def load_bing_cookies(driver, cookies_path='cookies.json'):
        driver.get('https://www.bing.com')
        if os.path.exists(cookies_path):
            with open(cookies_path, 'r') as f:
                cookies = json.load(f)
            random.shuffle(cookies)
            for cookie in cookies:
                if 'expiry' in cookie:
                    cookie['expiry'] = int(cookie['expiry'])
                try:
                    time.sleep(random.uniform(0.05,0.2))
                    driver.add_cookie(cookie)
                except Exception:
                    time.sleep(random.uniform(0.05,0.2))
                    pass
            driver.refresh()
            time.sleep(random.uniform(1.5, 3.5))
        else:
            print(f"Cookie file {cookies_path} not found.")
