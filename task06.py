emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
gmails = list(filter(lambda e: e.endswith("@gmail.com"), emails))

print(gmails)