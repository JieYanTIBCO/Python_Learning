import openai
import time
import os


# Set the xAI API base URL
openai.api_base = "https://api.x.ai/v1"

# Get 'YOUR_XAI_API_KEY' from system variable "XAI"
openai.api_key = os.environ.get('XAI')


def chat_with_grok(prompt):
    try:
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        # End timing
        end_time = time.time()

        # Calculate and print the time taken
        elapsed_time = end_time - start_time
        print(f"Time taken: {elapsed_time:.2f} seconds")

        return response.choices[0].message['content']

    except Exception as e:
        return f"An error occurred: {e}"


# Example usage
user_input = "请给我解释一下XAI的服务器架构，通讯网络用的什么? XAI解决了黎曼猜想了吗？"
reply = chat_with_grok(user_input)
print("Grok's Response:", reply)
