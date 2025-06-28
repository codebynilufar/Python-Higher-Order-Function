nums = list(range(1, 21))

evens = filter(
    lambda num: num % 2 == 0,
    nums
)

kv_evens = list(map(
    lambda num: pow(num, 2),
    evens
))
print(kv_evens)