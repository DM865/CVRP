#!/usr/bin/python3

import sys
import os
import argparse
import time

import data
import solution
import solverCH
import solverLS
import utilities

# @my_logger
# @my_timer


def solve(instance, config):
    t0 = time.perf_counter()
    ch = solverCH.ConstructionHeuristics(instance)
    sol = ch.construct(config.time_limit-(time.perf_counter() - t0)
                       )  # returns an object of type Solution

    ls = solverLS.LocalSearch(instance)
    sol = ls.local_search(sol, config.time_limit-(time.perf_counter() - t0)
                          )  # returns an object of type Solution
    return sol


def main(argv):

    parser = argparse.ArgumentParser()

    parser.add_argument('-o', action='store',
                        dest='output_file',
                        help='The file where to save the solution and, in case, plots')

    parser.add_argument('-t', action='store',
                        dest='time_limit',
                        type=int,
                        required=True,
                        help='The time limit')

    parser.add_argument('instance_file', action='store',
                        help='The path to the file of the instance to solve')

    config = parser.parse_args()

    print('instance_file    = {!r}'.format(config.instance_file))
    print('output_file      = {!r}'.format(config.output_file))
    print('time_limit       = {!r}'.format(config.time_limit))

    instance = data.Data(config.instance_file)
    instance.short_info()
    # if config.output_file is not None:
    #    instance.plot_points(config.output_file+'.png');
    # instance.show()

    sol = solve(instance, config)

    assert sol.valid_solution()
    if config.output_file is not None:
        sol.plot_routes(config.output_file+'_sol'+'.png')
        sol.write_to_file(config.output_file+'.sol')
    print("{} routes with total cost {:.1f}"
          .format(len(sol.routes), sol.cost()))

    #sol.plot_routes()  # remove this before submission


if __name__ == "__main__":
    main(sys.argv[1:])
