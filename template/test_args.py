import argparse
import template.CL_arguments_test
import template.runner
import shutil
import json

import argparse
import os

args=None
args, parser = template.CL_arguments_test.parse_arguments(args)

# # just tests if how I can access the CL-arguments
# if args.__dict__["number"] is None:
#     print("no Number")
# if args.__dict__["number"] is not None:
#     print("your number: ", args.number)
#
# print(parser)
# print(args)
#
# output_folder = args.__dict__["output_folder"]
# experiment_name = args.__dict__["experiment_name"]
# dataset = os.path.basename(os.path.normpath(args.__dict__['dataset_folder']))
#
# #creat a path to a folder
# path = os.path.join(*[output_folder, experiment_name, dataset])
# print("path: ", path)
#
# # create the folder
# if not os.path.exists(path):
#     os.makedirs(path)
#
# # deleat the folder
# shutil.rmtree(path)
#
# # create dictionary
# dict = {"one":1, "two":2, "three":3}
#
# import _pickle as pickle
# file_name = os.path.join(*[output_folder, experiment_name, "best_param.txt"])
# f = open(file_name, "w+")
# f.write(json.dumps(dict))
# f.close
print(args.__dict__["hyper_opt"])
with open(args.__dict__["hyper_opt"], 'r') as f:
    search_space = json.loads(f.read())

print(search_space)

# class test_args:
#     parser = None
#     def main(self, args=None):
#         try:
#             args, test_args.parser = template.CL_arguments_test.parse_arguments(args)
#         except:
#             print("error 1")
#         try:
#             print(test_args.parser)
#         except:
#             print("error 2")
#         try:
#             print(args.arg1)
#         except:
#             print("Error 3")
#
#         #if args.arg1 is not None:
#             #print("yesss")
#
#
# if __name__ == "__main__":
#     test_args().main()


