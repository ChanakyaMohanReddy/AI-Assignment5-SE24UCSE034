## Assignment 5 - Q4 - Bayesian Networks

---

A Bayesian Network is a probabilistic graphical model used to represent relationships between different variables using nodes and directed edges. It helps in modelling uncertainty and performing probabilistic reasoning based on given evidence.

This program demonstrates the basic concepts of Bayesian Networks using a medical diagnosis example. In this implementation, diseases such as Flu and Covid are connected with symptoms like Fever, Cough, and Breathing Problem. The relationships between these variables are represented using a Bayesian Network structure.

The program uses the pgmpy library for modelling and inferencing. Conditional Probability Distribution (CPD) tables are used to represent probabilities between diseases and symptoms.

The Bayesian Network created in this assignment performs inferencing using Variable Elimination. Different test cases are used to calculate probabilities such as:

* probability of Flu given Fever and Cough
* probability of Covid given Breathing Problem
* probability of Covid given Fever
* probability of Cough given Covid

The program also displays the nodes and edges of the network to show the problem representation clearly.

---

### Some commonly used tools for Bayesian Networks are:

* pgmpy - is a Python library used for creating Bayesian Networks, defining probability tables, and performing inference operations.

* GeNIe - is a graphical tool used for designing and visualizing Bayesian Networks and decision networks.

* Netica - is a software tool used for probabilistic reasoning and Bayesian Network modelling.

* Bayes Server - is a platform used for building and analyzing Bayesian Network models in real-world applications.

* bnlearn - is an R package used for learning Bayesian Network structures and performing probabilistic analysis.


These tools are used for modelling, probability representation, and inferencing in Bayesian Network applications.

---

### Sample Output

Bayesian Network model created successfully.

Nodes in the network:
['Flu', 'Fever', 'Cough', 'Covid', 'BreathingProblem']

Edges in the network:
[('Flu', 'Fever'), ('Flu', 'Cough'), ('Covid', 'Fever'),
 ('Covid', 'Cough'), ('Covid', 'BreathingProblem')]

Probability of Flu given Fever and Cough
No : 0.2369
Yes: 0.7631

Probability of Covid given Fever, Cough and Breathing Problem
No : 0.1726
Yes: 0.8274

Probability of Covid given Breathing Problem
No : 0.4474
Yes: 0.5526

Probability of Flu given Fever
No : 0.2975
Yes: 0.7025

Probability of Covid given Fever
No : 0.668
Yes: 0.332

Probability of Cough given Covid
No : 0.29
Yes: 0.71
