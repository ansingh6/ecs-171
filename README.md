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

You must have Python installed on your computer, as well as pip in order to complete this tutorial.
Python: https://www.python.org/downloads/
Pip:
```
python get-pip.py
```
To run the code, first download the final model from the link above.
Afterwards, clone the repository into a folder of your choice.
```
git clone https://github.com/ansingh6/ecs-171.git
```
Afterwards, you will need to install the libraries tensorflow, tensorflow_text, fastapi, and streamlit.
It is recommended to have Anaconda on your computer for easier installation of tensorflow.
```
conda create -n tf tensorflow
conda activate tf
pip install tensorflow-text
```

For Linux and Mac, the above commands should be sufficient. However, if you are a Windows user, you will have to downgrade Tensorflow to v2.10.0 in order to install tensorflow-text. This is because the latest version of tensorflow-text does not have a wheel for the latest TF version on Windows. To do this:
```
# if you have not already installed Tensorflow
pip install tensorflow==2.10.0
# if you have installed Tensorflow and want to downgrade it
pip install --upgrade tensorflow==2.10.0
```
After this, continue the tensorflow-text installation as normal.

Once this is finished, fastapi and uvicorn must be installed.
Use pip to install fastapi and uvicorn.
```
pip install uvicorn
pip install fastapi
```

Once installed, you can run the API by using the cd command to the directory containing main.py and frontend.py.
```
uvicorn main:app --reload
```

To verify that the API is up and running, head over to 127.0.0.1:8000/docs and check if there is an API popup.

It is now time to install streamlit. Open up another Terminal or cmd window, and then do:
```
pip install streamlit
```

Verify the installation by running:
```
streamlit
```
and checking to see if it is recognized.

The last step is to run:
```
streamlit run frontend.py
```
which will then pop up a new tab in your browser showing the frontend itself. If this does not occur, navigate to localhost:8501 and check to see if the interface has popped up.

It is important to note that for each modification to the frontend code, the API will reload each time and you will have to wait some time for it to restart before being able to run the full demo again.
