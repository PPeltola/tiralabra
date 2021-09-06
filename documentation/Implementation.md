### Structure

All the program code is in the root of the *code* folder. *Main* pulls the strings and other modules have a defined purpose (except *Utils*, which is a collection of useful utility functions). Layers are made of neurons and neurons utilize *Vector* algebra. *Loss*, *Activation*, *Backprpagation* and *Rate* just contain functions for the stated purposes. *IO* reads the data and handles the saving and reading of trained layers. *UI* and *Perceptron* remain unused at the moment, but you can find use cases for them in the commented code in *Main*.

### Implementation faults

The program is not even close to an optimal implementation of a neural net. The biggest design flaw is not using matrices for anything, and just relying on vectors. The backpropagation is messy and could be done a lot better with a recursive implementation. *Main* should also be cleaned and parts of the training process should be made into functions instead of just being a part of te main function.
