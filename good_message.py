import os
from jinja2 import Environment, FileSystemLoader

MAX_SCORE = 100
TEST_NAME = "Python Challenge"

students = [
    {"name": "Willow", "score": 100},
    {"name": "Cordelia", "score": 85},
    {"name": "Oz", "score": 95}
]

# Ensure the output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template("good.txt")

for student in students:
    name = student["name"]
    filename = os.path.join(output_dir, f"message_{name.lower()}.txt")
    content = template.render(student, max_score=MAX_SCORE, test_name=TEST_NAME)

    with open(filename, mode="w", encoding="utf-8") as output:
        output.write(content)
        print("... wrote", filename)
