from uitestcore.page import BasePage


class BbcWeatherHomePage(BasePage):

    def open(self):
        self.interact.open_url("https://www.bbc.co.uk/weather")
