# Phishing Detector API Backend

This is the backend service that powers the Chrome extension for detecting phishing messages using GPT-4o.

## Overview
This Flask-based API receives suspicious text and responds with an analysis from OpenAI's GPT-4o model, providing:
- Whether the text appears to be phishing
- An explanation
- A risk assessment

## How It Works
1. Receives a POST request at `/check_phishing` with JSON `{ "text": "..." }`
2. Sends the text to OpenAI ChatCompletion API
3. Returns a JSON response with the analysis

## Requirements
- Python 3.7+
- `Flask`
- `flask-cors`
- `openai`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Environment Variable
Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=your-openai-api-key
```

## Running Locally
```bash
python app.py
```
The server will start on port 10000 and be accessible at `http://localhost:10000`

## Deployment
You can deploy this service to platforms like:
- [Render](https://render.com/)
- [Railway](https://railway.app/)
- Heroku (with some adjustments)

Make sure to expose port 10000 and bind the host to `0.0.0.0` in `app.py`:
```python
app.run(host="0.0.0.0", port=10000)
```

## Sample Request
```bash
curl -X POST http://localhost:10000/check_phishing \
     -H "Content-Type: application/json" \
     -d '{"text": "You have won a prize! Click this link."}'
```

## Author
Created by Aviram Cohen

## License
MIT
