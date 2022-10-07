# Playing-With-Pi

A simulation based on an awesome video by 3b1b, and a research paper by Gregory Galperin.

## Basics

There are two visualisations-

1)Block Collisions- Simulated collisions between two blocks and a wall arranged in the order wall, smaller block(m1),
larger block(m2). Such that the total number of collisions comes out to be.
$\lfloor \pi \sqrt{m_{2}/m_{1}} \rfloor$.

2)Light- Simulated reflection of light in a two mirror system such that the angle between the mirrors is
k then the total number of reflections comes out to be $\lfloor \pi /k \rfloor$. Here k corresponds to the inverse
of the mass ratio in the previous simulation. Created two visualisations one in which the angle corresponds to k and a
scaled one (streched in y) which has a fixed angle of $45&deg$ between the mirrors.

## How to run

Note-You should have pygame and graphics installed for running these files.
<br>command for installing pygame- sudo apt-get install python-pygame
<br>command for installing graphics- pip install graphics.py

If this doesn't work try googling other solutions.

1) Go to terminal and write python3 collisions.py.
2) Go to terminal and write python3 reflections.py
3) Go to terminal and write python3 reflectionsscaled.py

You can change the values of m2 in each of the files but if you increase it beyond 10000 you may need to decrease
the speed.


## References

https://www.youtube.com/watch?v=jsYwFizhncE&t=0s&ab_channel=3Blue1Brown

https://www.maths.tcd.ie/~lebed/Galperin.%20Playing%20pool%20with%20pi.pdf
