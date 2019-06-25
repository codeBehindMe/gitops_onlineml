# Online to Stream

This is an example of a machine learning pipeline built on GitOps. If you're 
not familiar with GitOps checkout 
https://www.weave.works/technologies/gitops/
for some more information.

We are doing this to prove out some concepts around machine learning
software builds, and not really to focus on the ML concepts themselves.

Therefore, we won't try to go out there and try to get a live data set, instead
we will generate our own on the fly. 

Just to make things interesting, we are going to create a pretty tricky 
machine learning pipeline, which is going to be trained dynamically using
streaming data and mini batch gradient descent. 

## The scenario

We are working in a trading desk, and we are dynamically making trades as the
information comes through. So the trader will make requests through to our
front end system and will expect a binary result returning to buy or sell.

Obviously, it isn't as simple as that, again; this is about engineering and not
about science. 

Let's talk about synthesising the dataset / runtime.

### Generative function

The underlying generative function for this is going to be time dependent.
First, we are going to have a function which is the buy or sell function

f(.)

This function will take some stateless information and depending on some 
threshold return 1 or 0. 

