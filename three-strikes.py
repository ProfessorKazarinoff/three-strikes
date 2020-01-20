# three-strikes.py

"""A simple text-based game. 
Pick number to complete the addition problem
You have three chances to get the addition problem correct or you are out.
"""

print("""A simple text-based game. 
Pick number to complete the addition problem
You have three chances to get the addition problem correct or you are out.
""")

nums = [0,1,2,3,4,5,6,7,8,9]

for i in range(3):

    print("Numbers remaining: ")
    print(" ".join([str(num) for num in nums]))

    guess = int(input('Pick a number: '))

    nums.pop(guess)

    print(" ".join([str(num) for num in nums]))

print("Out of guesses, you loose")
