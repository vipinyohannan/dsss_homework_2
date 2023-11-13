import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def evaluate_expression(num1, num2, operator):
    """
    Evaluate the expression formed by num1, num2, and the operator.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    return f"{num1} {operator} {num2}", result

def math_quiz():
    """
    Conduct a math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem, answer = evaluate_expression(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            user_answer = 0  # Assigning a default value in case of invalid input

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__
