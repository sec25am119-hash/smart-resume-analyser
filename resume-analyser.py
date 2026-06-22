print("=== Smart Resume Analyzer ===")

resume = input("Paste your resume text:\n")

skills = ["python", "java", "sql", "git", "machine learning", "communication"]

resume = resume.lower()

found_skills = []
missing_skills = []

for skill in skills:
    if skill in resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

score = (len(found_skills) / len(skills)) * 100

print("\nSkills Found:")
for skill in found_skills:
    print("✔", skill)

print("\nMissing Skills:")
for skill in missing_skills:
    print("✘", skill)

print(f"\nResume Score: {score:.1f}%")
