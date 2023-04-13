from datetime import datetime, date
dnesnyDatum = date.today()
denVroku = int(datetime.now().timetuple().tm_yday)
meniny = open('meninyVroku', 'r')
meninyDnesMa = meniny.readlines()
print(meninyDnesMa[denVroku -1])
meniny.close()
