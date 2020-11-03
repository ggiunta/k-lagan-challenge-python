from appium import webdriver


@given('I make a booking')
def step_impl(context):
    print('Renfe')

    desired_caps = dict(
        platformName='iOS',
        platformVersion='14.1',
        automationName='xcuitest',
        deviceName='iPhone Simulator',
        #app=PATH('../../apps/UICatalog.app.zip')
    )
    
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.quit()