# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
print("POP QUIZ! Solve this simple math problem and flex your brain muscles.")
print("If you get the answer wrong, you will suffer the pain of a poor score")
print("and the wrath of your elders and Python.")
def math_problem_answer():
    x = 178
    y = 294
    z = x + y
    print("If 'x' = 178, 'y' = 294, and 'z' = x + y, find z.")
    answer = int(input("z is equal to: "))
    if answer > z:
        print("Bummer. Hate to say it, but that is not the right answer. Better luck next time!")
    elif answer < z:
        print("Bummer. Hate to say it, but that is not the right answer. Better luck next time!")
    else:
        print("Yes! Yes!! Yes!!! That is the right answer! Great job! That wasn't so hard, now, was it?")
    return z
math_problem_answer()
