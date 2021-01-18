function validateResponse(response) {
    if (!response.ok) {
        throw Error(response.statusText);
    }
    return response.json();
}

function makeQuestions(data) {
    const title = data.title;
    const questions = data.question;

    for (const question of questions) {
        var questionCard = document.createElement("div");
        questionCard.className = "quizcard";
        var questexttionTitle = document.createElement("h3");
        questexttionTitle.appendChild(document.createTextNode(question.question));
        questionCard.appendChild(questexttionTitle);

        var question_input = document.createElement("input")
        question_input.type = "text"
        question_input.className = "answerinput";
        questionCard.appendChild(question_input);

        var question_submit = document.createElement("button");
        question_submit.appendChild(document.createTextNode("Sjekk Svar"));

        document.getElementById("container")
            .appendChild(questionCard)
            .appendChild(question_submit);


    };
}

function checkButttonsInit() {
    var container = document.getElementById("container");
    container.querySelectorAll("button").forEach(button => console.log(button));
}

function getQuestions() {
    fetch("api/")
        .then(validateResponse)
        .then(data => makeQuestions(data))
        .then(checkButttonsInit)

};
getQuestions();
