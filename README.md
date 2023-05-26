# ECS-171 Group 4 Final Project
Classifying a job posting as real or fraudulent 

## EDA
Notebook to explore given data and all the attributes.

## Logreg notebook
Contains code for a simple logistic regression model. The text is processed through tfidf and then passed into a logistic regression model along with other attributes.
Pretty useless but I guess it's there.

## LLM (main model)
LLM stands for Large-Language Model. We used different sizes of Bert in order to train a model for text classification. The text is concatenated into one string and preprocessed. From there we use the pre-trained language model to perform our classification task.
In order to load the saved model, it must be imported into the same directory as the other scripts. The saved models are not uploaded on github since they are very large and make things crash. 
The final model is uploaded to google drive as a zip. In order to use it, it will need to be downloaded and unzipped.
Remember to add this unzipped folder to the directory while running code.
[Link to final model](https://drive.google.com/file/d/1KSlOKQpM3G8rlEhS9aed8--QP9sVWibl/view?usp=sharing)

## Inference
The inference notebook loads the saved models and makes predictions using them. It shows the exact value assigned by the model rather than a binary output.


## front end
https://streamlit.io/



https://fastapi.tiangolo.com/lo/
Interactive API docs: http://127.0.0.1:8000/docs
