import logging
from concurrent.futures import ThreadPoolExecutor

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s",
    level=logging.INFO
)

def process_chunk(chunk):
    """
    Process a chunk of numbers and log the thread handling it.
    """
    logging.info(f"Thread handling chunk: {chunk}")
    results = [num**2 for num in chunk]
    for num, result in zip(chunk, results):
        logging.info(f"{num}'s square = {result}")
    return results

if __name__ == "__main__":
    numbers = list(range(1, 21))  # Numbers 1 to 20
    workers = 4
    chunksize = 5  # Specify chunksize

    # Manually divide numbers into chunks
    chunks = [numbers[i:i + chunksize] for i in range(0, len(numbers), chunksize)]

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(process_chunk, chunks))

    # Flatten the results list
    final_results = [item for sublist in results for item in sublist]

    logging.info(f"Results: {final_results}")
