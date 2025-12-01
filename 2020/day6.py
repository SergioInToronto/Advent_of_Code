ANSWER_CHARS = "abcdefghijklmnopqrstuvwxyz"


with open("day6.input") as f:
    group_answers = f.read().strip().split('\n\n')

# total = sum(len({c for c in answers if c in ANSWER_CHARS}) for answers in group_answers)


total = 0

for group_answers in group_answers:
    individual_answers = group_answers.split()
    for char in ANSWER_CHARS:
        if all(char in individual_answer for individual_answer in individual_answers):
            total += 1

print(total)