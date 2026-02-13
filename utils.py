def save_resume(text):
    with open("output/generated_resume.txt", "w", encoding="utf-8") as f:
        f.write(text)
