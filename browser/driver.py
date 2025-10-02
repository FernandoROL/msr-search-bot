import random
import undetected_chromedriver as uc

class BrowserFactory:
    @staticmethod
    def create_driver():
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) "
            "Gecko/20100101 Firefox/117.0"
        ]
        width = random.randint(900, 1366)
        height = random.randint(540, 768)
        options = uc.ChromeOptions()
        options.add_argument(f'--user-agent={random.choice(user_agents)}')
        options.add_argument(f'--window-size={width},{height}')
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        return uc.Chrome(options=options)
