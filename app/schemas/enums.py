from enum import Enum

# Enum containing supported languages, add more as required
class LanguageEnum(str, Enum):
    PT = "PT"
    EN = "EN"


# Enum containing supported currencies, add more as required
class CurrencyEnum(str, Enum):
    BRL = "BRL"
    USD = "USD"