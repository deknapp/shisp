import constraints
import random

def get_valid_points_using_monte_carlo(problem_constraints, number_of_points):
  valid_point_list = []
  valid_point_counter = 0
  n_dims = problem_constraints.get_ndim()
  while valid_point_counter != number_of_points: 
    point = [random.uniform(0,1) for x in range(n_dims)] 
    if problem_constraints.apply(point):
      valid_point_list.append(point) 
      valid_point_counter += 1
  return valid_point_list 

def filter_out_valid_points(point_list, problem_constraints, n_results):
  for point in point_list:
    if problem_constraints.apply(point):
      valid_point_list.append(point)
  return random.sample(point_list, n_results)

# Divide the hypercube in half until you get number_of_points evenly divided regions 
def get_division_vector(number_of_points, ndims):
  number_of_regions = 1
  dimension_index = 0
  division_vector = [1]*ndims
  while total_points < number_of_points:
    dimension_index = (dimension_index + 1) % ndims
    division_vector[dimension_index] += 1
    total_points *= 2 
  return division_vector

def get_midpoints(division_vector):


# Used http://www.lumina.com/blog/latin-hypercube-vs.-monte-carlo-sampling as a reference
def get_valid_points_using_random_latin_hypercube(problem_constraints, number_of_points):
  n_dims = problem_constraints.get_ndim()
  dimension_division_vector = get_division_vector(number_of_points, ndims) 
  return   

def get_most_scattered_points(points, n_results):
  return points[:n_results]

def get_samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  valid_points = get_valid_points(problem_constraints, n_results*100)
  return best_point_set 

