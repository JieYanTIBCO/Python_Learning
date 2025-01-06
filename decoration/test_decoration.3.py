from utils.log_decoration import log_decoration


@log_decoration(max_retries=3)
def process_data(number: int, string_list: list[str], data_dict: dict) -> dict:
    """
    Process the input data and return a dictionary with results.

    Args:
        number: An integer input
        string_list: A list of strings
        data_dict: A dictionary with data

    Returns:
        dict: A dictionary with processed results
    """
    # Example processing
    result = {
        "number_squared": number ** 2,
        "string_lengths": [len(s) for s in string_list],
        "dict_keys": list(data_dict.keys())
    }
    return result


if __name__ == "__main__":
    number = 5.2
    string_list = ["apple", "banana", "cherry"]
    data_dict = {"key1": "value1", "key2": "value2"}

    result = process_data(number, string_list, data_dict) # type: ignore
    print(result)
