function validateResponse(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response.json();
}

fetch("api/").then(validateResponse)
    // .then(d => console.log(d))
    .then(data => {
        const title = data.title;
        console.log(title);
        const questions = data.question;
        console.log(questions);

        for (const question of questions) {
            // var fragment = new DocumentFragment()
            var questionCard = document.createElement("div");
            questionCard.className = "quizcard";
            var questexttionTitle = document.createElement("h3");
            questexttionTitle.appendChild(document.createTextNode(question.question));
            questionCard.appendChild(questexttionTitle);

            var question_input = document.createElement("input")
            question_input.type = "text"
            question_input.className = "anwerinput";
            questionCard.appendChild(question_input);

            var question_submit = document.createElement("button")
            question_submit.type = "submit"
            question_submit.appendChild(document.createTextNode("Sjekk Svar"));

            document.getElementById("container")
                .appendChild(questionCard)
                .appendChild(question_submit);

        }
    })


