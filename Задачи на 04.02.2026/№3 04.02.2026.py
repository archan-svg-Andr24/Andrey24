def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print("I четверть")
    elif xcoord < 0 and ycoord > 0:
        print("II четверть")
    elif xcoord < 0 and ycoord < 0:
        print("III четверть")
    else:
        print("IV четверть")
