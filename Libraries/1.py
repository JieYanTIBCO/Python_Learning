import argparse

parse = argparse.ArgumentParser(description="this is test")

parse.add_argument("parameter1", help="this is parameter1")

args = parse.parse_args()

print(args.parameter1)
