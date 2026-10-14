"""Your predictions, before you run anything.

Fill in what you think each call returns. Then run:

    python3 check.py

It tells you which ones matched. A prediction that does not match is not a
mistake, it is a finding. Those are the ones worth writing about.
"""

PREDICTIONS = {
    # "call as written": what you think it returns
    "apply_discount(100, 20)": None,
    "apply_discount(100, 120)": None,
    "add_tax(100)": None,
    "member_price(100, False)": None,
    "member_price(100, True)": None,
    "summarize([])": None,
    "order_total([{'name': 'Tea', 'price': 3.0, 'quantity': 2}], False)": None,
}
