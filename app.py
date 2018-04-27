
from Config import *
from src.utils.TicketAutomator import *
from src.utils.CSVHelper import *

ticketAutomator = TicketAutomator()
ticketAutomator.setup()
ticketAutomator.automate()

ticketTotals = ticketAutomator.getTicketsAndTotals()

csvHelper = CSVHelper(ticketTotals,restaurants[0])
csvHelper.writeToFile(exportDirectory)


