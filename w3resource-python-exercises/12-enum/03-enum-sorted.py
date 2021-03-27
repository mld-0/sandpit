import enum

class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672 

countries_sorted = [c.name for c in sorted(Country)]
print(countries_sorted)

countries_sorted = [c.name for c in sorted(Country, key=lambda x: x.name)]
print(countries_sorted)

countries_sorted = [c.name for c in sorted(Country, key=lambda x: x.value)]
print(countries_sorted)

