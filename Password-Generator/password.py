from string import punctuation,ascii_letters,digits
import random
combined = ascii_letters+digits+punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(combined))
for i in range(10):
    print(password)
