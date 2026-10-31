def ele_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(kwh, 50)
    tier2 = min(max(kwh - 50, 0), 100)
    tier3 = max(kwh - 200, 0)

    energy_cost = (tier1 * 480) + (tier2 * 610) + (tier3 * 730)
    fixed_fee = 2000
    sub_total = energy_cost + fixed_fee
    total_bill = sub_total * 1.10
    return round(total_bill)
kwh_values = [0, 35, 50, 120, 200, 350]
exchange_rate = 4100
print("Electricity bill table")
for kwh in kwh_values:
    bill_riel = ele_bill(kwh)
    bill_usd = bill_riel / exchange_rate
    print(f"{kwh:>3} kwh -> {bill_riel:>7} riel(=  {bill_usd:>5.2f} USD)")

user_input = input("Enter your monthly consumption(kwh): ")
try:
    user_kwh = float(user_input)
    bill = ele_bill(user_kwh)
    if bill is None:
        print("Please enter a non-negative number.")
    else:
        bill_usd = bill / exchange_rate
        print(f"Your bill: {bill:,} riel (={bill_usd:.2f} USD)")
except ValueError:
    print("Please enter a valid number.")
