"""最小 FastAPI 接口练习。

规格：
- GET /health 不需要请求体
- 成功时返回 200，JSON 为 {"status": "ok"}
- 启动后在 /docs 调用；访问不存在的 /missing 观察响应
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}