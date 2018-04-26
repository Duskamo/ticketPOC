
import time
from src.utils.TableParseHelper import *

class BreadCrumbTicketInfoBasePage:
	def __init__(self):
		""

	def gatherTicketInformation(self):
		print("URL: " + self.driver.current_url)
		
		# Wait for data to load and calculate number of groups (by date) in the table
		time.sleep(10)	
		b = self.driver.find_element_by_id("checks-list")
		dateRows = self.driver.find_elements_by_xpath(".//*[@id='checks-list']//tbody/tr")
		dateRowCount = len(dateRows)

		# Parse daily totals and individual ticket information
		self.tableParseHelper = TableParseHelper(self.driver)
		self.tableParseHelper.parseTotals()

		for rowId in range(dateRowCount):
			self.tableParseHelper.rowId = rowId + 1
			self.tableParseHelper.clickrow("collapsed")
			self.tableParseHelper.parseTickets()
			self.tableParseHelper.clickrow("expanded")

	def getTicketsAndTotals(self):
		return self.tableParseHelper.getTicketsAndTotals()


					

			
			
		
		 
