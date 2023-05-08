from langchain.vectorstores import FAISS


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

    def similarity_search(self, query):
        print("start similarity search...")
        result = self.db.similarity_search(query)
        print("similarity search result:")
        print(result)
        return result
