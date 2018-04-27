
import csv

class CSVHelper:
	def __init__(self,ticketTotals,restaurant):
		self.ticketTotals = ticketTotals
		self.restaurant = restaurant

	def writeToFile(self,exportDirectory):	
		with open("{0}{1}_ticket_info.csv".format(exportDirectory,self.restaurant), 'wb') as csvfile:
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
					ticketwriter.writerow([ticket.url,
							ticket.ticketNumber,
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

				
