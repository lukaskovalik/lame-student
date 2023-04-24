#pace calculator
lenght = input("Vzdialenost v km: \n").replace(',','.')
pace = input("Priemerne tempo behu: \n")
minuty, sekundy = pace.split(':')
vypocetCasu = (int(minuty)*60 + int(sekundy))*float(lenght)
behMinuty = int(vypocetCasu // 60)
behSekundy = int(vypocetCasu % 60)
print("Cas behu " + str(behMinuty) + "m:" + str(behSekundy) + "s")