def get_answer(prompt):
    while True:
        answer = input(prompt).strip(",!.?/\\").lower()
        if answer in ("yes", "no"):
            return answer


print(get_answer("yes or no? "))


print("asdasd asdadye".capitalize())
