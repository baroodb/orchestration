from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Response': 'Real Madrid could not  sign MBappe this summer!'}


