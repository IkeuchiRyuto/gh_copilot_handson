import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

class AzureOpenAIService:
    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.environ["OPENAI_API_URL"],
            api_key=os.environ["OPENAI_API_KEY"],
            api_version="2024-02-15-preview"
        )
    
    # 引数で渡ってきたpromptをAzure OpenAIに投げて、AIの返答を取得する
    async def query_openai(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"content": "Hello, I'm a chatbot", "role": "system"},
                {"content": prompt, "role": "user"},
            ],
        )
        ai_response = response.choices[0].message.content
        return ai_response