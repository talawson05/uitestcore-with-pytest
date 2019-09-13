from uitestcore.utilities.logger import Logger

from instantiate_driver import InstantiateDriver
from test.bbc_weather.bbc_weather_home_page import BbcWeatherHomePage


def test_open_bbc_weather():
    #path based on executing from root
    driver = InstantiateDriver().chrome("./resources/drivers/chromedriver.exe")
    home_page = BbcWeatherHomePage(driver, Logger().init_logger())
    home_page.open()
