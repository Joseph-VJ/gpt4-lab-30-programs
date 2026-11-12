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


text = input("Enter a paragraph: ")
prompt = f"""Extract the important keywords and key phrases.
Also identify the main concepts.
Present the results in a clear, readable bullet list.

Paragraph:
{text}"""
result = ask_ollama(prompt)
display_result(result)
