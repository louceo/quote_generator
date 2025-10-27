# Random Quote Generator

A simple web app that fetches random quotes from an API and displays them dynamically using FastAPI and JavaScript.

---

<img width="1440" height="662" alt="quote_page" src="https://github.com/user-attachments/assets/1785a286-22d2-475a-978d-43e839f14e0b" />

## Features

- Fetches random quotes in real-time from a backend API.
- Displays author names.
- Loading animation with spinning dots while fetching a new quote.
- Button to fetch a new quote dynamically without refreshing the page.
  
---

## Stack

- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript (Fetch API)
- **External API**: api-ninjas.com

```markdown
## How it Works

1. The HTML page loads and calls the JavaScript function `fetchQuote()`.

2. `fetchQuote()` sends a request to the FastAPI backend at `/quote`.

3. FastAPI calls `get_quote()` in `quote_gen.py` and returns a JSON object:

{
  "quote": "Beauty is everywhere a welcome guest.",
  "author": "Johann Wolfgang von Goethe"
}
