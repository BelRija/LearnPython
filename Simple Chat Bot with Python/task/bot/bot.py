def greet(bot_name, birth_year):
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():
    print('Please, remind me your name.')
    user_name = input()
    print(f'What a great name you have, {user_name}!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    remainder_3 = int(input())
    remainder_5 = int(input())
    remainder_7 = int(input())
    age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    target_number = int(input())
    current_count = 0
    while current_count <= target_number:
        print(f"{current_count} !")
        current_count += 1


def get_user_input(prompt):
    print(prompt)
    return int(input())


def test():
    print("Let's test your programming knowledge.")
    print('''Why do we use methods?
            1. To repeat a statement multiple times.
            2. To decompose a program into several small subroutines.
            3. To determine the execution time of a program.
            4. To interrupt the execution of a program.''')

    correct_answer = 2
    user_answer = get_user_input("Your answer:")

    while user_answer != correct_answer:
        print('Please, try again.')
        user_answer = get_user_input("Your answer:")

    print('Congratulations, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


# Main function calls
greet('Timmy', '2025')  # Adjust arguments as required
remind_name()
guess_age()
count()
test()
end()
