# Read resume from file
with open("sample_resume.txt", "r") as file:
    resume = file.read().lower()

print("Resume Loaded Successfully!")
print(resume)
