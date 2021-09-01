from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Response': 'Hello and Welcome here to discuss with us today, we gonna have a lot of fun.'}

