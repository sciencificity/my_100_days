# my_100_days

Attempt to do a 100 day Python coding challenge. The idea is to do the exercises in RMarkdown and use both R and Python to code solutions in, time willing of course!

### Day 1 <2019-12-20>
Today I worked on  Datetimes in Python

### Day 2 <2019-12-21>
I worked more with Datetimes in Python. <br>
I am doing coding in an Rmd & mostly trying to solve in both Python and R since I learn more R that way as well (e.g. today I learnt about the testit package).

### Day 3 <2019-12-22>
Coded a timer in Python. The R equivalent is also in an Rmd but totally cribbed from a SO post. On the plus side I learnt how to use a progress bar, so the cribbing amounted to some learning. 

### Day 4 <2019-12-23>
Today I worked on the Collections module, and learnt about the namedtuple, defaultdict and deque (double ended queue) types. Still to figure out: are there R equivalents? 

### Day 5 <2019-12-24>
Learnt more about collections modules in Python through an exercise.

### Day 6 <2019-12-25>
Added code from Lesson 3 of 'Intro to DL Pytorch' @udacity into a nb.

### Day 7 <2019-12-26>
I worked on Python Data Structures such as Lists & Dictionaries. I also learnt about lambdas and did some numpy practise for the 'Intro to DL with Pytorch' course I am doing. 

### Day 8 <2019-12-27>
Today I worked on some PyTorch tutorials. For example, I learnt that PyTorch methods that end with an _ e.g. add_() is an in place addition. <br>
So:  a.add_(b) is equivalent to a = a + b. 

### Day 9 <2019-12-28>
I worked on Python Dictionaries as well as 'Intro to DL with Pytorch' Udacity lessons. <br>
Learning DL:  https://playground.tensorflow.org. The site is great for someone like me who is just now learning DL - you can visualise what is happening under the hood.

### Day 10 <2019-12-29>
I worked on dictionaries and lists more. Want to get the longest string from a list or dict: <br>
max(data, key=len) where data is the list/dict.

### Day 11 <2019-12-30>
Today I classified the MNIST data using a Neural Network with 2 hidden dense layers and some regularisation in the form of dropout (to prevent overfitting). 

### Day 12 <2019-12-31>
Learnt about the application of different filters in DL CNN's. In doing so I came across this when learning about filtering which helped me [link](https://www.codingame.com/playgrounds/2524/basic-image-manipulation/filtering).

### Day 13 <2020-01-01>
Not as much coding but installed OpenCV (Open Source Computer Vision Library) on anaconda. Learnt this from a classmate: <br>

> activate base <br>
> pip install opencv-contrib-python

### Day 14 <2020-01-02>
Some practice on basic tensor ops. <br>
For e.g. the tensor.view() method lets you reshape a tensor: <br>

> d1 = torch.arange(0,9) # 9 x 1 tensor <br>
> d1.view(3,-1) 

Creates a 3 row by x col matrix (-1 says please infer how many cols needed) - num cols inferred as 3.

### Day 15 <2020-01-03>
I did some Linear regression using PyTorch to learn more torch and python.<br>
https://gist.github.com/sciencificity/ae6b71a86f5bd6101deb147efb24f7a5#file-linearreg_torch-ipynb

### Day 16 <2020-01-04>
Learnt about sampling through DQ's Statistics Fundamental course, and progressed in Lesson 6 of the 'Intro to DL with Pytorch' course (about 80% done now).

### Day 17 <2020-01-05>
Learnt more about sampling through DQ's Statistics Fundamental course, and progressed in Lesson 6 of the 'Intro to DL with Pytorch' course (about 90% done now). Worked on DQ's Statistics Fundamentals course. Learnt about sampling using Python. When we deal with a population and we find the mean, or the max it is called a `parameter` - e.g. if we had to poll everyone in this learnership about their height and then take the average height that would be a `parameter`.
When we do the same for a sample of the population then we term it a `statistic`, for example if we poll all the students in the learnership who are studying full time for their heights and take the average that would be a `statistic`. <br>
Here's how to get a sample of a panda's dataframe:

> sample = df.sample(30, random_state = 1) # set random_state for reproducibility.

### Day 18 <2020-01-06>
Learnt how to emulate a switch statement in Python using a dictionary.

### Day 19 <2020-01-07>
- Finised Lesson 6 of the 'Intro to DL with Pytorch' course of Udacity
- Completed a tutorial on Deep Neural Networks with Pytorch - separated a data cluster (through classification) where the outer circle contained 0's and the inner circle contained 1's using neural network.

### Day 20 <2020-01-08>
- Learnt about pylint linter
- install using `pip install pylint`
- Run at command line using `pylint file_path\file_name.py`
- The more negative your score the worse the linter finds your code
- Fix errors and add pylint: disable to ignore deliberate decisions you have made about your code

### Day 21 <2020-01-09>
- Trained an MNIST image classifier using NN

### Day 22 <2020-01-10>
- Learnt more about the KeyError exception.

### Day 23 <2020-01-11>
- Learnt about Python Exceptions and how to handle them:

    * `assert`
    * Try / Except 
    * Try / Except / Else where `else` code is executed should no exception occur
    * Try / Except / Else / Finally where `finally` code is run regardless of whether an exception occurred or not. Used for cleaning up - e.g. closing a file which was opened earlier.


