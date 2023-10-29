from transformers import pipeline
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Download a model from Hugging Face
generator = pipeline(
    "text-generation", model="databricks/dolly-v2-3b", use_auth_token=True
)

app = FastAPI()


class Body(BaseModel):
    text: str


# Run "uvicorn --host 0.0.0.0 main:app" to run the app locally
@app.get("/")
def root():
    return HTMLResponse(
        "<h1>A self-documenting API to interact with a GPT2 model and generate text.</h1>"
    )


@app.post("/generate")
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
