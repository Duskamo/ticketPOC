
import csv

class CSVHelper:
	def __init__(self,ticketTotals):
		self.ticketTotals = ticketTotals

	def writeToFile(self,outputFile):	
		with open(outputFile, 'wb') as csvfile:
			ticketwriter = csv.writer(csvfile, delimiter=',')

			for ticketAndTotal in self.ticketTotals:
				# Write ticket daily totals
				"""
				ticketwriter.writerow([ticketAndTotal.date,
							str(ticketAndTotal.guests),
							ticketAndTotal.compsTotal,
							ticketAndTotal.voidsTotal,
							ticketAndTotal.netsalesTotal,
							ticketAndTotal.autogratTotal,
							ticketAndTotal.taxTotal,
							ticketAndTotal.billTotal,
							ticketAndTotal.paymentTotal,
							ticketAndTotal.tipsTotal,
							ticketAndTotal.cashTotal, 
							ticketAndTotal.creditTotal, 
							ticketAndTotal.tendersTotal]
						)
				"""

				for ticket in ticketAndTotal.tickets:
					# Write individual ticket information
					ticketwriter.writerow([ticket.ticketNumber,
							str(ticket.name),
							ticket.server,
							ticket.time,
							ticket.guests,
							ticket.comps,
							ticket.voids,
							ticket.netsales,
							ticket.autograt,
							ticket.tax,
							ticket.bill, 
							ticket.payment, 
							ticket.tips,
							ticket.cash,
							ticket.credit,
							ticket.tenders]
						)				

				
