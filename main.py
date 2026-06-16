from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

SYSTEM_PROMPT = """You are an expert AI research assistant.
When given a topic, provide a thorough, well-structured research summary with:
- Key concepts and definitions
- Current state of the field
- Important applications
- Future directions
Be detailed but clear."""

class ResearchRequest(BaseModel):
    topic: str

# TASK 1: Write the generator function
# def stream_research(topic: str):
#   - create an OpenAI stream with stream=True
#   - for each chunk, if delta exists:
#       yield f"data: {json.dumps({'content': delta})}\n\n"
#   - after the loop, yield "data: [DONE]\n\n"
#
# Why json.dumps here instead of raw text?
# So the frontend can parse structured data — later you can add
# {"content": "...", "tokens": 42} without breaking anything


def stream_research(topic: str):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": topic}
        ],
        stream=True
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield f"data: {json.dumps({'content': delta})}\n\n"
    yield "data: [DONE]\n\n"


# TASK 2: GET "/" — serve static/index.html
# return FileResponse("static/index.html")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.get('/')
def read_root():
    return FileResponse(os.path.join(BASE_DIR, "static", "index.html"))

@app.get('/how-we-roll')
def read_how_we_roll():
    return FileResponse(os.path.join(BASE_DIR, "static", "how-we-roll.html"))

@app.get('/services')
def read_services():
    return FileResponse(os.path.join(BASE_DIR, "static", "services.html"))

@app.get('/community')
def read_community():
    return FileResponse(os.path.join(BASE_DIR, "static", "community.html"))

# TASK 3: POST "/research"
# takes a ResearchRequest
# if topic is empty → raise HTTPException 400
# return StreamingResponse(
#     stream_research(request.topic),
#     media_type="text/event-stream"
# )

@app.post('/research')
async def read_research(request: ResearchRequest):
    if not request.topic:
        raise HTTPException(status_code=400, detail="No topic provided")
    return StreamingResponse(stream_research(request.topic), media_type="text/event-stream")
