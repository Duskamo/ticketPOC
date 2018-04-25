
from src.basepages.BreadCrumbTicketInfoBasePage import *

class BreadCrumbHomeBasePage:
	def __init__(self):
		""

	def gotoTicketInfoBasePage(self,ticketInfoPage):
		self.driver.get(ticketInfoPage)

		breadCrumbTicketInfoBasePage = BreadCrumbTicketInfoBasePage()
		breadCrumbTicketInfoBasePage.driver = self.driver
		return breadCrumbTicketInfoBasePage
