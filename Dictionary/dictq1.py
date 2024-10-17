
def get_highest_scorer(student_scores: dict) -> str:
    current_score=0
    max_score=0
    max_student=""
    for student, score in student_scores.items(): # iterate student_scores dictionary
        scorelist=list(score)   # get score list
        sum=0
        for i in scorelist:                 # sum the score
            sum+=i
        current_score=round(sum/len(scorelist), 10)   # get average score with 2 digital around.
        if (current_score>max_score) or (current_score==max_score and student<max_student):
            max_score=current_score
            max_student=student
    return str(max_student)







student_scores = {
    "Alice": [88, 92, 85],
    "Bob": [95, 90, 85],
    "Charlie": [90, 85, 90],
    "Adam": [95, 90, 85],
}

print(get_highest_scorer(student_scores))