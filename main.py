import time
from models import ChatGLM
from chains import CustomEmbeddings, VectorStore
from text_splitter import CustomTextSplitter
from utils import *
from scheme.api import BaseResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:6006",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

source_folder = get_abs_path('source')
test_folder = get_abs_path('test')
index_folder = get_abs_path('faiss_index')

embeddings = CustomEmbeddings().embeddings
split_docs = CustomTextSplitter(source_folder).get_split_docs()
vector_store = VectorStore(embeddings, split_docs)
llm = ChatGLM()


@app.post("/api/get-answer", response_model=BaseResponse)
async def get_answer(request: Request):
    json_request = await request.json()
    prompt_template = vector_store.get_vector_prompt(json_request['query'])
    begin_time = time.time() * 1000
    # TODO: llm stop key word
    answer = llm(prompt_template, stop=["stop"])
    end_time = time.time() * 1000
    used_time = round(end_time - begin_time, 3)
    print(f"chatGLM process time: {used_time}ms")
    return {'data': {'answer': answer}, 'code': 200}
