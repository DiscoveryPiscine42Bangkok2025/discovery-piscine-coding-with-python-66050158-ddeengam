import sys

if len(sys.argv) == 1:
    print("none")
else:
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")
    for arg in params:
        print(f"{arg}: {len(arg)}")