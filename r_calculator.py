#running pace calculator

while True:
    print("1. priemerne tempo behu")
    print("2. cas behu")
    print("3. ukoncit program")
    userInput = int(input())
    if userInput == 1:
        lenght = input("Zadaj vzdialenost v km: \n").replace(',', '.')
        time = input("Zadaj cas behu: \n")
        if time.count(':') == 2:
            hodiny, minuty, sekundy = time.split(':')
        else:
            hodiny = 0
            minuty, sekundy = time.split(':')
        totalSec = (int(hodiny) * 3600) + (int(minuty) * 60) + int(sekundy)
        secPerKm = float(totalSec) / float(lenght)
        paceMin = int(secPerKm // 60)
        paceSec = int(secPerKm % 60)
        print("Priemerne tempo behu " + str(paceMin) + ":" + str(paceSec)+" \n")

    elif userInput == 2:
        lenght = input("Vzdialenost v km: \n").replace(',', '.')
        pace = input("Priemerne tempo behu: \n")
        minuty, sekundy = pace.split(':')
        vypocetCasu = (int(minuty)*60 + int(sekundy))*float(lenght)
        behSekundy = int(vypocetCasu % 60)
        behMinuty = int(vypocetCasu // 60)
        if behMinuty > 59:
            behHodiny = behMinuty // 60
            behMinutyIf = behMinuty % 60
            print("Cas behu " + str(behHodiny) + "h:" + str(behMinutyIf) + "m:" + str(behSekundy) + "s \n")
        else:
            print("Cas behu " + str(behMinuty) + "m:" + str(behSekundy) + "s \n")
    elif userInput == 3:
        quit()
    else:
        continue