### Day 24 <2020-01-12>
- Finished NB0 of Georgia Tech GTx: CSE6040x SP20: Computing for Data Analysis course.
- To upload only when assign is passed deadline since it contains answers.

### Day 25 <2020-01-13>
- Finished Lesson 7 together with a Style Transfer nb of own picture and art.

### Day 26 <2020-01-14> and 27 <2020-01-15> 
- Learnt to use pytest

    * For example learnt how to mock values using `from unittest.mock import patch` and `@patch.object(random, 'randint')`
    * Learnt how to simulate the input() call to get the user input using side_effects which can be a list of values.
    * Learnt about `capfd` a feature of pytest - which captures the standard output of the program and execution.
    * Learnt about pytest's parametrize feature where we can give it a list of tuples of argument and expected return values in a decorator. In the function we can just call the func with arg and test it against return
    
### Day 28 <2020-01-16>
- Practised pytest using @pybites (fibonacci and a pybite)

### Day 29 <2020-01-17>
- Tested a stack data structure, learnt about @pytest.fixture

### Day 30 <2020-01-18>
- Learnt about the filter method. For e.g. say you want to remove a particular entry from a list, you can use:

> def remove_mult_x(L, x): <br>
>     assert type(L) is list and x is not None <br>
>     new_L = list(filter((lambda num: num != x), L)) <br>
>     return new_L <br>

> Calling on:<br>
> `remove_mult_x([1, 7, 2, 2, 4, 8, 2, 6], 2)`...<br>
> [1, 7, 4, 8, 6]<br>

- Note to self: upload nb's after the 27th Jan.

### Day 31 <2020-01-19>
- Did a bunch of dictionary and list exercises for Gtx course.
- Note to self: upload nb's after the 27th Jan

### Day 32 <2020-01-20>
- Halfway through Lesson 8 on RNNs of 'Intro to DL using Pytorch' from Udacity.
- Did some intro pybite exercises

### Day 33 <2020-01-21>
- Continued with Lesson 8 of RNNs of 'Intro to DL using Pytorch' from Udacity
- Talk Python list comprehensions

    * Aside: Learnt about string module in the process: https://docs.python.org/3/library/string.html
    * Nifty for if you need to match that the word in a corpus starts with a letter or similar

### Day 34 <2020-01-22>
- Built a shallow net using Keras
- Completed Lesson 8 on RNNs of 'Intro to DL using Pytorch' from Udacity

### Day 35 <2020-01-23>

- Learnt how to use `&nbsp;` and `&emsp;` in markdown.
- Learnt more about list comprehensions - for e.g. here's some advice from Trey over at PyMorsels. List comprehensions are great but sometimes less readable. Solution: break up a list comprehension over several lines.

> Don't do this: <br> <br>
> squared_odds = [n**2 for n in numbers if n % 2 == 1]


> Do this:  <br> <br>
> squared_odds = [ <br>
> &nbsp;&nbsp;&nbsp;&nbsp;n**2<br>
> &emsp;for n in numbers<br>
> &ensp;&ensp;if n % 2 == 1<br>
> ]<br>

"Your code will take up more space this way, but that doesn't matter. Space isn't something we should be optimizing for, readability is."

### Day 36 <2020-01-24>
- Learnt about generators
- Learnt about the timeit module. In order to use timeit in RMarkdown we need to import the module, and then call timeit with the name of the function as a string input 'func_name()', or "func_name()" and tell timeit to look in the global namespace for the function you're trying to time.

### Day 37 <2020-01-25>
- Did some list comprehension and dictionary comprehension bites.
- Started Lesson 9 of Udacity's 'Intro to DL with Pytorch' course.

### Day 38 <2020-01-26>
- Completed GTx course assignment on association rules mining.
- Learnt about defaultdict - there's good info in the post [here](https://realpython.com/python-coding-interview-tips/#handle-missing-dictionary-keys-with-collectionsdefaultdict)

### Day 39 <2020-01-27>
- Learnt about `*args` and `*kwargs`

### Day 40 <2020-01-28>
- Learnt about the representation of floating point and double precision numbers in Python.
- Finished Lesson 9 of Udacity's 'Intro to DL with Pytorch' course.
- Upload nb after the 7th Feb.

### Day 41 <2020-01-29>
- Finished Udacity's 'Intro to DL with Pytorch' course. 

### Day 42 <2020-01-30>
- Learnt about the Kahan summation algo which gives a more accurate sum that usual summing due to the rounding off error. https://en.wikipedia.org/wiki/Kahan_summation_algorithm
- Upload nb after the 7th Feb.

### Day 43 <2020-01-31>
- Worked on GtX assignments due 2020-02-03. Learnt about how the int() function in Python takes 2 arguments, the string you want to convert as well as the base of the string. https://docs.python.org/3/library/functions.html#int

> Definition: int(x, base = 10)<br>
> int('101', base = 2) # Call the function but specify that string representation is in base 2<br>
> &emsp;[Out]: 5<br>

- Note to self: upload nb's after the 7th Feb.


