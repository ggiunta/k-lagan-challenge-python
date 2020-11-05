from appium import webdriver
import time
from page_objects.renfe_search_page import *
from page_objects.renfe_home_page import *
from page_objects.renfe_timetable_page import *


@given('I make a booking')
def step_impl(context):

    desired_caps = dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Nexus 5 API 30',
        appPackage='com.renfe.wsm',
        appActivity='ticket.ui.splash.SplashActivity'
    )
    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    time.sleep(2)

    renfe_home_page = RenfeHomePage(driver)
    renfe_home_page.click_on_timetable()

    renfe_timetable_page = RenfeTimetablePage(driver)
    renfe_timetable_page.click_on_timetable()

    ticket_search_page = RenfeSearchPage(driver)
    ticket_search_page.search_for('Barcelona (Todas)', 'Madrid (Todas)', 2, '20 November 2020')

    time.sleep(15)#Enough time to allow people to see the results
    driver.quit()