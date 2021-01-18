// var quiz_selector = document.getElementById("id_quizark");

document.querySelectorAll(".choose").forEach(
    button => button.addEventListener('click', (event) => {
        document.querySelector(`#id_quizark > option[value="${event.target.value}"]`).selected = true;
    })
)
