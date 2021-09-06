### Reading the dataset

You need to download the [data, all four files](http://yann.lecun.com/exdb/mnist/) and extract them to a folder named 'data' in the root of the project. Keep the file names as they are, or if you wish to change them you need to change the constants in the Data.py as well.

### Running the program

To run the code as is, just run Main.py. I highly recommend using the [pypy3 JIT compiler](https://www.pypy.org/), because it runs the program approximately 10 times faster. With pypy just run `pypy3 Main.py` in the root of the *code* folder.

At the moment, the program will start training a small but decent 32-16-10 neural net with the parameters of:

* Initial learning rate of 0.05

* Learning decay scalar of 0.0025

* Batch size of 100

It will end the training after 20 iterations or an accuracy of 65% or higher. The test run I made with these parameters ended with an accuracy of 49.32%. You can change the learning parameters and the conditions for ending the training by changing the named constants in *Main*.

### Running the tests & coverage

To run the existing tests run `coverage run -m unittest discover` and to check the test coverage run `coverage report -m` after that.
