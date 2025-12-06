# Advent of Code
Jack Osmond's solutions to [Advent of Code](https://adventofcode.com)

## Installation and running

### Initial setup
In Git Bash, navigate to where you would like to clone this repository, and run:

```shell
git clone https://github.com/JWOsmond/advent-of-code.git
```

Enter the repository:

```shell
cd advent-of-code
```

and run:

```shell
conda env create -f environment.yaml
```

Your setup is now complete.

### Running the project

When running the project, you need to ensure you have the right packages loaded in your working environment, so you must activate the environment you created in the previous step. This can be done with the following command in Git Bash:

```shell
conda activate advent-of-code-env
```

You can run desired scripts now with the command, e.g.:

```shell
python 2025/day-01-secret-entrance.py
```

## Data

Datasets need to be downloaded from the problem page and saved to a file name specified in the README within a given year's folder. For example, `2025/day-01-secret-entrance.py` requires there to be a file named `directions.txt` inside the `2025/input` directory. You can generate your own personalised problem dataset on the page for that problem, or copy the example dataset for each problem to the file with the right name.