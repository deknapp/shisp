SHISP

Sample HIgh dimensional SPaces with complex, nonlinear contraints 

Installation instructions:

To get the code from git, git clone https://github.com/deknapp/shisp.git . You should not
need any Python modules that do not come with Python 2.7.10. 

To make sure you can run sampler, you need to execute:

python install.py

This changes the permissions of sampler to allow it to be executed.   

If you have any issues obtaining or running the code, please email me
at nathaniel.knapp@gmail.com. 

Description of algorithm:

I used a modification of the hit and run sampling method described mathematically in answer 2 of this question on math overflow: 
https://mathoverflow.net/questions/9854/uniformly-sampling-from-convex-polytopes

The algorithm is contained in the file src/sample.py, which has a few explanatory comments.

Here is a summary of the sampling algorithm steps:

1. Start at the example point, let's call it P, provided in the input file. 

2. Move away from P in the same randomly generated direction D, scaled by epsilon, until either 10 moves have been made, or
   a point that does not meet constraints is reached. Add each valid point obtained along the way to a temporary list.

3. If a point that does not meet constraints is reached, and at least one valid point 
   was obtained before going outside constraints, select a random valid point from the temporary list in number 2, and 
   add it to the final list of valid points. Then, use this point as P in order to repeat step 2. In each repetition of step 
   2, use a newly generated random direction.

4. If a point that does not meet constraints is reached before any valid points are obtained, repeat step 2 using
   the same starting point, but a different random direction.  

5. If more than 10 moves have been made in step 2, repeat step 2, with the same direction and starting point P, but
   with an epsilon ten times greater.

6. Repeat step 2 and 3 until the number of valid points obtained in step 3 is equal to the number of results
  specified in the input file.




  

 
