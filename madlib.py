import re

def read_template(path):
    try:
        print("Welcome to the Madlib program! This is an interactive game where you will provide various words to fill in the blanks of a pre-written story. The program will prompt you to enter specific types of words, such as nouns, verbs, and adjectives, which will then be inserted into the story to create a unique and silly Madlib.")
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {path}")

def parse_template(template):
    parts = template
    variables = re.findall(r'{([^}]+)}', template)
    stripped = re.sub("{[^}]+}", "{}", parts)
    return stripped, tuple(variables)

def merge(template, parts):
    for part in parts:
        template = template.replace("{}", str(part), 1)
    return template

read_template("./assets/dark_and_stormy_night_template.txt")