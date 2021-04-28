budget, m = float(input()), float(input())
n = int(input())

if m >= budget:
    print(f"We will manage to build it. Start now! Extra money - {(m - budget):.2f}.")
else:
    for i in range(n):
        investor_money = float(input())
        print(f"Investor {i+1} gave us {investor_money:.2f}.")
        m+=investor_money
        if m >= budget:
            print(f"We will manage to build it. Start now! Extra money - {(m - budget):.2f}.")
            break

if m < budget:
    print(f"Project can not start. We need {(budget - m):.2f} more.")