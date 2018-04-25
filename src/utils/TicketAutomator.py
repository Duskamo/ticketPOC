
from Config import *
from src.basepages.BreadCrumbLoginBasePage import *

class TicketAutomator:
	def __init__(self):
		""

	def setup(self):
		print("Automation setup code...")

	def automate(self):
		print("Automation primary code...")

		breadCrumbLoginBasePage = BreadCrumbLoginBasePage()
		breadCrumbLoginBasePage.open(base_url)
		breadCrumbHomeBasePage = breadCrumbLoginBasePage.login(username,password)
		
		breadCrumbTicketInfoBasePage = breadCrumbHomeBasePage.gotoTicketInfoBasePage(template_url)
		breadCrumbTicketInfoBasePage.gatherTicketInformation()
