import os

print(type(os.environ))

for k, v in os.environ.items():
    print(f"{k}: {v}")
