def file_parser(quiz_file):
    all_questions = {}
    with open(quiz_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            question, answer = linje.split(":")
            question = spørsmål.strip()
            answer = svar.strip().lower()
            all_questions[question] = answer

    return all_questions
