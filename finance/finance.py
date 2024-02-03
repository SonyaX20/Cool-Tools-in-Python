import os
from datetime import date

path = "finance.txt"
today = date.today()
month_day = today.strftime("%m.%d")
product = input("product:")
if product == "total":
    with open(path,'r') as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        day_read,price_read = line.split("\t")[0],float(line.split("\t")[2][:-2])
        if day_read==month_day:
            total += price_read
    line = f"{month_day}\t\t{total}€\n"
    with open(path,'a') as f:
        f.write(line)
else:
    price = input("price:")+"€"
    line = month_day+"\t"+product+"\t"+price+"\n"
    with open(path,'a') as f:
        f.write(line)
