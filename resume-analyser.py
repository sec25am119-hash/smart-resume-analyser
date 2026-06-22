print("Welcome to Smart Resume Analyzer")

resume = input("Paste your resume text: ")

skills = ["python", "java", "sql", "git", "machine learning"]

resume = resume.lower()

found_skills = []

for skill in skills:
    if skill in resume:
        found_skills.append(skill)

print("\nSkills Found:")
for skill in found_skills:
    print("-", skill)
