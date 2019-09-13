from selenium import webdriver


class InstantiateDriver:

    def chrome(self, path_to_driver_binary):
        return webdriver.Chrome(executable_path=path_to_driver_binary)
