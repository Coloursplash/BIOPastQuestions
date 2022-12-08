# fullm marks

firstFast, secondFast = input().split(" ")
firstFast = int(firstFast)
secondFast = int(secondFast)

firstMin = 0
secondMin = 0
realMin = 0


def mins_format(mins):
    hours = 0
    while mins >= 60:
        mins -= 60
        hours += 1
    while hours >= 24:
        hours -= 24
    return str(hours).rjust(2, "0") + ":" + str(mins).rjust(2, "0")


while True:
    realMin += 1
    firstMin += 1
    secondMin += 1
    if realMin % 60 == 0:
        firstMin += firstFast
        secondMin += secondFast

        if mins_format(firstMin) == mins_format(secondMin):
            print(mins_format(firstMin))
            break


# part B
# 0 8 9 16 18
