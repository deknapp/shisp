import os, sys

def run_test(test_name, n_results):
  executable = '../sampler'
  test = '../examples/' + test_name + '.txt'
  output = '../output/' + test_name + '_output.txt'
  os.system(executable + ' ' + test + ' ' + output + ' ' + n_results)

run_test(sys.argv[1], sys.argv[2])
