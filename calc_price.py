from kadai2_1 import calc_price
import sys

def calc_price_side_effect(inp=sys.__stdin__, outp=sys.__stdout__):
    while(True):
        price_string = inp.readline()

        if price_string == "": return
        price_string = price_string.split("\n")[0]

        prices = [int(num) for num in price_string.split(',')] if price_string != "" else []
        outp.write(str(calc_price(prices)) + "\n")

if __name__ == "__main__":
    calc_price_side_effect()