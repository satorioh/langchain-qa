import os
import logging
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from configs.global_config import *


def get_embeddings():
    logging.info("start embeddings...")
    logging.info(f"EMBEDDING_MODEL:{EMBEDDING_MODEL}")
    logging.info(f"EMBEDDING_DEVICE:{EMBEDDING_DEVICE}")

    current_path = os.path.abspath(__file__)
    dir_name, file_name = os.path.split(current_path)
    parent_dir = os.path.dirname(dir_name)
    absolute_path = os.path.join(parent_dir, embedding_model_dict[EMBEDDING_MODEL])
    # TODO MEAN pooling warning
    embeddings = HuggingFaceEmbeddings(model_name=absolute_path,
                                       model_kwargs={'device': EMBEDDING_DEVICE})
    logging.info(f"embedding client: {embeddings}")
    logging.info("embeddings finished")
    return embeddings
