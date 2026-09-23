from rich.console import Console  # pyright: ignore[reportMissingImports]

console = Console()

questions = [
    ("The best CMS in the World?", ["A: WordPress", "B: Joomla", "C: Drupal", "D: Squarespace"], "A"),
    ("What is the most popular CMS?", ["A: WordPress", "B: Joomla", "C: Drupal", "D: Squarespace"], "A"),
    ("Which CMS is known for its user-friendly interface?", ["A: WordPress", "B: Joomla", "C: Drupal", "D: Squarespace"], "A")
]

score = 0
index = 1
NORMAL_SCORE = 10
HIGH_SCORE = 20
PENALTY = 3
correct_answers = 0
for question, answers, correct in questions:
    console.print(question, style="red on white")
    for answer in answers:
        console.print(f"{answer}\n", style= "red")
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == correct:
        correct_answers += 1
        if index == len(questions):
            score += HIGH_SCORE
        else:
            score += NORMAL_SCORE
        console.print("Correct!\n")
    else:
        score -= PENALTY
        console.print(f"Wrong! The correct answer is {correct}.\n")
    index += 1

console.print(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
console.print(f"Your final percentage is: {correct_answers / len(questions) * 100}%")
console.print(f"Your final score is: {score}")