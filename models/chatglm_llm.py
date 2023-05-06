import logging
import requests
import langchain
from typing import Optional, List, Dict, Mapping, Any
from langchain.llms.base import LLM
from langchain.cache import InMemoryCache
from configs.api_config import CHATGLM_API_URL

logging.basicConfig(level=logging.INFO)
# 启动llm的缓存
langchain.llm_cache = InMemoryCache()


class ChatGLM(LLM):
    # 模型服务url
    url = CHATGLM_API_URL

    @property
    def _llm_type(self) -> str:
        return "ChatGLM"

    def _construct_query(self, prompt: str) -> Dict:
        """构造请求体"""
        query = {
            "prompt": prompt,
            "history": []
        }
        return query

    @classmethod
    def _post(cls, url: str, query: Dict) -> Any:
        """POST请求"""
        _headers = {"Content_Type": "application/json"}
        with requests.session() as sess:
            resp = sess.post(url,
                             json=query,
                             headers=_headers,
                             timeout=60)
        return resp

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        # construct query
        query = self._construct_query(prompt=prompt)

        # post
        res = self._post(url=self.url, query=query)

        if res.status_code == 200:
            res_json = res.json()
            predictions = res_json["response"]
            return predictions
        else:
            return "请求错误！"

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        _param_dict = {
            "url": self.url
        }
        return _param_dict
