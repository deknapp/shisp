import constraints
import random

# Utility function to test both constraints in the input file and in the prompt.
# Constraints.apply is not enough, because it does not consider that the space
# is limited to the unit hypercube.
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
    # This parameter is hardcoded due to time limiations. 
    # With more time I would tune it to for efficiency and accuracy.
    maximum_iterations = 1000 
    if counter > maximum_iterations:
      return find_valid_point(start_point, direction, epsilon*10, problem_constraints)
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
  valid_point = example
  valid_point_list = [valid_point] 
  # This parameter is hardcoded due to time limiations. 
  # With more time I would tune it to for efficiency and accuracy.
  epsilon = 0.000001 
  while len(valid_point_list) < number_of_results: 
    direction = [random.uniform(-1,1) for x in range(n_dims)]
    test_point = find_valid_point(valid_point, direction, epsilon, problem_constraints)   
    if test_point is not None:
      valid_point_list.append(test_point)
      # Use new valid point found as the next start point.
      valid_point = test_point
    # If a valid point wasn't found, repeat using the same starting point
    # but a new random direction.
  return valid_point_list 
 
def samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  points = evenly_sample_valid_points(problem_constraints, n_results)
  return points 
