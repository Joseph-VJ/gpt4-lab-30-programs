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


notes = input("Enter meeting notes: ")
prompt = f"""Convert these notes into structured meeting minutes.
Include:
1. Meeting summary
2. Important decisions
3. Action items

Meeting notes:
{notes}"""
result = ask_ollama(prompt)
display_result(result)
save_result(result, "meeting_minutes.txt")
