# sharpfit

> website for purchasing personalied suits based on an AI inference of your chest size and height

## Build Setup and Run

``` bash
# install dependencies
yarn

# serve with hot reload at localhost:8080
yarn dev

# build for production with minification
yarn build

# launch a python 3.12 venv
# install python modules
pip install -r "requirements.txt"

# start python server.py - will run on localhost:8000
python server/server.py

# Provide the sentence and image for the ai model to inference and it should come back with a selection of suits for the occasion that are in stock and with their prices and your chest size.


```

## If you want to run the chest size inference alone

``` bash
# run the getPose.py file
python getPose.py img_name.jpg
```