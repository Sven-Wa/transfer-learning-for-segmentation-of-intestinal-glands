import argparse

#0. define a function
def parse_arguments(args=None):

    # 1. ArgumentParser
    parser = argparse.ArgumentParser(description = "test the parser", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    _general_parameters(parser)
    # parser.add_argument('--something', type=str, default=None, help='provide a arg')
    # 3. Parse Arguments
    args = parser.parse_args(args)

    return args, parser

def _general_parameters(parser):
    # 2. Add Argument
    parser.add_argument('--something', type=str, default=None, help='provide a string')
    parser.add_argument('--number', type=int, default=None, help='provide a integer')
    parser.add_argument('--output-folder', type=str, default=None, help='provide flder path')
    parser.add_argument('--dataset-folder', type=str, default=None, help='provide dataset path')
    parser.add_argument('--experiment-name', type=str, default=None, help='provide experiment-name')
    parser.add_argument('--hyper-opt', type=str, default=None, help='provide path to json file')


