function validateResponse(response) {
    if (!response.ok) {
        if (response.status == 404) {
            console.log("Spiller finnes ikke")
        }
        throw Error(response.statusText);
    }
    return response.json();
}

function makeQuestions(data) {
    const title = data.title;
    const questions = data.question;

    for (const question of questions) {
        var id = question.id

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
        question_input.name = "answer"
        question_input.className = "answerinput";
        questionCardForm.appendChild(question_input);

        var question_submit = document.createElement("button");
        question_submit.appendChild(document.createTextNode("Sjekk Svar"));
        questionCardForm.appendChild(question_submit)

        document.getElementById("container")
            .appendChild(questionCard)
            .appendChild(questionCardForm)
        questionCardForm.setAttribute("data-question-id", id)


    };
}

function rightOrWrong(response) {
    const question_id = response.id
    const right = response.answer
    const htmlQuestion = document.querySelector("form[data-question-id='" + question_id + "']").parentElement
    if (right == true) {
        htmlQuestion.classList.add("right-answer")

    } else if (right == false) {
        htmlQuestion.classList.add("wrong-answer")
    } else {
        throw Error("Responsen var hverken riktig eller feil")
    }
    if (response.finish) {
        const rightQuestions = response.finish.right_answers;
        const questionCount = response.finish.question_count;
        var finishBox = document.createElement("div");
        finishBox.className = "finishBox";
        var finishBoxP = document.createElement("p");
        finishBoxP.appendChild(document.createTextNode(`Du greide ${rightQuestions} av ${questionCount} mulige spørsmål`));
        return_home = document.createElement("a")
        return_home.href = "../"
        return_home.appendChild(document.createTextNode("Tilbake"))
        finishBox.appendChild(finishBoxP)
        finishBox.appendChild(return_home)

        document.getElementById("container").appendChild(finishBox)
        console.log(`Du greide ${rightQuestions} av ${questionCount} mulige spørsmål`)

    }
}

// finner csrf_token, fra django docs
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrf_token = getCookie("csrftoken");

function sendAnswer(form) {
    const formData = new FormData(form);
    // Trenger Error handling
    const form_id = form.getAttribute("data-question-id")
    formData.append("id", form_id)
    fetch('api/', {
        headers: {'X-CSRFToken': csrf_token},
        method: 'POST',
        body: formData
    })
        .then(validateResponse)
        .then(response => rightOrWrong(response))
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
