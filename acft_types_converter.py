import csv
import time
import datetime

today = datetime.datetime.now()
todayYear = today.strftime("%Y")
todayMonth = today.strftime("%m")
todayDay = today.strftime("%d")

unfilteredAcftTypes = []

print(f"Processing file acft_afps_{todayYear}-{todayMonth}-{todayDay}")
time.sleep(2)

with open(f"acft_afps_{todayYear}-{todayMonth}-{todayDay}.csv") as csvFile:
    acftTypes = csv.reader(csvFile, delimiter=',')
    next(csvFile)
    for row in acftTypes:
        unfilteredAcftTypes.append(row[0])

filteredAcftTypes = set(unfilteredAcftTypes)

print(f"Found {len(unfilteredAcftTypes)} ACFT Types")
time.sleep(2)
print(f"Filtered out {len(unfilteredAcftTypes)-len(filteredAcftTypes)} duplicate ACFT Types,")
print(f"{len(filteredAcftTypes)} ACFT Types remaining.")
time.sleep(2)
print(f"Writing Java ready String Array to acft_afps_{todayYear}-{todayMonth}-{todayDay}.txt")

with open(f"acft_afps_{todayYear}-{todayMonth}-{todayDay}.txt", "w") as txtFile:
    count = 0
    for acftType in filteredAcftTypes:
        if acftType == list(filteredAcftTypes)[-1]:
            txtFile.write(f"\"{acftType}\"")
        else:
            txtFile.write(f"\"{acftType}\", ")
        count += 1
        if count == 9:
            txtFile.write("\n")
            count = 0
            
time.sleep(2)
print(f"Successfully created acft_afps_{todayYear}-{todayMonth}-{todayDay}.txt with {len(filteredAcftTypes)} ACFT Types")
input("Press any key to exit")
