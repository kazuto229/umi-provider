from fastapi import FastAPI
from pydantic import BaseModel

from gateway.router import ProviderRouter
from providers.umi_kiro import UMIKiroProvider
from providers.umi_canva import UMICanvaProvider

app = FastAPI(title="UMI Provider Gateway")

providers = [
    UMIKiroProvider(),
    UMICanvaProvider()
]

router = ProviderRouter(providers)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {
        "gateway": "UMI Provider Gateway",
        "status": "online"
    }

@app.post("/chat")
async def chat(req: ChatRequest):
    return await router.route_prompt(req.prompt)