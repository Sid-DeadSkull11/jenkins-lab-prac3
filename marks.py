import sys

if __name__ == "__main__":
    # Check if exactly 3 marks are provided
    if len(sys.argv) < 4:
        print("Error: Missing parameters. Please provide marks for 3 subjects.")
        sys.exit(1)

    try:
        # Read parameters from command line arguments
        sub1 = float(sys.argv[1])
        sub2 = float(sys.argv[2])
        sub3 = float(sys.argv[3])
    except ValueError:
        print("Error: Marks must be valid numbers.")
        sys.exit(1)

    # Calculate Total and Average
    total = sub1 + sub2 + sub3
    average = total / 3

    print("\n--- Student Performance Report ---")
    print(f"Subject 1: {sub1}")
    print(f"Subject 2: {sub2}")
    print(f"Subject 3: {sub3}")
    print(f"Total Marks: {total:.2f} / 300")
    print(f"Average Mark: {average:.2f}")
    print("----------------------------------")

    # Pass Criterion: Min 40 in each subject AND min 50 average total
    if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and average >= 50:
        print("Final Status: PASS")
    else:
        print("Final Status: FAIL")
