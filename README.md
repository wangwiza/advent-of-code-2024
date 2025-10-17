# Advent of Code 2024

This repository contains my solutions for the Advent of Code 2024 programming puzzles. Each day's solution is contained within its own directory and can be run independently.

-----

## Day 1: Historian Hysteria

### Problem Description

The `historian_hysteria.py` script solves two problems related to analyzing pairs of numbers from an input file (`input.txt`):

1.  **Sum of Distances**: Calculates the sum of absolute differences between two sorted lists of numbers.
2.  **Sum of Similarity Scores**: Computes a similarity score based on the frequency of numbers in the second list.

### Running the Solution

```bash
python day1/historian_hysteria.py
```

-----

## Day 2: Red-Nosed Reports

### Problem Description

`red_nosed_reports.py` processes a file of numerical reports (`input.txt`) to determine how many are "safe" based on two criteria:

1.  **Standard Safe Reports**: Checks if a report's numbers are in strictly ascending or descending order.
2.  **Dampened Safe Reports**: Checks if a report becomes strictly ascending or descending after removing one number.

### Running the Solution

```bash
python day2/red_nosed_reports.py
```

-----

## Day 3: Mull It Over

### Problem Description

The script `mull_it_over.py` is designed to parse a text file (`input.txt`) and calculate the sum of products from `mul(x,y)` expressions. It includes two functionalities:

1.  **`mull_it_over()`**: Calculates the sum of all `mul(x,y)` expressions.
2.  **`mull_it_over2()`**: Calculates the sum of `mul(x,y)` expressions, but ignores any that appear after a `don't()` command and before a `do()` command.

### Running the Solution

```bash
python day3/mull_it_over.py
```

-----

## Day 4: Ceres Search

### Problem Description

`ceres_search.py` contains two functions that search for patterns within a grid of characters defined in `input.txt`:

1.  **`ceres_search()`**: Counts the occurrences of the "XMAS" pattern in all 8 directions (horizontally, vertically, and diagonally).
2.  **`ceres_search2()`**: Counts occurrences of a specific 3x3 "XMAS" pattern where 'A' is in the center and 'M' and 'S' are on the diagonals.

### Running the Solution

```bash
python day4/ceres_search.py
```

-----

## Day 5: Print Queue

### Problem Description

The `print_queue.py` script processes a set of printing queue updates from `input.txt` based on a given set of page ordering rules. It includes:

1.  **`print_queue()`**: Verifies if updates adhere to the ordering rules and calculates a sum based on the median page number of valid updates.
2.  **`print_queue2()`**: Corrects updates that violate the ordering rules and calculates a sum based on the median page of the corrected updates.

### Running the Solution

```bash
python day5/print_queue.py
```

-----

## Day 6: Guard Gallivant

### Problem Description

`guard_gallivant.py` simulates a guard's movement on a 2D map from `input.txt`. The guard starts at `^` and moves, marking visited cells. The script has two main functions:

1.  **`guard_gallivant()`**: Calculates the number of unique cells visited by the guard.
2.  **`guard_gallivant2()`**: Determines the number of cells that, if turned into obstacles, would cause the guard to enter an infinite loop.

### Running the Solution

```bash
python day6/guard_gallivant.py
```

-----

## Day 7: Bridge Repair

### Problem Description

The `bridge_repair.py` script reads a file (`input.txt`) of targets and numbers. It uses backtracking to determine if a target can be reached by applying a series of operations (addition, multiplication, and concatenation) to the numbers.

### Running the Solution

```bash
python day7/bridge_repair.py
```

-----

## Day 8: Resonant Collinearity

### Problem Description

`resonant_collinearity.py` analyzes a map from `input.txt` containing "antennas" of different frequencies. It identifies "antinodes" based on the collinear arrangement of antennas of the same frequency. Two versions of the logic are provided:

1.  **`resonant_collinearity()`**: Finds antinodes formed by pairs of antennas.
2.  **`resonant_collinearity2()`**: Finds antinodes formed by pairs of antennas and their "harmonics" along the same line.

### Running the Solution

```bash
python day8/resonant_collinearity.py
```

-----

## Day 9: Disk Fragmenter

### Problem Description

The `disk_fragmenter.py` script processes a "disk map" from `input.txt`, which represents fragmented files on a disk. Two different algorithms are implemented to defragment the disk:

1.  **`disk_fragmenter()`**: A simple defragmentation algorithm.
2.  **`disk_fragmenter2()`**: A more complex algorithm that reorders files based on size.

### Running the Solution

```bash
python day9/disk_fragmenter.py
```

-----

## Day 10: Hoof It

### Problem Description

`hoof_it.py` is a script that solves a pathfinding puzzle on a 2D "hike map" (`input.txt`). It uses a backtracking algorithm to find and count valid "hikes" which are paths of increasing altitude from 0 to 9. Two variations are provided:

1.  **`hoof_it()`**: Counts the number of unique summits reached.
2.  **`hoof_it2()`**: Counts the total number of valid paths, regardless of the summit.

### Running the Solution

```bash
python day10/hoof_it.py
```

-----

## Day 11: Plutonian Pebbles

### Problem Description

The `plutonian_pebbles.py` script simulates the behavior of "Plutonian pebbles" as described in `input.txt`. The pebbles undergo transformations based on a set of rules over a number of "blinks." Two different simulation approaches are implemented:

1.  **`plutonian_pebbles()`**: A simulation using a simple list.
2.  **`plutonian_pebbles2()`**: A more optimized simulation using a frequency counter.

### Running the Solution

```bash
python day11/plutonian_pebbles.py
```

-----

## Day 12: Garden Groups

### Problem Description

`garden_groups.py` analyzes a 2D "garden map" from `input.txt` to calculate a total "cost" based on contiguous regions of the same character. The cost for each region is determined by its area multiplied by its perimeter.

### Running the Solution

```bash
python day12/garden_groups.py
```
