# AIG2018
Repo for the AIG course project

#Requirements
* Python 3
* [Python virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)


#Installation
checkout git repository:

    git clone ...
    cd AIG2018

create virtual environment

    virtualenv env

activate virtual environment

    source env/bin/activate

install requirements

    pip install -r requirements.txt

Prepare nltk

    >>> import nltk
    >>> nltk.download('punkt')

#Running the app

    python app.py

#Virtualenv
When you are done, deactivate virtualenv

    deactivate

#Chat commands
    debug
    stop debug
    please translate
    stop translating
    bye