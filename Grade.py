def cal_grade(score):
    if 90 <= score <= 100:
        return "A", "Excellent"
    elif 80 <= score < 90:
        return "B", "Very Good"
    elif 70 <= score < 80:
        return "C", "Good"
    elif 60 <= score < 70:
        return "D", "Fair"
    elif 0 <= score < 60:
        return "F", "Fail – Needs Improvement"
    else:
        return None, "invalid score you sef get sense"

student_name = input("Oboy put your name init: ")

try:
    score = float(input("Enter your score try not to lie: "))
    grade, remark = cal_grade(score)

    if grade is not None:
        print("\n------ Student Report ------")
        print("Name:   ", student_name)
        print("Score:  ", score)
        print("Grade:  ", grade)
        print("Remark: ", remark)
    else:
        print("Error: mumu invalid score entered.")
except ValueError:
    print("Error: baba enter a num value for score.")
