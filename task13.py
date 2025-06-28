sentence = "Functional programming in Python is very powerful and elegant"

words = sentence.split()

words = sorted(
    words,
    key=lambda word: len(word)
)

print(words[-3:])