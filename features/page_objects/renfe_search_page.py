import time


class RenfeSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.from_to_city_input = 'new UiSelector().text("Enter the station name.")'
        self.from_to_city_enabled_input = 'new UiSelector().className("android.widget.EditText")'
        self.calendar_ok_button = 'new UiSelector().text("OK")'
        self.adults_number_picker = 'new UiSelector().className("android.widget.NumberPicker").childSelector(className("android.widget.EditText"))'
        self.leave_date_element = 'new UiSelector().resourceId("com.renfe.wsm:id/editTextCompuest").instance(2)'
        self.submit_button = 'Continuar'

    def search_for(self, from_city, to_city, adults, leave_date):
        self.driver.find_element_by_android_uiautomator(self.from_to_city_input).click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.from_to_city_enabled_input).send_keys(from_city)
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("' +from_city+ '").instance(1)').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.from_to_city_input).click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.from_to_city_enabled_input).send_keys(to_city)
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("' +to_city+ '").instance(1)').click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.adults_number_picker).send_keys(adults)
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.leave_date_element).click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(leave_date).click()
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator(self.calendar_ok_button).click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id(self.submit_button).click()
        time.sleep(2)