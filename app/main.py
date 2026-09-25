from fastapi import FastAPI

from app.schemas import DeckIR

app = FastAPI(title="AI Content Platform Showcase")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/decks/validate")
def validate_deck(deck: DeckIR) -> dict:
    return {"valid": True, "deck": deck.model_dump(mode="json")}
