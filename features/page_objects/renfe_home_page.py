import time


class RenfeHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.timetable_button = ' timetable / purchase item'

    def click_on_timetable(self):
        self.driver.find_element_by_accessibility_id(self.timetable_button).click()
        time.sleep(2)