Requirements:

Python >= 3.x.x (Getestet mit Python 3.6.4)
xhtml2pdf | Installieren via 'pip install xhtml2pdf'
requests | Installieren via 'pip install requests'

Das Script loggt sich mit OnlyRead-Rechten in die Finanzen ein, zieht den HTM-Code, übergibt ihn an xhtml2pdf und dieses rendert eine Seite zusammen und speichert sie als pdf.
Der Ordner 'processed' ist notwendig, sonst schmeißt das Script die pdfs in den selben Ordner und das ist doch eher unübersichtlich.

Mögliche TO-DO's: 

* CSS miteinbinden, weil das ganze Ding noch etwas hässlich ist :-)
* Statt dem aktuellen Try-Except-Block ne If-Else-Anweisung und dann richtige Try-Except-Blöcke setzen, damit die Exceptions richtig gehandhabt werden.
* Die Request-Abläufe in ne eigene Funktion packen

~~~zehnzwanzig