#pace calculator
lenght = input("Vzdialenost v km: \n").replace(',','.')
pace = input("Priemerne tempo behu: \n")
minuty, sekundy = pace.split(':')

vypocetCasu = (int(minuty)*60 + int(sekundy))*float(lenght)
behSekundy = int(vypocetCasu % 60)
behMinuty = int(vypocetCasu // 60)

if behMinuty > 59:
    behHodiny = behMinuty // 60
    behMinutyIf = behMinuty % 60
    print("Cas behu " + str(behHodiny) + "h:" + str(behMinutyIf) + "m:" + str(behSekundy) + "s")
else:
    print("Cas behu " + str(behMinuty) + "m:" + str(behSekundy) + "s")