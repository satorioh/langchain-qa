from langchain.vectorstores import FAISS
from configs.global_config import *
from typing import List


class VectorStore:
    def __init__(self, embeddings, split_docs):
        print("init vector store...")
        self.embeddings = embeddings
        self.split_docs = split_docs
        try:
            self.db = FAISS.load_local("faiss_index", embeddings)
        except Exception as err:
            self.db = FAISS.from_documents(split_docs, embeddings)
            self.db.save_local("faiss_index")
        print("init vector store finished")

    @staticmethod
    def generate_prompt(related_docs: List,
                        query: str,
                        prompt_template=PROMPT_TEMPLATE) -> str:
        context = "\n".join([doc.page_content for doc in related_docs])
        prompt = prompt_template.replace("{question}", query).replace("{context}", context)
        return prompt

    def get_similarity_docs(self, query):
        print("start similarity search...")
        result = self.db.similarity_search(query)
        print("similarity search result:")
        print(result)
        return result

    def get_vector_prompt(self, query):
        # TODO query need vector
        related_docs = self.get_similarity_docs(query)
        prompt = self.generate_prompt(related_docs, query)
        return prompt
