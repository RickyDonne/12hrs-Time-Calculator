def add_time(start, duration, day=""):

    start = start.split()

    time = start[0].split(":")
    HH = time[0]
    MM = time[1]

    AP = start[1]

    duration = duration.split(":")
    dHH = duration[0]
    dMM = duration[1]

    fHH = fMM = fAP = n = 0

    fMM = int(MM) + int(dMM)
    if fMM > 60:
        fMM -= 60
        fHH += 1

    if fMM < 10:
        fMM = str("0" + str(fMM))

    # print(fMM)

    fHH += int(HH) + int(dHH)
    # print(fHH)
    if fHH >= 24:
        count = fHH//24
        n += count
        extra = count * 24
        fHH -= extra

    if fHH >= 12:
        if AP == "AM":
            AP = "PM"
        else:
            AP = "AM"
            n += 1

    if fHH < 24 and fHH > 12:
        fHH -= 12

    list_days = ['Sunday', 'Monday', 'Tuesday',
                 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if (day != ""):
        day = day.lower()
        day = day[0].upper() + day[1:]
        index = list_days.index(day)
        findex = list_days[(index + n) % 7]
        # print(findex)

    numd = ""

    if (n == 1):
        numd = "(next day)"

    if (n > 1):
        numd = f"({n} days later)"

    # print(str(fHH) + ":" + str(fMM) + " " + AP)
    # print(numd)

    if day == "":
        if n == 0:
            return f"{fHH}:{fMM} {AP}"
        else:
            return f"{fHH}:{fMM} {AP} {numd}"
    else:
        if n == 0:
            return f"{fHH}:{fMM} {AP}, {findex}"
        else:
            return f"{fHH}:{fMM} {AP}, {findex} {numd}"
