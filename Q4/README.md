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

### Some commonly used tools for Bayesian Networks are:

* pgmpy
* GeNIe
* Netica
* Bayes Server
* bnlearn

These tools are used for modelling, probability representation, and inferencing in Bayesian Network applications.

