# Read resume
with open("sample_resume.txt", "r") as file:
    resume = file.read().lower()

# Read skills
with open("skills.txt", "r") as file:
    skills = file.read().splitlines()

found_skills = []
missing_skills = []

for skill in skills:
    if skill.lower() in resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

score = (len(found_skills) / len(skills)) * 100

print("===== SMART RESUME ANALYZER =====")

print("\nSkills Found:")
for skill in found_skills:
    print("✔", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✘", skill)

print(f"\nResume Score: {score:.0f}%")
