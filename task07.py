# prices = ["$120", "$340", "$50", "$90"]
# result = list(map(lambda n: int(n[1:]), prices))

# print(result)

prices = ["$120", "$340", "$50", "$90"]
prices_list = list(map(
    lambda price : float(price.replace("$", "")), prices
))

print(prices_list)



