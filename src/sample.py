import constraints
import random

def get_boundary_in_direction(start_point, direction, epsilon, problem_constraints):
  max_boundary = start_point
  while problem_constraints.apply(max_boundary):   
    max_boundary[direction] += epsilon
  min_boundary = start_point
  while problem_constraints.apply(max_boundary):   
    max_boundary[direction] -= epsilon
  return [min_boundary, max_boundary]

# source: https://mathoverflow.net/questions/9854/uniformly-sampling-from-convex-polytopes
def find_valid_point(start_point, problem_constraints):
  direction = random.randint(0,problem_constraints.get_ndim()-1)
  boundary_points = get_boundary_in_direction(start_point, direction, 0.0001, problem_constraints)
  start_point[direction] += random.uniform(boundary_points[0], boundary_points[1])   
  return start_point

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
  return evenly_saple_valid_points
 
def get_samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  points = evenly_sample_valid_points(problem_constraints, n_results*100)
  return points 

