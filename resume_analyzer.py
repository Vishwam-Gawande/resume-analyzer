import re


def analyze_resume(text):
    score = 0
    feedback = []
    strengths = []

    text_lower = text.lower()


    if "@" in text:
        score += 1
        strengths.append("Email present")
    else:
        feedback.append("Add email address")


    if re.search(r"\d{5}[- ]?\d{5}", text):
        score += 1
        strengths.append("Phone number present")
    else:
        feedback.append("Add phone number")


    if "linkedin" in text.lower():
        score += 1
        strengths.append("LinkedIn profile present")
    else:
        feedback.append("Add LinkedIn profile ")

    if "project" in text_lower:
        score += 2
        strengths.append("Projects section present")
    else:
        feedback.append("Add a project section")

    if "experience" in text_lower:
        score += 2
        strengths.append("Experience section present")
    else:
        feedback.append("Add experience section")

    if "skills" in text_lower:
        score += 2
        strengths.append("Skills section present")
    else:
        feedback.append("Add skills section")


    sections = ["project", "experience", "skills", "education"]

    found_section = [s for s in sections if s in text_lower]

    score += len(found_section) 

    if len(found_section) >= 3:
        strengths.append("Well-structured resume with multiple sections")
    else:
        feedback.append("Add more structured sections (project, experience, skills)")

    action_words = ["build", "developed", "created", "designed", "implemented"]

    count = sum(1 for word in action_words if word in text_lower)

    if count >= 2:
        score += 2
        strengths.append("Good use of action words")
    elif count == 1:
        score += 1
        feedback.append("Add more strong action words ")
    else:
        feedback.append("Use action words like build, developed, created")

    score = min(score, 12)
    
    return{
        "score": score,
        "strengths": strengths,
        "feedback": feedback
    }


if __name__ == "__main__":
    
    resume_text = input("Paste your resume text:\n")

    result = analyze_resume(resume_text)

    print("\n📊 RESUME ANALYSIS")
    print("="*30)

    print(f"\n🎯 Score: {result['score']} / 12")

    print("\n✅ Strengths:")
    for s in result["strengths"]:
        print(f"✔ {s}")

    print("\n⚠️ Areas to Improve:")
    for f in result["feedback"]:
        print(f"✘ {f}")

        print(result)