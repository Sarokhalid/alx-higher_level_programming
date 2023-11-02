#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)
    arg_str = "argument" if num_args == 1 else "arguments"
    print(f"{num_args} {arg_str}:", end="")
    print("." if num_args == 0 else "")
    for i, arg in enumerate(args):
        print(f"{i+1}: {arg}")
