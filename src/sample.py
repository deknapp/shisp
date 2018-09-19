import constraints

def linspace(length):
  return [x*(1.0/(length-1)) for x in range(length)]

def get_point_list(point_list, sample_vector, n_dims): 
  if len(point_list) >= pow(n_dims, n_dims):
    return point_list
  else: 
    new_point_list = list() 
    for point in point_list:
      for val in sample_vector:
        new_point_list += [point + [val]]
    return get_point_list(new_point_list, sample_vector, n_dims)              

def evaluate(sample_vector, problem_constraints):
  n_good_results = 0
  point_list = get_point_list([[x] for x in sample_vector], sample_vector, problem_constraints.get_ndim())
  print len(point_list)
  print point_list
  exit()
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
    print 'number of samples per dimension ', n_samples_per_dimension
    # I could use numpy.linspace here, but I did not want a numpy dependency
    sample_vector = linspace(n_samples_per_dimension) 
    n_good_results = evaluate(sample_vector, problem_constraints)
    n_samples_per_dimension = n_samples_per_dimension + 1

  return sample_points[:n_results]

