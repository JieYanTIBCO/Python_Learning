from typing import List, Union, Iterable, Generator
import os

# Field 1: Input Validation
def validate_input(data: Iterable[Union[int, None]]):
    if not isinstance(data, Iterable):
        raise TypeError("Input must be an iterable of integers.")

# Field 2: Processing Logic
def process_item(item: Union[int, None]) -> Union[int, None]:
    if isinstance(item, int) and item > 0:
        return item * 2
    return None

# Field 3: Main Function Logic (Generator Version)
def double_positive_integers(data: Iterable[Union[int, None]]) -> Generator[int, None, None]:
    validate_input(data)
    for item in data:
        doubled_value = process_item(item)
        if doubled_value is not None:
            yield doubled_value

# Save results in batches to avoid high memory usage
def save_to_file_in_batches(data: Iterable[Union[int, None]], batch_size: int, output_file: str):
    # Open the file in write mode
    with open(output_file, "w") as f:
        batch = []
        for value in double_positive_integers(data):
            batch.append(str(value))
            
            # Once the batch size is reached, write to the file
            if len(batch) >= batch_size:
                f.write("\n".join(batch) + "\n")
                batch.clear()  # Clear the batch to start accumulating again
        
        # Write any remaining items in the batch
        if batch:
            f.write("\n".join(batch) + "\n")

# Example Usage:
# This will process a large dataset in batches of 1000 and save to "output.txt"
save_to_file_in_batches(range(1000000), batch_size=1000, output_file="output.txt")
