# Smart Resume Analyzer

# Read resume
with open("sample_resume.txt", "r", encoding="utf-8") as file:
    resume = file.read().lower()

# Read required skills
with open("skills.txt", "r", encoding="utf-8") as file:
    skills = [skill.strip() for skill in file.readlines() if skill.strip()]

found_skills = []
missing_skills = []

# Analyze skills
for skill in skills:
    if skill.lower() in resume:
        found_skills.append(skill)
    else:
        missing_skills.append(skill)

# Calculate score
if len(skills) > 0:
    score = (len(found_skills) / len(skills)) * 100
else:
    score = 0

# Display results
print("=" * 45)
print("        SMART RESUME ANALYZER")
print("=" * 45)

print("\nSKILLS FOUND:")
if found_skills:
    for skill in found_skills:
        print("✓", skill)
else:
    print("No matching skills found.")

print("\nMISSING SKILLS:")
if missing_skills:
    for skill in missing_skills:
        print("✗", skill)
else:
    print("No missing skills!")

print("\nRESUME SCORE: {:.1f}%".format(score))

print("\nIMPROVEMENT SUGGESTIONS:")

if score < 50:
    print("→ Add more relevant technical skills.")
    print("→ Include more technical projects.")
elif score < 75:
    print("→ Add missing skills that match your target role.")
    print("→ Highlight your projects and certifications.")
else:
    print("→ Good skill coverage!")
    print("→ Add measurable achievements to strengthen your resume.")

print("\nAnalysis completed successfully.")
print("=" * 45)
