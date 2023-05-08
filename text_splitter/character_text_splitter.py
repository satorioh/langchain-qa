from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

source_folder = '../source'
test_folder = '../test'


def get_split_docs():
    # 加载文件夹中的所有txt类型的文件
    loader = DirectoryLoader(test_folder, glob='**/*.md')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()

    # 初始化加载器
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    # 切割加载的 document
    split_docs = text_splitter.split_documents(documents)
    return split_docs
