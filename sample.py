import constraints
import numpy as np

def evaluate(sample_points, constraints):
	n_good_results = 0
	for point in sample_points:
		if constraints.eval(point):
		  n_good_results += 1
  return n_good_results

def get_samples(constraints, n_results):
  n_dimensions = constraints.get_ndim()
  n_samples_per_dimension = pow(n_results, (1/3))
	if int(n_samples) < n_samples:
		n_samples_per_dimension = n_samples + 1
  
  while (n_good_results < n_results):  
    n_samples_per_dimension = n_samples_per_dimension + 1
    sample_vector = np.linspace(0, 1, n_samples_per_dimension)
	  sample_points = np.meshgrid([sample_vector]*n_dimensions]) 
	  n_good_results = evaluate(sample_points, constraints)

  return sample_points[0:n_results]

