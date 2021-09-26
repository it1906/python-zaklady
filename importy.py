import datetime
from dateutil.relativedelta import *
from dateutil.easter import *
print("\n")
print("UKOL 1: DATUM A CAS")
def casTed():
    x = datetime.datetime.now()
    print('Aktualni datum a cas je: ', x)
casTed()
print("\n")
print("UKOL 2: VELIKONOCE")
def eastern():
    year = 2021
    now = datetime.datetime.now()
    today = now.date()
    for i in range(1, 6):
        rdelta = relativedelta(easter(year + i), today)
        print("Velikonocni nedele: %s" % (today + rdelta))
eastern()
print("\n")
print("UKOL 3: VANOCE")
def xmas():
    year = 2021
    vanoce = datetime.date(year, 12, 24)
    y = vanoce.strftime("%A")
    while y != 'Sunday':
        year = year+1
        vanoce = datetime.date(year, 12, 24)
        y = vanoce.strftime("%A")
    if y == 'Sunday':
        print('Vanoce budou v nedeli v roce: ', year)
xmas()