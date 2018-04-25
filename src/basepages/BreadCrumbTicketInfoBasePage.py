
import time
import urllib2
from bs4 import BeautifulSoup

class BreadCrumbTicketInfoBasePage:
	def __init__(self):
		""

	def gatherTicketInformation(self):
		print("URL: " + self.driver.current_url)
		
		time.sleep(20)	
		b = self.driver.find_element_by_id("checks-list")
		dateRows = self.driver.find_elements_by_xpath(".//*[@id='checks-list']//tbody/tr")

		dateRowCount = len(dateRows)
			
		page = urllib2.urlopen(self.driver.current_url)
		soup = BeautifulSoup(page, 'html.parser')

		for tr in soup.find_all('tr')[2:]:
			tds = tr.find_all('td')
			print(tds[0].text)
			print(tds[1].text)
			print(tds[2].text)

		"""
		for rowId in range(dateRowCount):
			current_row = self.driver.find_element_by_xpath(".//*[@id='checks-list']//tbody/tr[{0}]".format(rowId+1))
			#current_row.click()
		"""
			

			
			
		
		 
