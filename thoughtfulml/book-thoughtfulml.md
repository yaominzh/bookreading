[toc]
# chap01 SOLID
| Machine Learning Problem | Manifests as | SOLID violation
| --- | --- | ---
| Entanglement | Changing one factor changes everything |SRP
| Hidden feedbask loops | having built-in hidden features in model | OCP
| Undeclared consumers/visibility debt |   | ISP
| unstable data dependencies | volatile data | ISP
| correction cascade |   | *
| Glue code | writing code that does everything | SRP
| pipeline jungles |sending data through complex workflow |DIP 
| Experimental paths | Dead paths that go nowhere | DIP
| configuration debt | using old configuration for new data | *
| fixed thresholds a dynamic world | not being flexible to changes in correlations | *
| correlations change | modeling correlation over causation | ML Specific

# chap02 quick intro

| problem | ML category
| --- | ---
| Fitting some data to a function or function approximation | supervised learning
| figuring out what data is without any feedback | unsupervised learning
| maximizing rewards over time | Reinforcement learning

**ML algorithm matrix**
---
| algorithm | learning type | class | restriction bias | Preference bias
| --- | --- | --- | --- | ---
| K-Nearest Neighbors | supervised | Instance based | good for measuring distance-based approximations; suffers from the curse of dimensionality | distance based
| Naive Bayes | supervised | probabilistic | where the inputs are independent from each other | where the probability will always be greater than zero for each class
| Decision Trees / Random Forests | supervised | Tree | bad at problems with low covariance | prefers problems with categorical data
| support vector machines | supervised | Decision Boundary | works where there is a definite distintion between two classifications | prefers Binary classification problems
| Neural Networks | Supervised | nonlinear functional approximation | little restriction bias | prefers binary inputs
| Hidden Markov Models | Supervised/Unsupervised | Clustering | Generally works for system information where the Markov assumption holds| prefers time-series data and memoryless information
| Clustering | unsupervised | Matrix factorization | no restriction | preferes data that is in groupings given some form of distance
| feature selection | unsupervised | Matrix factorization | no restrictions | depending on algorithm can prefer data with high mutual information
| feature selection | unsupervised | Matrix  factorization | no restrictions | depending on algorithm can prefer data with high mutual information
| Bagging Meta-heuristic | Meta-heuristic | will work on just about anything | prefers data that isn't highly variable


