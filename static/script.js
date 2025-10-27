const quoteBox = document.getElementById("quote");
const authorBox = document.getElementById("author");
const button = document.getElementById("btn");
const loading = document.getElementById("loading");

function fetchQuote() {
    loading.style.display = "flex";
    button.style.display = "none";
    quoteBox.textContent = "";
    authorBox.textContent = "";

    fetch("/quote")
        .then(response => response.json())
        .then(data => {
            quoteBox.textContent = data.quote;
            authorBox.textContent = `-${data.author}`;
        })
        .catch(error => console.error("Error:", error))
        .finally(() => {
            loading.style.display = "none";
            button.style.display = "inline-block";
        });
}

fetchQuote();
button.addEventListener("click", fetchQuote);