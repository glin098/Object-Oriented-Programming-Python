cases = int(input())
count = []

for x in range(cases):
    cities = int(input())
    cityList = []
    for y in range(cities):
        cityList.append(input())
    citySet = set(cityList) # set()removes duplicates 
    count.append(len(citySet))
        
for z in count:
    print(z)

