from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter


class CustomTextSplitter:
    def __init__(self, folder_path):
        print("init load documents...")
        # 加载文件夹中的所有txt类型的文件
        self.loader = DirectoryLoader(folder_path, glob='**/*.md')
        # 将数据转成 document 对象，每个文件会作为一个 document
        self.documents = self.loader.load()

    def get_split_docs(self):
        # 初始化加载器
        text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
        # 切割加载的 document
        print("start split docs...")
        split_docs = text_splitter.split_documents(self.documents)
        print("split docs finished")
        return split_docs
