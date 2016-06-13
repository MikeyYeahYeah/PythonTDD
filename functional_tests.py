from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = '/usr/local/bin/wires'

driver = webdriver.Firefox(capabilities=firefox_capabilities)
driver.get('http://localhost:8000')

assert 'Django' in driver.title
