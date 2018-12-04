from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
#<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
browser.get('http://inventwithpython.com')
