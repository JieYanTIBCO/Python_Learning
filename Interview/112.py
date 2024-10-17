fruit = ["apple.", "/BaNaNa,", "CHERRY  ", None]
try:
    if not all(map(lambda f: isinstance(f, str),fruit)):
        raise TypeError("There is none str type in the list!")

    first_Capital_fruit = list(map(lambda x: x.strip("./, ").lower().capitalize(), fruit))

    print(first_Capital_fruit)

except Exception as e:
    print(f"Error:{e}")