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
