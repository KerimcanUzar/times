#Times
Play = True
while Play:
    t1 = int(input("\n1.Milisecond\n2.Second\n3.Minute\n4.Hour\n5.Day\n6.Week\n7.Month\n8.Year\n9.Century\n10.Millennium\n\nChoose first time: "))
    t2 = int(input("\n1.Milisecond\n2.Second\n3.Minute\n4.Hour\n5.Day\n6.Week\n7.Month\n8.Year\n9.Century\n10.Millennium\n\nChoose second time: "))
    x = int(input("\nHow many? "))
    ms=1
    sec=ms*100
    mins=sec*60
    hour=mins*60
    day=hour*24
    week=day*7
    month=day*30
    year=day*365.25
    century=year*100
    millennium=century*10
    if t1 == 1:
        arg1 = "miliseconds"
        t1 = ms
    if t1 == 2:
        arg1 = "seconds"
        t1 = sec
    if t1 == 3:
        arg1 = "minutes"
        t1 = mins
    if t1 == 4:
        arg1 = "hours"
        t1 = hour
    if t1 == 5:
        arg1 = "days"
        t1 = day
    if t1 == 6:
        arg1 = "weeks"
        t1 = week
    if t1 == 7:
        arg1 = "months"
        t1 = month
    if t1 == 8:
        arg1 = "years"
        t1 = year
    if t1 == 9:
        arg1 = "centuries"
        t1 = century
    if t1 == 10:
        arg1 = "millenniums"
        t1 = millennium
    if t2 == 1:
        arg2 = "miliseconds"
        t2 = ms
    if t2 == 2:
        arg2 = "seconds"
        t2 = sec
    if t2 == 3:
        arg2 = "minutes"
        t2 = mins
    if t2 == 4:
        arg2 = "hours"
        t2 = hour
    if t2 == 5:
        arg2 = "days"
        t2 = day
    if t2 == 6:
        arg2 = "weeks"
        t2 = week
    if t2 == 7:
        arg2 = "months"
        t2 = month
    if t2 == 8:
        arg2 = "years"
        t2 = year
    if t2 == 9:
        arg2 = "centuries"
        t2 = century
    if t2 == 10:
        arg2 = "millenniums"
        t2 = millennium
    result = x*t2/t1
    print ("There is", result, arg1, "in", x, arg2,".\n")
    response = input("Do you want to play again? [y/n]\n")
    if response == "n":
        Play = False
