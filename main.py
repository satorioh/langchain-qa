import time
import logging
from models import ChatGLM

if __name__ == "__main__":
    llm = ChatGLM()
    while True:
        human_input = input("Human: ")

        begin_time = time.time() * 1000
        # 请求模型
        # TODO: llm stop key word
        response = llm(human_input, stop=["stop"])
        end_time = time.time() * 1000
        used_time = round(end_time - begin_time, 3)
        logging.info(f"chatGLM process time: {used_time}ms")
        logging.info(f"ChatGLM: {response}")
