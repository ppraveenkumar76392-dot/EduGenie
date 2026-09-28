from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )

def fail(exc):
    return JSONResponse(status_code=500, content={"error": str(exc)})

@app.post("/qa")
async def qa(text: str = Form(...)):
    try:
        if not text.strip(): return JSONResponse({"error":"Please enter a question."}, status_code=400)
        return {"result": answer_question(text.strip()), "type":"qa"}
    except Exception as e: return fail(e)

@app.post("/explain")
async def explain(text: str = Form(...)):
    try:
        if not text.strip(): return JSONResponse({"error":"Please enter a topic."}, status_code=400)
        return {"result": explain_concept(text.strip()), "type":"explain"}
    except Exception as e: return fail(e)

@app.post("/quiz")
async def quiz(text: str = Form(...)):
    try:
        if not text.strip(): return JSONResponse({"error":"Please enter a topic or passage."}, status_code=400)
        return {"result": generate_quiz(text.strip()), "type":"quiz"}
    except Exception as e: return fail(e)

@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        if not text.strip(): return JSONResponse({"error":"Please enter text to summarize."}, status_code=400)
        return {"result": summarize_text(text.strip()), "type":"summarize"}
    except Exception as e: return fail(e)

@app.post("/learn/recommendations")
async def recommendations(text: str = Form(...)):
    try:
        if not text.strip(): return JSONResponse({"error":"Please enter a learning topic."}, status_code=400)
        return {"result": get_learning_recommendations(text.strip()), "type":"learning_path"}
    except Exception as e: return fail(e)

@app.get("/health")
async def health():
    return {"status":"ok"}
