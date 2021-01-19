import requests
import datetime
import json

date = datetime.datetime.now()
today = date.day
year = str(date.year)
month = date.month
if month < 10:
    month = "0" + str(month)
# gia kathe mera toy mina mexri ti simerinh
for day in range(1, today + 1):
    if day < 10:
        day = "0"+str(day)
    if day == today:
        temp = datetime.datetime.now()
        hour = temp.hour
        minutes = temp.minute
    urldrawid = f"https://api.opap.gr/draws/v3.0/1100/draw-date/{year}-{month}-{str(day)}/{str(year)}-{month}-{str(day)}/draw-id"
    # briskei ta drawids tis imeras
    response = requests.get(urldrawid)
    drawids = response.json()

    # gia kathe drawid briskei tous tuxerous arithmous kai dimiourgei mia lista me ta plithi tous
    nums = [0] * 80
    for drawid in drawids:
        url = "https://api.opap.gr/draws/v3.0/1100/" + str(drawid)
        response1 = requests.get(url)
        game = response1.json()
        for i in game["winningNumbers"]["list"]:
            nums[i - 1] += 1

    # briskei tous arithmous me tis perissoteres fores a exoun klirwthei
    maxwins = 0
    maxnums = []
    for i in range(len(nums)):
        if nums[i] > maxwins:
            maxwins = nums[i]
            maxnums = [i + 1]
        elif nums[i] == maxwins:
            maxnums.append(i + 1)
    if day != today:
        print(f"Την ημέρα {day}-{month}-{year} ο αριθμός/αριθμοί {maxnums} εμφανίζεται/εμφανίζονται περισσότερες φορές "
              f"και συγκεκριμένα {maxwins} φορές")
    else:
        print(
            f"Την ημέρα {day}-{month}-{year} και έως την ώρα {hour}:{minutes} ο αριθμός/αριθμοί {maxnums}"
            f" εμφανίζεται/εμφανίζονται περισσότερες φορές και συγκεκριμένα {maxwins} φορές")
