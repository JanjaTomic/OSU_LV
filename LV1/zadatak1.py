def total_euro(hours, rate):
    total = hours * rate
    return total

hours = float(input("Radni sati: "))
rate = float(input("Stanica: "))

total = total_euro(hours, rate)
print("Ukupno:", total, "eura")