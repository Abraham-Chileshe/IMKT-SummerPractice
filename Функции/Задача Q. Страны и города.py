cnt_countries = int(input())
countries = dict()

for _ in range(cnt_countries):
    cities = list(input().split())
    for i in range(1, len(cities)):
        countries[cities[i]] = cities[0]

for _ in range(int(input())):
    print(countries[input()])
