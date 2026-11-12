import requests

# Reusable function to connect Python with Ollama
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()["response"]

# Reusable function to display the AI response
def display_result(result):
    print("\n----- AI OUTPUT -----\n")
    print(result)

# Reusable function to save the AI response in a text file
def save_result(result, filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(result)
    print("\nResult saved in", filename)


subject = input("Enter subject: ")
interest = input("Enter area of interest: ")
prompt = f"""Generate five relevant assignment topics.
Subject: {subject}
Area of interest: {interest}
Give a brief description for each topic."""
result = ask_ollama(prompt)
display_result(result)
