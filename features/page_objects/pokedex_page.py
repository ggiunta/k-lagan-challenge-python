from selenium.webdriver.common.keys import Keys


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class PokedexPage(BasePage):
    def navigate_to(self):
        self.driver.get("https://www.pokemon.com/us/pokedex")

    def search_for(self, pokemon):
        element = self.driver.find_element_by_id('searchInput')
        element.send_keys(pokemon)
        element.send_keys(Keys.RETURN)

    def select_result(self, name):
        element = self.driver.find_element_by_xpath("//ul[@class='results']/li[div/h5[text()='"+ name +"']]")
        element.click()

class PokedexDetailsPage(BasePage):
    def get_name(self):
        element = self.driver.find_element_by_xpath("//div[@class='pokedex-pokemon-pagination-title']/div")
        return element.text

    def get_weaknesses(self):
        weaknesses = []
        elements = self.driver.find_elements_by_xpath("//div[@class='dtm-weaknesses']/ul/li")
        for element in elements:
            weaknesses.append(element.text)
        return weaknesses