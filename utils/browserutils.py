from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, requests, random, threading




class BrowserPool:
    def __init__(self, max_browsers):
        self.max_browsers = max_browsers
        self.browsers = threading.BoundedSemaphore(max_browsers)
        self.browser_queue = []
        for n in range(max_browsers):
            self.browser_queue.append(self.start_browser())
    
        
    def get_browser(self):
        self.browsers.acquire()
        browser = self.browser_queue.pop(0)
        return browser
    
    
    def release_browser(self, browser):
        self.browser_queue.append(browser)
        self.browsers.release()
        


    def user_agent(self):
        user_agent_list = [
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 OPR/85.0.4341.71',
                'Mozilla/5.0 (Windows; U; Windows NT 5.2; es-VE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36 UCBrowser/13.4.0.1306',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Safari/537.36 Edg/104.0.1293.70',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4476.0 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Safari/537.36 OPR/91.0.4516.78',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42',
                
        ]
        user_agent = random.choice(user_agent_list)
        return user_agent



    def petition(self, url, headers=False, execute_js=False):
        
        browser = self.get_browser()
        
        if headers and headers != {}:
            browser.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': headers})
            
            
        try:
            
            browser.get(url)

            while "<title>Just a moment...</title>" in browser.page_source:
                time.sleep(1)
                print("Cloudflare waiting "+url)
        

            content = browser.page_source
        
            wait = WebDriverWait(browser, 10)
            wait.until(lambda browser: browser.execute_script("return document.readyState === 'complete' || document.readyState === 'interactive';"))
            
            if browser.page_source == content:
                print("Complete repeats on "+url+", waiting 5s")
                time.sleep(5)

            js_result = False
            if execute_js:
                js_result = browser.execute_script(execute_js)

            
            content = browser.page_source
            
            self.release_browser(browser)   
                    
            return content, js_result
            
        except Exception as error:
            self.release_browser(browser)
        
            print("browser failed on "+url)
            print(error)
            return False, False





    def start_browser(self):
        # Configure the browser options to run headless
        options = ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-accelerated-2d-canvas')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--user-agent='+self.user_agent())
        
 
                    
        # Create a new instance of the Chrome driver with the configured options
        browser = Chrome(options=options)
        
        return browser
