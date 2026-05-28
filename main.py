from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from datetime import datetime

app = FastAPI(title="Autonomous Yield Protocol API", version="0.1.0")

# CORS erlauben (damit dein Carrd-Frontend später die API abfragen darf)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "operational", "node": "alpha-primary", "intent": "standby"}

@app.api_route("/api/v1/yield/arbitrage", methods=["GET", "HEAD"])
def get_arbitrage_opportunities():
    # Simulierte Daten-Ausgabe für den Proof-of-Concept
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "network_status": "synced",
        "opportunities": [
            {
                "asset": "ETH/USDC",
                "layer_1": "Ethereum",
                "delta_percent": round(random.uniform(0.8, 2.1), 2),
                "executable": True
            },
            {
                "asset": "RNDR/USDT",
                "layer_1": "Solana",
                "delta_percent": round(random.uniform(0.3, 1.2), 2),
                "executable": True
            }
        ]
    }
