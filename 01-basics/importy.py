import datetime
def casTed():
    x = datetime.datetime.now()
    print('Aktualni datum a cas je: ', x)
casTed()

def eastern():
    year = 2021







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