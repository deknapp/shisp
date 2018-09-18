import constraints
import sample

def main(input_file, output_file, n_results):
  problem_constraints = Constraints(input_file)
  samples = get_samples(constraints, n_results)
	output_file_handle = open(output_file, 'r')
  for sample in samples:
    output_file_handle.print(string(samples))

	

