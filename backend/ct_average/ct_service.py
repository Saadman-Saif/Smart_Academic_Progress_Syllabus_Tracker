from math import ceil

def calculate_best_three(ct_marks):
    if not ct_marks:
        return 0, 0

    # Remove None values
    valid_marks = [m for m in ct_marks if m is not None]

    if len(valid_marks) == 0:
        return 0, 0

    if len(valid_marks) <= 3:
        average = sum(valid_marks) / len(valid_marks)
        return round(average, 2), len(valid_marks)

    # If 4 marks exist → drop lowest
    sorted_marks = sorted(valid_marks)
    best_three = sorted_marks[1:]

    average = ceil(sum(best_three) / 3)
    return round(average, 2), 3