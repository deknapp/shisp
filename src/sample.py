import constraints
import random

def valid(point, problem_constraints):
  if not problem_constraints.apply(point):
    return False
  for val in point:
    if (val<0.00000 or val>1.00000):
      return False
  return True

def increment_in_direction(point, direction, epsilon):
  return [point[i] + epsilon*direction[i] for i in range(len(point))]

# source: https://mathoverflow.net/questions/9854/uniformly-sampling-from-convex-polytopes
# I am using a modification of the "hit and run" method described in one of the answers.
def find_valid_point(start_point, direction, epsilon, problem_constraints):
  
  if epsilon > 1:
    return None 
  point = start_point
  counter = 0 
  valid_point_list = []
  while True: 
    counter += 1
    if counter > pow(10, 6):
      return find_valid_point(start_point, direction, epsilon*2, problem_constraints)
    point = increment_in_direction(point, direction, epsilon) 
    if valid(point, problem_constraints):
      valid_point_list.append(point)
    else:
      break 
  if len(valid_point_list) < 1:
    return None
  return random.choice(valid_point_list)

def evenly_sample_valid_points(problem_constraints, number_of_results):
  n_dims = problem_constraints.get_ndim()
  example = problem_constraints.get_example()
  print example
  valid_point_list = [example] 
  epsilon = 0.00001 
  while len(valid_point_list) < number_of_results: 
    direction = [random.uniform(-1,1) for x in range(n_dims)]
    valid_point = find_valid_point(example, direction, epsilon, problem_constraints)   
    if valid_point is not None:
      valid_point_list.append(valid_point)
  return valid_point_list 
 
def samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  points = evenly_sample_valid_points(problem_constraints, n_results)
  for point in points:
    print point
  return points 
