from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Hello my name is Moe'}

@app.get('/health')
def health():
    return {'status': 'ok'}