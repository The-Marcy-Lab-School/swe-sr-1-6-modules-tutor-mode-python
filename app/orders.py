"""A tiny order program. Nobody has explained it to you. That is the point."""

TAX_RATE = 0.08
MEMBER_DISCOUNT = 0.10


def apply_discount(total, percent_off):
    return total - (total * percent_off / 100)


def add_tax(total):
    return round(total * (1 + TAX_RATE), 2)


def member_price(total, is_member):
    if is_member:
        total = apply_discount(total, MEMBER_DISCOUNT)
    return add_tax(total)


def summarize(items):
    if not items:
        return "No items"
    names = [item["name"] for item in items]
    return ", ".join(names)


def order_total(items, is_member):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return member_price(total, is_member)
