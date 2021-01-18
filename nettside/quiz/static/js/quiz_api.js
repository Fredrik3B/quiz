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

        // lage spørsmålkort med en form
        var questionCard = document.createElement("div");
        questionCard.className = "quizcard";
        var questionCardForm = document.createElement("form");
        questionCardForm.className = "question-form";

        // lage tittel fra spørsmål og legge inni spørsmålkort
        var questexttionTitle = document.createElement("h3");
        questexttionTitle.appendChild(document.createTextNode(question.question));
        questionCard.appendChild(questexttionTitle);

        // lage input til svar inne i form
        var question_input = document.createElement("input")
        question_input.type = "text"
        question_input.className = "answerinput";
        questionCardForm.appendChild(question_input);

        var question_submit = document.createElement("button");
        question_submit.appendChild(document.createTextNode("Sjekk Svar"));
        questionCardForm.appendChild(question_submit)

        document.getElementById("container")
            .appendChild(questionCard)
            .appendChild(questionCardForm)


    };
}

function sendAnswer(form) {
    var formData = new FormData(form)
    // console.log(formData)
    fetch('api/', {
        method: 'POST',
        body: new FormData(formElem)
    });

}

function submitListener() {
    document.querySelectorAll(".question-form").forEach(
        form => form.addEventListener("submit", function(event) {
            event.preventDefault();
            sendAnswer(form)
        })
    )
}

function getQuestions() {
    fetch("api/")
        .then(validateResponse)
        .then(data => makeQuestions(data))
        .then(submitListener)

};
getQuestions();
