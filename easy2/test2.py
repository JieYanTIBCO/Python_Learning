def longestsubstr(mystr):
    n = len(mystr)
    substr = ""
    win = 0

    for x in range(n):
        # Reset the substring for each new starting point `x`
        current_str = ""
        for i in range(x, n): 
            if mystr[i] in current_str:
                break  # Stop if a duplicate character is found
            current_str += mystr[i]  # Add current character to the substring
            if len(current_str) > win:
                win = len(current_str)
                substr = current_str

    return substr

outcome = longestsubstr("abcdabcbbcdefg")
print(f"Length: {len(outcome)}, Substring: '{outcome}'")
