# Rock, Paper, Scissors! 
The following sections will provide setup instructions and command lines needed to run the program from scratch, before explaining each section of code.

Rock, Paper, Scissors is a classic game, and this Python script will allow you to play against a computer. Best of luck! 

## Prerequisites

+ Anaconda 3.7+
+ Python 3.7+
+ Pip

## Setup
Once you have accessed the [repository](https://github.com/sarahmardjuki/rock-paper-scissors-exercise) containing the game, fork the remote repository and "clone" your copy onto your computer. 

Navigate to the local repository's root directory, then navigate using the command line:

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment. For example, you can call it "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

Once you're inside the virtual environment, install the packages before trying to run the program. 

```sh
pip install -r requirements.txt
```

Now you're ready to play! Run the Python script from the command-line:
```sh
python game.py
```