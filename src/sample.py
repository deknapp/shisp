import constraints
import random

def valid(point, problem_constraints):
  if not problem_constraints.apply(point):
    return False
  for val in point:
    if (val<0.00000 or val>1.00000):
      return False
  return True

def random_direction(n_dims):
  return [random.uniform(-1,1) for x in range(n_dims)]

def increment_in_direction(point, direction, epsilon):
  for i in range(len(direction)):
    point[i] += direction[i]*epsilon 
  return point

# source: https://mathoverflow.net/questions/9854/uniformly-sampling-from-convex-polytopes
# I am using the "hit and run" method described in one of the answers.
def find_valid_point(start_point, direction, epsilon, problem_constraints):
  boundary = start_point
  counter = 0 
  max_iterations = 1000
  while True: 
    counter += 1
    if (counter > max_iterations):
      return find_valid_point(start_point, direction, epsilon*10, problem_constraints)
    boundary = increment_in_direction(
      boundary, 
      direction,
      epsilon) 
    if not problem_constraints.apply(boundary):
      break 
  random_step = random.randint(0, counter)
  valid_point = start_point
  for i in range(random_step):
    valid_point = increment_in_direction(
      valid_point,
      direction,
      epsilon)
  return valid_point 

def evenly_sample_valid_points(problem_constraints, number_of_results):
  n_dims = problem_constraints.get_ndim()
  valid_point = problem_constraints.get_example()
  valid_point_list = [valid_point] 
  direction = random_direction(problem_constraints.get_ndim())
  epsilon = 0.0000001
  while len(valid_point_list) < number_of_results:
    valid_point = find_valid_point(valid_point, direction, epsilon, problem_constraints)   
    valid_point_list.append(valid_point)
  return valid_point_list 
 
def samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  points = evenly_sample_valid_points(problem_constraints, n_results)
  return points 

