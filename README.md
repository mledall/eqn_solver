# eqn_solver
The aim of this repository is to use machine learning techniques to solve differential equations. In particular, we will take the Boltzmann differential equations that appear in Leptogenesis.

Below is a run down of how we will go about it:

- The Boltzmann equations are linear first order equations, that dictate the amount of matter-antimatter asymmetry in the universe. They plateau after a certain point. The plateau depends on the parameters of the governing particle theory. We want to generate a machine learning algorithm that takes as input the particle theory parameters, and as output the final value.

- We will start by generating the data by generating a number of instances of the differential equations with different input parameters and the associated plateau values. Anticipating for the machine learning code, in principle this problem is a regression problem since the output values are real numbers. However, classication problems are less demanding numerically. We will thus sort the output values within two categories, those that are within a certain uncertainty range from the theoretical matter-antimatter asymmetry values, labelled as 'yes' or 'correct', and the others labeled as 'no' or 'wrong'. In this way the problem becomes a classification problem.

- We will then create a machine learning algorithm that learns the output 'yes' or 'no' from the input parameters. In principle, this should save us from having to solve the equations in the future. Of course, this means having to solve them initially a couple of thousand times.

- As a bonus, it would be great to know how to invert the machine learning algorithm. More specifically, writing a code that takes as input the output of the equations, and having it telling us what are the particle theory parameters that would generate that input. I don't know how to do this.

