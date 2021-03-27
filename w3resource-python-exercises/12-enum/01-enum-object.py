from enum import Enum

class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672

print(Country.Albania)
print(Country.Albania.name)
print(Country.Albania.value)

