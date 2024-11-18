def is_valid_part(s):
    # Check if the part is within the range 0-255 and has no leading zeros unless it is '0'
    return 0 <= int(s) <= 255 and (s == "0" or s[0] != '0')

def restore_ip_addresses(s):
    n = len(s)
    result = []

    # Try all possible splits into four parts
    for i in range(1, min(4, n - 2)):       # First part
        for j in range(i + 1, min(i + 4, n - 1)):  # Second part
            for k in range(j + 1, min(j + 4, n)):  # Third part
                # Split the string into four parts
                part1, part2, part3, part4 = s[:i], s[i:j], s[j:k], s[k:]

                # Validate each part
                if all(map(is_valid_part, [part1, part2, part3, part4])):
                    result.append(f"{part1}.{part2}.{part3}.{part4}")

    return result

# Example usage
input_string = "25525511135"
print("Input:", input_string)
print("Valid IP Addresses:", restore_ip_addresses(input_string))
