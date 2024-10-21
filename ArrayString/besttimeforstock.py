prices = [7,1,5,3,6,4]

min_price=float('inf')
max_prof=0


for price in prices:
    if price<min_price:
        min_price=price

    profit = price -min_price

    if profit > max_prof:
        max_prof = profit

print(max_prof)