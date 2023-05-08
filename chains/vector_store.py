from langchain.vectorstores import FAISS


class VectorStore:
    def __init__(self, embeddings, split_docs):
        print("init vector store...")
        self.embeddings = embeddings
        self.split_docs = split_docs
        self.db = None
        print("init vector store finished")

    def save_local(self):
        print("start save local...")
        self.db = FAISS.from_documents(self.split_docs, self.embeddings)
        # self.db.save_local("faiss_index")

    def similarity_search(self, query):
        print("start similarity search...")
        result = self.db.similarity_search(query)
        print("similarity search result:")
        print(result)
