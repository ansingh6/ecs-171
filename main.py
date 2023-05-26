from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import tensorflow as tf
import tensorflow_text as text
import re

class JobPost(BaseModel):
    text: str

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    load_options = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
    model = tf.saved_model.load('the_model_A12/', options=load_options)

@app.post("/predict")
def predict(job_post: JobPost):
    try:
        # preprocess the input
        data = job_post.text
        data = data.replace('\n','').replace('\r','').replace('\t','')
        data = re.sub(r'[0-9]','',data)
        data = re.sub(r'[/(){}\[\]\|@,;.:-]',' ',data)
        data = data.lower()
        data = data.replace('  ',' ')
        
        # model inference
        result = tf.sigmoid(model(tf.constant([data])))
        return {"fraud_probability": result.numpy().tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

