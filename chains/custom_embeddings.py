import os
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from configs.global_config import *
from utils import *


class CustomEmbeddings:
    def __init__(self):
        print("init embeddings...")
        print(f"EMBEDDING_MODEL:{EMBEDDING_MODEL}")
        print(f"EMBEDDING_DEVICE:{EMBEDDING_DEVICE}")

        absolute_path = get_abs_path(embedding_model_dict[EMBEDDING_MODEL])
        # TODO MEAN pooling warning
        self.embeddings = HuggingFaceEmbeddings(model_name=absolute_path,
                                                model_kwargs={'device': EMBEDDING_DEVICE})
        print(f"embedding client: {self.embeddings}")
        print("init embeddings finished")
