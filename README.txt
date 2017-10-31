Methods to normalize the Twitter data. More specifically, by giving an unlabelled token, we expect the system to produce a normalized output, such like from tomoroe to tomorrow.

The data set used here contains labelled- tokens.txt, labelled-tokens.txt, and dict.txt, which respectively represents the labelled, un- labelled data, and dictionary. Our system will use the labelled data to evaluate itself, and the final target is to give a canonical form of unlabelled data.

Editdistance, soudex and ngram will be used to achieve the goal.

The system is programmed by python 2.7
The package is in 13 files and 1 directory:

- README.txt: this file, which describes the python files and the test results.

- {labelled, unlabelled}-tokens.txt, dict.txt: these files will be used in the 
  system as input source.

- requirements.txt: contains the python package information which is used by
  pip

- filtered_input.txt: the output of evaluation_input_generator.py.

- output.txt: the output of normalized forms of unlabelled data.

- evaluation_input_generator.py: filter the data in labelled-tokens.txt, and 
  output the data which is needed to be normalized.

- algorithms.py: contains all distance and similarity algorithms used in system.
  In this file, the levenshtein distance, ngram and soudex package are imported
  from the third party, shown below:
  https://pypi.python.org/pypi/editdistance
  https://pypi.python.org/pypi/ngram
  https://pypi.python.org/pypi/Fuzzy

- util.py: contains the assistant functions, including the changes before or 
  after the normalization, and the preprocessing part.

- predict.py: This python file contains the main function of predicting the 
  normalized forms of tokens.

- eval.py: this file, contains the program to run the whole system to evaluate
  the labelled data, and compare the results with the labelled correct forms.
  The accuracy, precision and recall will be calculated, which helps us to 
  make adjustion to the existed system.

- run.py: this python file is the main entrance of the system. If the user 
  gives an input, the program will return the corresponding normalized word. 
  Otherwise, if there is no input, the program will process the data in 
  unlabelled-tokens.txt.  

- test_result: this directory, contains the results of running eval.py,
  showing the evaluation metrics with different normalization strategies.
  In the directory, the file, with the name "l4n5", represents the strategy
  of Levenshtein Distance with threshold 4 and NGRAM with threshold 0.5

  Before running the system, please make sure you've installed all packages,
  by:
  pip install -r requirements.txt

  So, to evaluate the system with labelled-tokens.txt, the precedures are 
  shown below.
  1. python evaluation_input_generator.py > filtered_input.txt
  2. python eval.py
  
  To run the system with single token, for example "freakin":
  python run.py freakin

  To run the system to process the unlabelled-tokens.txt:
  python run.py > output.txt

