HMM.py


USAGE: ./hmm.py


I've been reading up more on radar tracking algorithms, specifically the logic behind Kalman Filters. While I haven't built anything on that level yet, I was able to put together an interesting kind of analysis program.

It's built logically similarly to a Hidden Markov Model (got inspired after I read how easily Kalman Filter state measurements vs. expected values can be modeled via HMM).

Let's say you observed 20 states for a given track. The program prompts the user to enter in 1) the number of states, 2) the values for each of the state parameters 3) the expected values for each parameter at each state

From this, it spits back the mean squared error for each parameter (let's say your states are each 3-dimensional vectors measuring position, velocity, and acceleration, it will give you an MSE for each of these). 

Overall, manual entry is certainly not the most efficient means of analysis, but it could potentially be paired up with a given tracking algorithm to judge the accuracy of predicted tracks automatically.


- Brian Erickson, Systems Engineer, Aspiring Scientist


