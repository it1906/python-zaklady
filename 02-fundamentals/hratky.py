import module
import math

module.vzdalenost
module.hmotnost
print("***********************************")
if module.svetlo > 3600:
    print("Svetlo dorazi za (hodin) ", round(module.svetlo/3600,2))
elif module.svetlo <60:
    print("Svetlo dorazi za (sekund) ", round(module.svetlo,2))
else:
    print("Svetlo dorazi za (minut) ",round(module.svetlo/60,2))
if module.zvuk > 3600:
    module.zvuk/3600
    print("Zvuk dorazi za(hodin) ", round(module.zvuk/3600,2))
elif module.zvuk < 60:
    print("Zvuk dorazi za (sekund) ", round(module.zvuk, 2))
else:
    print("Zvuk dorazi za (minut) ",round(module.zvuk/60,2))
print("***********************************")
print("Vase hmotnost na mesici bude (kg): ", round(module.vaha,1))
print("***********************************")
print("Vase celkova energie je (TJ): ", round(((module.SPEED_OF_LIGHT*1000)*(module.SPEED_OF_LIGHT*1000)*module.hmotnost)/1000000000,2))
print("Pro porovnani, atomova bomba, ktera znicila Nagasaki mela priblizne 60 TJ")







"""
print("********************************************")
print("Vypocet rychlosti zvuku a svetla v minutach.")
print("Svetlo dorazi za ",round(module.svetlo/60,2))
print("Zvuk dorazi za ",round(module.zvuk/60,2))
print("********************************************")
print("Vypocet rychlosti zvuku a svetla v sekundach.")
print("Svetlo dorazi za ",round(module.svetlo,2))
print("Zvuk dorazi za ",round(module.zvuk,2))
print("********************************************")
"""