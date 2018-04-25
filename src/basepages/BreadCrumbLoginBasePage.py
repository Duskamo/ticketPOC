
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from src.basepages.BreadCrumbHomeBasePage import *

class BreadCrumbLoginBasePage:
	def __init__(self):
		""

	def open(self, base_url):
		firefoxOptions = Options()
        	firefoxOptions.add_argument("--headless")
        	self.driver = webdriver.Firefox(options=firefoxOptions,executable_path='/usr/local/bin/geckodriver')
        	self.driver.maximize_window()
	        self.driver.get(base_url)

	def login(self, username, password):
		print("URL: {}".format(self.driver.current_url))

		# Enter Username and Password and Submit
		emailTextbox = self.driver.find_element_by_id("email")
		passwordTextbox = self.driver.find_element_by_id("password")
		loginButton = self.driver.find_element_by_name("commit")		
		emailTextbox.send_keys(username)
		passwordTextbox.send_keys(password)
		loginButton.click()
		
		# Navigate to Home Page
		breadCrumbHomeBasePage = BreadCrumbHomeBasePage()
		breadCrumbHomeBasePage.driver = self.driver

		return breadCrumbHomeBasePage


