# Read resume from file
with open("sample_resume.txt", "r") as file:
    resume = file.read().lower()

# Read skills from file
with open("skills.txt", "r") as file:
    skills = file.read().splitlines()

print("===== SMART RESUME ANALYZER =====")

print("\nResume Loaded Successfully!\n")

print("Skills Found:")

for skill in skills:
    if skill.lower() in resume:
        print("✔", skill)
