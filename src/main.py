import random

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    n = random.randint(0,1000000)
    return {"hello": f"random number: {n}"}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port = 8001)
