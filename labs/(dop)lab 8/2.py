num = input().split(";")

result = []
for i in num:
    amounts = i.split(",")
    no_amounts = [amount for amount in amounts if int(amount) >= 1000000000]
    if no_amounts:
        result.append(",".join(no_amounts))

print("\n".join(result))
