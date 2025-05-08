from apiKeyInfo import * # contains hidden API keys
import openai


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













if __name__ == "__main__":

    user_prompt = input("Enter anything here: ")

    print("OpenAI Response: ", generate_openai(user_prompt))

