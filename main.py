import sys
from classes.app import App

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print(" Incorrect usage. It should be: python3 script.py num_of_cities[int], "
              "num_of_generations[int], show_map[bool]")
        sys.exit(1)

    # Extract command-line arguments
    num_of_cities = int(sys.argv[1])
    num_of_generations = int(sys.argv[2])
    if sys.argv[3] == 'True':
        show_map = True
    else:
        show_map = False
    app = App(num_of_cities, num_of_generations, show_map)
    app.run_app()
