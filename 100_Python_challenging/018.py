import re


def password_validation(strings: str):
    value = []

    items = [x for x in strings.split(',')]

    for pw in items:
        pw_length = len(pw)
        if pw_length < 6 or pw_length > 12:
            continue
        if all(
            (re.search('[0-9]', pw),
             re.search('[a-z]', pw),
             re.search('[A-Z]', pw),
             re.search('[$#@]', pw))
        ):
            value.append(pw)
    return value


print(password_validation('ABd1234@1,a F1#,2w3E*,2We3345'))
