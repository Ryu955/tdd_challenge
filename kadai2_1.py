from decimal import Decimal, ROUND_HALF_UP


def calc_price(prices):
    price_sum = sum(prices) * 1.10
    return int(Decimal(price_sum).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

