import re


filelocation = "C:\\Build\\SRs\\02309066\\EBXLogs\\3.txt"

with open(filelocation, "r") as file:
    log_data = file.read()


ip_pattern = re.compile(
    r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
)


def ip_validator(input):
    for index, row in enumerate(input.splitlines()):
        if row:
            hasip = bool(ip_pattern.fullmatch(row))
            print(index + 1, row, end="---")
            print(hasip)
            # return bool(ip_pattern.fullmatch(input))


ip_validator(log_data)
