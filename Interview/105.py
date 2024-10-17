def process_data(data):
    # Trying to access the length of the data
    print("111")
    if data is None:
        raise TypeError("data is None value, null pointer exception!!!")
    return len(data)


try:
    a = 10 / 0
except ZeroDivisionError as e:
    print(f"Error caught: {e}")


# Calling the function with None
try:
    result = process_data(None)

    print(result)
    print("222")
except TypeError as e:
    print(f"Error caught: {e}")

print("finished!!")
