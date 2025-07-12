import os

import requests


def call_openrouter(
    prompt: str, model: str = "mistralai/mistral-7b-instruct",
     temperature: float = 0.3
) -> str:
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content":
                  "You are a helpful academic writing assistant.",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
    }

    base_url = os.getenv("OPENROUTER_BASE_URL",
                          "https://openrouter.ai/api/v1")
    response = requests.post(
        f"{base_url}/chat/completions", headers=headers, json=payload
    )
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"].strip()
