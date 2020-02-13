import random


FORTUNES = [
    "There is a good chance your code will work, eventually.",
    "The weather will be hot, cold or just right today.",
    "I see Network DevOps in your future.",
]


def generate_fortune() -> str:
    """Use mystical forces (a random selection) to get a user's fortune."""
    return random.choice(FORTUNES)


def generate_lucky_numbers(how_many: int) -> list:
    """Returns a list of (random) 'lucky' numbers."""
    lucky_numbers = []
    for _ in range(how_many):
        lucky_numbers.append(random.randint(0, 99))
    return lucky_numbers


def create_fortune_cookie_message(how_many_lucky_numbers: int) -> str:
    """Create and return a fortune cookie message.
    The message should include the user's fortune and lucky numbers.
    """
    # TODO: Create a fortune cookie message by calling generate_fortune() and
    # generate_lucky_numbers() and then composing and returning the fortune
    # cookie's message.
    msg = generate_fortune()
    lucky_nums = generate_lucky_numbers(how_many_lucky_numbers)
    lucky_nums = "-".join(str(n) for n in lucky_nums)
    lucky_msg = f"{msg}\nLucky Numbers: {lucky_nums}"
    return lucky_msg

    # raise NotImplementedError()


def main():
    """Create and print a fortune cookie."""
    print("Get your fortune cookie!")

    # Prompt the user for how many lucky numbers they would like
    qty_lucky_numbers = input("How many lucky numbers would you like?  ")
    try:
        qty_lucky_numbers = int(qty_lucky_numbers.strip())
    except ValueError:
        print("Number must be a integer.")
        main()

    # Create and display their Fortune
    fortune_cookie_message = create_fortune_cookie_message(qty_lucky_numbers)
    print("\nHere is your fortune:\n")
    print(fortune_cookie_message)


if __name__ == '__main__':
    main()