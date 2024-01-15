# Knight's Tour Problem

## Introduction
This repository contains Python implementations for solving the Knight's Tour problem on an 8x8 chessboard, as part of CMPE 300: Analysis of Algorithms Project 3. The Knight's Tour is a classic problem involving moving a knight across the chessboard, visiting each square exactly once.

## Description
The project implements two different algorithms to solve the Knight's Tour:
- **Part 1**: A probabilistic approach where the knight's moves are chosen randomly.
- **Part 2**: An algorithm that combines random steps with deterministic backtracking.

## Installation
Make sure Python is installed on your system. Clone this repository to your local machine.

## Usage
The program can be run in two modes, corresponding to the two parts of the project:

### Part 1 - Probabilistic Approach
Run the program for Part 1 with:
```bash
python knights_tour.py part1
```
### Part 2 - Heuristic Backtracking
Run the program for Part 2 with:
```bash
python knights_tour.py part2
```
## Output
The program will execute the Knight's Tour 100,000 times for each specified p value in Part 1 and for each combination of p and k values in Part 2. The results include the number of successful tours and the probability of a successful tour.

## Contact
For any inquiries, please reach out to:
Ceylin Gebes - huriye.gebes@std.bogazici.edu.tr
Damla Kayikci - damla.kayikci@std.bogazici.edu.tr