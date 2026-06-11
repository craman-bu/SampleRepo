"""Add two numbers from the command line."""
""" Changing to test conflict with collabaator in github"

import argparse


def add_numbers(a: float, b: float) -> float:
    #add the numbers a and b
    return a + b


def main() -> None:
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()
    print(add_numbers(args.a, args.b))


if __name__ == "__main__":
    main()
