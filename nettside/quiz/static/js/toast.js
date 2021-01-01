document.querySelectorAll(".toast-message").forEach(function(currentValue) {
    currentValue.classList.add("show-toast");
    setTimeout(function(){ currentValue.remove(); }, 7000);
});
