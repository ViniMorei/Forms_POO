from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

class FormBase:
    def __init__(self):
        self.__bot = WebBot()
        self.__bot.browser = Browser.CHROME
        self.__bot.driver_path = ChromeDriverManager().install()
    
    
    @property
    def bot(self):
        return self.__bot