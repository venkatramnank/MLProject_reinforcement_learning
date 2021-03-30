# MLProject_reinforcement_learning
This repo contains code for Shortest distance using Q Learning and Dynamic Modeling of Segway using Q Learning.
This is done as project work for the course Machine Learning.

## Requirements

- Python 3+
- Packages : gym,matplotlib,numpy
- OS preferably: Ubuntu

Note: Please download all openai simulation code from their Github website. Please follow the instructions given in that website properly.

Note: Mujoco needs License. Go to Openai Mujoco docs to install with license.

## OpenAI Simulations
Here are some of the simulations done using OpenAI GYM environment as a part of Learning the concepts of RL.

Mountain Car climbing

<p align="center">
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/mountaincar.gif" width="500" height="300">
  </p>

Lunar Lander

<p align="center">
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/lunarlander.gif" width="500" height="300">
  </p>
  
Bipedal Walker
 
<p align="center">
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/walker.gif" width="500" height="300">
  </p>
  
 ## Case Study : Shortest path using Q Learning
  
The shortest path using Q learning is an example of RL solving Combinatorial optimization problems. It is usually applied for many situations like Delivery and Routing. 

Given below is image of Q matrix and learning curve for a given graph of routers.
<p>
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/shortestdistanceQ.png" >
  </p>
 
 The below graph shows the comparison wrt Dijkstra shortest path time.***
 <p>
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/comparoQshortrst.png" >
  </p>
 *** For larger graphs Q learning takes quite some time. In such cases we use Deep Q Learning.
 
 ## Dynamic Modeling of Segways using Q Learning
 Segways can be seen as inverted pendulum structures. Q Learning can be used to balance them.
 
 After 10 iterations we can see the following
  <p>
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/Cartploe10.gif" >
  </p>
 After 200 iterations we can see the following
  <p>
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/CartpoleQLearn20.gif" >
  </p>
 
 The rewards with respect to 10000 iterations are explained in this graph.
  <p>
<img src="https://github.com/venkatramnank/MLProject_reinforcement_learning/blob/main/GraphsAndGIFs/rewards.png" >
  </p>

## References
- Richard S. Sutton and Andrew G. Barto. 2018. Reinforcement Learning: An Introduction. A Bradford Book, Cambridge, MA, USA.
- Keras Reinforcement Learning Projects , Giuseppe Ciaburro
- Watkins, Christopher JCH, and Peter Dayan. "Q-learning." Machine learning 8.3-4 (1992): 279-292.
- Lillicrap, Timothy P., et al. "Continuous control with deep reinforcement learning." arXiv preprint arXiv:1509.02971 (2015).
- https://gym.openai.com
- https://www.freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc/
- https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56
- https://heartbeat.fritz.ai/automating-an-ai-to-find-the-shortest-route-using-reinforcement-learning-19dc9a3c0411?gi=1ac3a024b9a0
- Github Based Codes


