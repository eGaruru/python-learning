import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_number = random.randint(0, len(friends) - 1)
person_who_pays_bill = friends[random_number]

print(person_who_pays_bill)

# Alternative

# 1 Option
print(random.choice(friends))

# 2 Option
random_index = random.randint(0, 4)
print(friends[random_index])

# 3 Option
random_index = random.randrange(0, len(friends))
print(friends[random_index])