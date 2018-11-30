from xhtml2pdf import pisa
import requests
import datetime

s = requests.Session()																															
s.get('https://finanzen.piratenpartei.at/index.php?action=login')																				# Cookie abholen
s.post('https://finanzen.piratenpartei.at/index.php?action=login', data={'name': 'USERNAME', 'pass' : 'PASSWORD', 'submit': 'Anmeldung'})		# Login mit payload (name, pass, submit)
r = s.get('https://finanzen.piratenpartei.at/index.php?action=mb')																				# Mitgliederstatistik reinladen
sourceHtml = r.content																															# Den ganzen HTM-Code in nen String																								
outputFilename = './processed/' + '{0:%Y-%m-%d}'.format(datetime.datetime.now()) + ".pdf"														# Ausgabename der Datei

def convertHtmlToPdf(sourceHtml, outputFilename):																								# Funktion mit 2 Argumenten (String für HTM-Code und Dateiname für Output)
	
	try:																																		# Datei öffnen
		resultFile = open(outputFilename, "w+b")																								
	except:																																		# Wurde der Ordner 'processed' nicht gefunden, wird die pdf-File im Stammordner abgelegt
		outputFilename = '{0:%Y-%m-%d}'.format(datetime.datetime.now()) + ".pdf"
		resultFile = open(outputFilename, "w+b")
	pisaStatus = pisa.CreatePDF(																												# PDF erstellen
		sourceHtml,                
		dest=resultFile)           
	resultFile.close() 																															# Datei schließen                
	return pisaStatus.err																														# true wenn alles passt, return false bei Fehler

if __name__ == "__main__":																														# Hauptprogramm
    pisa.showLogging()
    convertHtmlToPdf(sourceHtml, outputFilename)																								# Funktionsaufruf