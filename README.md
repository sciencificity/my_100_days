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

