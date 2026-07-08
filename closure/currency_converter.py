def make_converter(rate):
    def currency(amount):
        return amount * rate
    return currency

rub_to_usd = make_converter(76.2)
rub_to_aed = make_converter(20.75)

print(rub_to_usd(100))
print(rub_to_aed(100))