from apiKeyInfo import * # contains hidden API keys
import openai
from google import genai


def generate_openai(user_prompt):

    client = openai.OpenAI(api_key=openaiApiKey)
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini", 
        messages = [
            {"role": "system", "content": "You are a master at answering anything."},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response.choices[0].message.content


def generate_gemini(user_prompt):

    client = genai.Client(api_key=geminiApiKey)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=user_prompt
    )

    return response.text










if __name__ == "__main__":

    while True: 
        user_prompt = input("Enter anything here: ")

        print("\n----------------------- OPENAI RESPONSE ----------------------\n")
        print(generate_openai(user_prompt))

        print("\n----------------------- GEMINI RESPONSE -----------------------\n")
        print(generate_gemini(user_prompt))
