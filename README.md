# Programming-and-Design-EE1503

Final coursework submission

Task given as follows:

Scientific Data Analysis

Problem description: Dr Smith is a world-famous scientific expert in Biomedical
Engineering. His assistants have performed a large number of complex
experiments. The results of these experiments are stored in the file
results.txt (uploaded separately)

This file contains four rows of data – the first row presents the experiment
number, starting from 1. The second row presents the day of the experiment, in
the format of a floating number, dd.mm (e.g: 12.05 represented the 12th day of
the 5th month, i.e. 12 May). The third row presents the time of the experiment,
presented as a floating point number in the format hh.mm (e.g. 15.45 – the
experiments occurred at quarter to four in the afternoon). Finally, the fourth row
presents the experimental data, as a floating number.

Dr Smith requests that you make a computer program using Python to perform
detailed analysis of the experimental results. The program needs to read the data
from the .txt file and also to write new data into another .txt file. The list of
functions the program should perform is:

1. Reading and displaying the data.

  The program should be able to read the data from the file results.txt and to
  display the data on the screen in a way that gives clear visual understanding of
  the data. When doing this, make sure to name the matrix where data will be kept
  using your first name, for example john_data.


2. Basic data processing
  For the whole data set:
  
  a. The program should be able to identify the maximum and the
  minimum value of the experimental results
  
  b. The program should be able to calculate the average value and the
  standard deviation value of the experimental results
  
  c. The program should be able to calculate how many experiments
  resulted in values greater than some input value
  
  d. The program should be able to sort the experiments data (4th row) in
  ascending and descending order.
  
  Note: the program should have open with a menu for the user, where the user
  can choose which of the functions 2a-2d they want the program to perform.


3. Data processing for a portion of data.

  The program should process the data according to functions 2a-2d for the
  portion of data specified by the user (e.g. for all data between certain times, or
  for all data on a specific date, or for data for experiment numbers x to y), and to
  display this in the form “The maximum value for the period … is …”. The program
  should enable the user to choose the portion of data.


4. Advanced data processing

  a. The program should be able to return the experiment number, the
  day and the time for any individual experiment value requested by
  the user. The binary search algorithm should be used for this.
  The result should be displayed in the format “ The value … has been
  found in experiment number … which was performed on day … at
  time …”. If the value does not match any of the experiment’s data
  values, the information for the value closest to the input value
  should be returned.
  
  b. The program should enable the user to modify any of the values of
  the experiments and also to add new values of experiments, and to
  store the old and the new values together in a new file. The user
  should be given options of whether they want to change a value or
  to add a new value and should be asked to input the new values.
  The Python code should ideally be modular – there should be a separate module
  (function) for each of the functions listed above. There should be a clear menu
  and communication with the user of the program, with clear explanations of
  what choice is available in each of the functions. You should also consider
  unreasonable inputs from the user.
