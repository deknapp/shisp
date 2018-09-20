import constraints
import random


def valid(point, problem_constraints):
  if not problem_constraints.apply(point):
    return False
  for val in point:
    if (val<0.001 or val>1.000):
      return False
  return True

# TODO
def increment_in_direction(point, direction, epsilon):
  return point


def get_boundary_in_direction(start_point, direction, epsilon, problem_constraints):
  min_boundary = start_point 
  while valid(min_boundary, problem_constraints):
    min_boundary = increment_in_direction(min_boundary, direction, -1*epsilon) 
  max_boundary = start_point 
  while valid(max_boundary, problem_constraints):
    max_boundary = increment_in_direction(max_boundary, direction,  epsilon)
  return [min_boundary[direction], max_boundary[direction]]
  
# source: https://mathoverflow.net/questions/9854/uniformly-sampling-from-convex-polytopes
def find_valid_point(valid_point, problem_constraints):
  direction = random.randint(0, problem_constraints.get_ndim()-1)
  epsilon = 0.0001
  boundaries = get_boundary_in_direction(valid_point, direction, epsilon, problem_constraints)
  valid_point = random.uniform(boundaries[0], boundaries[1])   
  return valid_point

def evenly_sample_valid_points(problem_constraints, number_of_results):
  n_dims = problem_constraints.get_ndim()
  valid_point = problem_constraints.get_example()
  valid_point_list = [valid_point] 
  valid_points_obtained = 0 
  while valid_points_obtained < number_of_results:
    valid_point = find_valid_point(valid_point, problem_constraints)   
    valid_point_list.append(valid_point)
    valid_points_obtained += 1
    start_point = valid_point 
  return valid_point_list 
 
def get_samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  points = evenly_sample_valid_points(problem_constraints, n_results)
  print points
  return points 

