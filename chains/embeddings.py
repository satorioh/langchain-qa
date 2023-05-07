import os
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from configs.global_config import *

source_folder = '../source'
test_folder = '../test'


def get_embeddings():
    # 加载文件夹中的所有txt类型的文件
    loader = DirectoryLoader(test_folder, glob='**/*.md')
    # 将数据转成 document 对象，每个文件会作为一个 document
    documents = loader.load()

    # 初始化加载器
    text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
    # 切割加载的 document
    split_docs = text_splitter.split_documents(documents)
    print(f"EMBEDDING_MODEL:{EMBEDDING_MODEL}")
    print(f"EMBEDDING_DEVICE:{EMBEDDING_DEVICE}")

    current_path = os.path.abspath(__file__)
    dir_name, file_name = os.path.split(current_path)
    parent_dir = os.path.dirname(dir_name)
    absolute_path = os.path.join(parent_dir, embedding_model_dict[EMBEDDING_MODEL])
    embeddings = HuggingFaceEmbeddings(model_name=absolute_path,
                                       model_kwargs={'device': EMBEDDING_DEVICE})
    print(embeddings)
    print("embeddings完成")
    return embeddings
