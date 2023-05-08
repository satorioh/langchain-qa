import time
from models import ChatGLM
from chains import CustomEmbeddings, VectorStore
from text_splitter import CustomTextSplitter
from utils import *

source_folder = get_abs_path('source')
test_folder = get_abs_path('test')

if __name__ == "__main__":
    embeddings = CustomEmbeddings().embeddings
    split_docs = CustomTextSplitter(test_folder).get_split_docs()
    vector_store = VectorStore(embeddings, split_docs)
    vector_store.similarity_search("宅基地使用权及房屋所有权转移登记")
    # llm = ChatGLM()
    # while True:
    #     human_input = input("Human: ")
    #
    #     begin_time = time.time() * 1000
    #     # 请求模型
    #     # TODO: llm stop key word
    #     response = llm(human_input, stop=["stop"])
    #     end_time = time.time() * 1000
    #     used_time = round(end_time - begin_time, 3)
    #     print(f"chatGLM process time: {used_time}ms")
    #     print(f"ChatGLM: {response}")
