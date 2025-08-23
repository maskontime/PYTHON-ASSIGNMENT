
"""
File Read & Write Challenge
This program reads a text file, applies a transformation to the content,
and writes the modified content to a new file.
"""

import argparse  # for command-line arguments

# Function to add line numbers to text
def add_line_numbers(lines):
    return [f"{i+1}: {line}" for i, line in enumerate(lines)]

def main():
    # --- Step 1: Setup argument parser ---
    parser = argparse.ArgumentParser(description="Read, transform, and write a text file")
    parser.add_argument("input", help="Path to input text file")
    parser.add_argument("output", help="Path to output file (new file to be created)")
    parser.add_argument(
        "--transform",
        choices=["linenumbers", "upper", "lower", "title"],
        default="linenumbers",
        help="Transformation to apply to file content"
    )

    args = parser.parse_args()

    # --- Step 2: Open input file safely ---
    with open(args.input, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    # --- Step 3: Apply transformation ---
    if args.transform == "linenumbers":
        transformed = add_line_numbers(lines)
    elif args.transform == "upper":
        transformed = [line.upper() for line in lines]
    elif args.transform == "lower":
        transformed = [line.lower() for line in lines]
    elif args.transform == "title":
        transformed = [line.title() for line in lines]
    else:
        transformed = lines  # default: no change

    # --- Step 4: Write to output file ---
    with open(args.output, "w", encoding="utf-8") as outfile:
        outfile.writelines(transformed)

    print(f"✅ File transformed using '{args.transform}' and saved to {args.output}")

if _name_ == "_main_":
    main()