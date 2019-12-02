from django import template

register = template.Library()


@register.filter
def price_parser(price, decimal=0) -> str:
    if not price:
        print(price)
        return "N/A"
    carry = "%.{}f".format(decimal) % (price % 1)
    buffer = carry[1:]
    p = str(int(price))
    while len(p) > 3:
        buffer = ',' + p[-3:] + buffer
        p = p[:-3]

    buffer = p + buffer
    return buffer
