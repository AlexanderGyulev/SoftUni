grade_data = float(input())


def grades_classification(grade):
    if 2 <= grade <= 2.99:
        return "Fail"
    elif 3 <= grade <= 3.99:
        return "Poor"
    if 4 <= grade <= 4.49:
        return "Good"
    if 4.5 <= grade <= 5.49:
        return "Very Good"
    elif grade >= 5.50:
        return "Excellent"


print(grades_classification(grade_data))
