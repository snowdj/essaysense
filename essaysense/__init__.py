"""An NLP project on Automated Essay Scoring.

Project EssaySense
==================
EssaySense is an NLP project on Automated Essay Scoring, based on neural network
technologies.

Several neural network models are included to modelling the scoring task, imple-
mented using TensorFlow (see https://tensorflow.org). Pre-trainedmodels are also
included based on ASAP-AES (see https://www.kaggle.com/c/asap-aes/) dataset. You
can use this application to score English essays, or train new models by feeding
your own datasets.

Use this documentation
----------------------
For any submodule, class or function, you can use built-in 'help' method to
check the documentation.

    >>> help(essaysense.datasets)

Requirements
------------
Note that this project is only compatible with Python 3. Also, TensorFlow 1.4.1+
and NLTK 3.2+ are required to make this project alive.

Subpackages
-----------
    - datasets: datasets used in this project.
    - models: models implemented in this project.
    - metrics:


Run this project
----------------
Temporarily in this preview version, we deliver a command line interfate
'essaysense-cli' alongwith the project to run the models. For more information,
please see README.md.

Copyright and license
---------------------
Copyright (c) 2017 Quincy Liang & Jiancong Gao
Under MIT license
"""

# This project follows SemVer 2.0 (see https://semver.org)
__version__ = "0.0.4"

# Make datasets avaliable
from essaysense import datasets

# Configurations.
from essaysense import configs

# Models implemented in this version.
from essaysense import models

# Package metadata
avaliable_models = {
    "lstm": {
        "model": models.DocumentLevelLstmWithMotPooling,
        "train": datasets.DocumentLevelTrainSet,
        "test": datasets.DocumentLevelTestSet
    },
    "cnn-cnn": {
        "model": models.SentenceLevelCnn,
        "train": datasets.SentenceLevelTrainSet,
        "test": datasets.SentenceLevelTestSet
    },
    "cnn-lstm": {
        "model": models.SentenceLevelCnnLstmWithAttention,
        "train": datasets.SentenceLevelTrainSet,
        "test": datasets.SentenceLevelTestSet
    }
}
