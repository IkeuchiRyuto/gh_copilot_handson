# fastapiのメインファイル
# ここからサーバーを起動する
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.aoai import AzureOpenAIService

# インスタンスの生成
app = FastAPI()

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルーティングの設定
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# チャットリクエストのためのモデル
class ChatRequest(BaseModel):
    text: str

# Azure OpenAI Serviceのインスタンス化
azure_openai_service = AzureOpenAIService()

# チャットエンドポイント
@app.post("/chat")
async def chat(chat_request: ChatRequest):
    try:
        response = await azure_openai_service.query_openai(chat_request.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))