data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]

words = filter(
    lambda item: isinstance(item, str) and len(item) > 5,
    data
)
print(list(words))
