import random
import json

# List of 20 mini code projects
project_ideas = [
    {
        "title": "Random Compliment Generator",
        "description": "A program that generates a random compliment when prompted.",
        "steps": [
            "Create a list of compliments.",
            "Use a randomization function to select a random compliment.",
            "Prompt the user to press Enter to receive a compliment.",
            "Print the compliment to the console."
        ],
        "tags": ["beginner", "fun", "Python"]
    },
    {
        "title": "Number Guessing Game",
        "description": "A game where the user tries to guess a randomly chosen number.",
        "steps": [
            "Generate a random number between 1 and 100.",
            "Prompt the user to guess the number.",
            "Provide feedback if the guess is too high or too low.",
            "Repeat until the user guesses correctly."
        ],
        "tags": ["beginner", "game", "Python"]
    },
    # Add more project ideas...
]

# Function to get a random project idea
def get_random_project():
    project = random.choice(project_ideas)
    project_json = json.dumps(project, indent=4)
    print("Here's your random project idea!")
    print(f"Title: {project['title']}\n")
    print("Description:")
    print(project['description'])
    print("\nJSON Instructions:")
    print(project_json)

# Run the idea generator
get_random_project()
