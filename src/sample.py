import constraints

# Credit to https://stackoverflow.com/questions/6683690/making-a-list-of-evenly-spaced-numbers-in-a-certain-range-in-python
# I used one of these answers because I did not want a numpy dependency, in case that 
# would cause installation problems on the Citrine end. 
def linspace(lower, upper, length):
  return [lower + x*(upper-lower)/(length-1) for x in range(length)]

def get_point_list(point_list, sample_vector, n_dims): 
  if len(point_list) == pow(n_dims, 3):
    return point_list
  else: 
    new_point_list = [] 
    for point in point_list:
      for val in sample_vector:
        new_point_list.append(point + val) 
    return get_point_list(new_point_list, sample_vector, n_dims)              

def evaluate(sample_vector, problem_constraints):
  n_good_results = 0
  point_list = get_point_list(sample_vector, sample_vector, problem_constraints.get_ndim())
  for point in point_list: 
    print point
    if problem_constraints.apply(point):
      n_good_results += 1
  return n_good_results

def get_samples(input_file, n_results):
  problem_constraints = constraints.Constraint(input_file) 
  n_dimensions = problem_constraints.get_ndim()
  n_samples_per_dimension = pow(n_results, (1.0/3))
  if int(n_samples_per_dimension) < n_samples_per_dimension:
    n_samples_per_dimension = int(n_samples_per_dimension) + 1
 
  n_good_results = 0 
  while (n_good_results < n_results):  
    n_samples_per_dimension = n_samples_per_dimension + 1
    # I could use numpy.linspace here, but I did not want a numpy dependency
    sample_vector = linspace(0, 1, n_samples_per_dimension) 
    n_good_results = evaluate(sample_vector, problem_constraints)

  return sample_points[:n_results]

