
import time
import urllib2
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

from src.models.TicketTotals import *
from src.models.Ticket import *

class TableParseHelper:
	def __init__(self,driver):
		self.driver = driver
		self.page = urllib2.urlopen(self.driver.current_url)
		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

		self.ticketTotals = []

	def parseTotals(self):
		for index, tr in enumerate(self.soup.find_all('tr')):
			self.ticketTotals.append(TicketTotals())			

			# Scrape all daily total ticket information
			tdss = tr.find_all('td')						
			tds = []

			for td in tdss:
				if len(td) > 0:
					tds.append(td.text)
		
			# Add information to TicketTotal model
			if len(tds) > 0:		
				self.ticketTotals[index].date = tds[0].strip()
				self.ticketTotals[index].guests = tds[1].strip()
				self.ticketTotals[index].compsTotal = tds[2].strip()
				self.ticketTotals[index].voidsTotal = tds[3].strip()
				self.ticketTotals[index].netsalesTotal = tds[4].strip()
				self.ticketTotals[index].autogratTotal = tds[5].strip()	
				self.ticketTotals[index].taxTotal = tds[6].strip()	
				self.ticketTotals[index].billTotal = tds[7].strip()
				self.ticketTotals[index].paymentTotal = tds[8].strip()
				self.ticketTotals[index].tipsTotal = tds[9].strip()
				self.ticketTotals[index].cashTotal = tds[10].strip()
				self.ticketTotals[index].creditTotal = tds[11].strip()
				self.ticketTotals[index].tendersTotal = tds[12].strip()		
			

	def clickrow(self,className):
		# Giving time for table data to load
		time.sleep(3)

		if className is "collapsed":
			current_row_element = self.driver.find_element_by_xpath(".//*[@id='checks-list']//tbody/tr[@class='day clickable {0}'][{1}]/td[{2}]".format(className,self.rowId,1))
		elif className is "expanded":
			current_row_element = self.driver.find_element_by_xpath(".//*[@id='checks-list']//tbody/tr[@class='day clickable {0}'][{1}]/td[{2}]".format(className,1,1))

		ActionChains(self.driver).move_to_element(current_row_element).click()
		current_row_element.click()

	def parseTickets(self):
		# Giving time for table data to load
		time.sleep(3)

		self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

		for index, tr in enumerate(self.soup.find_all('tr', {"class": "check clickable"})):
			# Scrape unique ticket URL
			ticketUrl = self.extractTicketUrl(tr['data-href'])

			# Scrape all daily total ticket information
			tdss = tr.find_all('td')						
			tds = []

			for td in tdss:
				if len(td) > 0:
					tds.append(td.text.strip())


			# Add information to TicketTotal model
			self.ticketTotals[self.rowId].tickets.append(Ticket())

			if len(tds) > 0:
				self.ticketTotals[self.rowId].tickets[index].url = ticketUrl		
				self.ticketTotals[self.rowId].tickets[index].ticketNumber = tds[1].strip()
				self.ticketTotals[self.rowId].tickets[index].name = tds[2].strip()
				self.ticketTotals[self.rowId].tickets[index].server = tds[3].strip()
				self.ticketTotals[self.rowId].tickets[index].time = tds[4].strip()
				self.ticketTotals[self.rowId].tickets[index].guests = tds[5].strip()
				self.ticketTotals[self.rowId].tickets[index].comps = tds[6].strip()	
				self.ticketTotals[self.rowId].tickets[index].voids = tds[7].strip()	
				self.ticketTotals[self.rowId].tickets[index].netsales = tds[8].strip()
				self.ticketTotals[self.rowId].tickets[index].autograt = tds[9].strip()
				self.ticketTotals[self.rowId].tickets[index].tax = tds[10].strip()
				self.ticketTotals[self.rowId].tickets[index].bill = tds[11].strip()	
				self.ticketTotals[self.rowId].tickets[index].payment = tds[12].strip()
				self.ticketTotals[self.rowId].tickets[index].tips = tds[13].strip()
				self.ticketTotals[self.rowId].tickets[index].cash = tds[14].strip()
				self.ticketTotals[self.rowId].tickets[index].credit = tds[15].strip()
				self.ticketTotals[self.rowId].tickets[index].tenders = tds[16].strip()	


	def getTicketsAndTotals(self):
		return self.ticketTotals

	# Private Methods
	def extractTicketUrl(self, fullUrl):
		return fullUrl[44:]
