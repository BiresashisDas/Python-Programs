# Author :- Biresashis Das

# NOTE :- **kwargs : Many Keyworded Argumnets.

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# Here n is 4, so 4 is first added to 3 and then the result of their addition will be multiplied by 6 and it will give us the output 42.
calculate(4, add=3, multiply=6)


