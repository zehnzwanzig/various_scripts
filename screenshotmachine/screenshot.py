import datetime
import urllib.request
link = "http://api.screenshotmachine.com/?key=INSERTYOURKEYHERE&dimension=1920xfull&device=desktop&cacheLimit=0&delay=500&format=png&&url=https://www.coingecko.com/de/kurs_chart/zcash/eur"
local_file = './screenshots/' + '{0:%Y-%m-%d}'.format(datetime.datetime.now()) + ".png"
urllib.request.urlretrieve(link, local_file)		#Download screenshot and save it