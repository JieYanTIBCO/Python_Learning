from datetime import datetime, timedelta


# Initialize logger once
logger = get_logger()


def validate_date(start_time, end_time):
    """
    Validate the input date format and value 
    make sure start time is less than end time
    :param start_time: Start time in string format
    :param end_time: End time in string format
    :return: starttime and endtime in datetime format
    """
    formats = ["%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S"]

    def parse_date(date_str: str):
        """
        Format the date string to datetime object and validate the date string with multiple formats.

        Args:
            date_str: date string in string format

        Returns:
            datetime: date string in datetime format
        """
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt
            except ValueError:
                continue
        raise ValueError(
            "Incorrect data format, should be YYYY-MM-DD HH:MM:SS[.sss]")

    starttime = parse_date(start_time)
    endtime = parse_date(end_time)

    if starttime > endtime:
        raise ValueError("Start time must be less than end time")
    return starttime, endtime


def get_user_input():
    """
    Get user input for start and end time
    :return: start time and end time
    """
    start_time = input("Enter the start time (YYYY-MM-DD HH:MM:SS.sss): ")
    end_time = input("Enter the end time (YYYY-MM-DD HH:MM:SS.sss): ")
    return start_time, end_time


def calculate_time_difference(startime: datetime, endtime: datetime) -> None:
    """
    Calculate and print the time difference between starttime and endtime.

    Args:
        start_time: Start time in datetime format
        end_time: End time in stdatetimering format
    """

    time_diff = endtime - starttime
    total_seconds = time_diff.total_seconds()
    time_diff_seconds = time_diff.seconds
    days = time_diff.days
    hours = int(time_diff_seconds // 3600)
    minutes = int((time_diff_seconds % 3600) // 60)
    seconds = int(time_diff_seconds % 60)
    milliseconds = int(time_diff.microseconds // 1000)

    logger.info(f"Time difference is {days} days, {hours} hours, {
                minutes} minutes, {seconds}.{milliseconds} seconds")
    logger.info(f"Time difference in total seconds is {total_seconds}")


def process_dates(test_mode: bool = False) -> None:
    """
    Process user input dates and calculate the time difference.

    Args:
        test_mode: If True, run test code. Otherwise, get user input.
    """
    if test_mode:
        start_time = "2020-11-23 14:30:00.125"
        end_time = "2024-11-24 15:25:22.444"
        starttime, endtime = validate_date(start_time, end_time)
        logger.debug(f"Start time is {starttime}")
        logger.debug(f"End time is {endtime}")
    else:
        start_time, end_time = get_user_input()
        try:
            starttime, endtime = validate_date(start_time, end_time)
            calculate_time_difference(starttime, endtime)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    x = datetime.now()
    ms = (x.microsecond // 1000)*1000
    y = x.replace(microsecond=ms)
    logger.debug(f"now time is {y}")

    # Set test_mode to True to run test code, False for real scenario
    process_dates(test_mode=True)
    # process_dates(test_mode=False)
