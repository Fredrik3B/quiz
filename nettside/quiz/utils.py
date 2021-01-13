def file_parser(quiz_file):
    all_questions = {}
    with open(quiz_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            question, answer = line.split(":")
            question = question.strip()
            answer = answer.strip().lower()
            all_questions[question] = answer

    return all_questions
