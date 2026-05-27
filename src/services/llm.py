



import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_answer(prompt):

    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
    

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    # print("STATUS CODE:", response.status_code)

    # print("RAW RESPONSE:")
    # print(response.text)

    # result = response.json()

    # return result.get("response", "No response from model")
    return response.json()["response"]