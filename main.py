# fastapiのメインファイル
# ここからサーバーを起動する
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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