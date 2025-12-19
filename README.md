# Matchstick Math Puzzle Solver & Quiz Generator

A Python-powered matchstick puzzle engine that models digits as 7-segment sticks and explores **all possible one-stick moves** (move, add, or remove) to fix or create math equations. Perfect for:

* Generating brain-busting **math quizzes** where you correct equations by moving a single matchstick
* Exploring the fascinating world of **matchstick arithmetic puzzles**
* Building automated puzzle generators, solvers, and challenge platforms
* Learning constraint-solving and combinatorial logic through code

---

## Features

* Models digits 0–9 as classic 7-segment sticks
* Enumerates all valid single-stick transformations (move/add/remove) between digits
* Checks equations for potential fixes by applying those transformations
* Supports analyzing and fixing `i + j = z` style puzzles
* Outputs detailed explanations of moves that fix broken equations
* Easily extensible for multi-digit numbers and complex matchstick math

---

## Why?

Matchstick puzzles combine logic, spatial reasoning, and creativity — this project turns those into programmable, automated challenges you can generate and solve systematically.

---

## Usage

Run the main script to generate puzzles and save solutions to a file. Customize it to generate quizzes, integrate into games, or extend with new operations!

---

## Tech Stack

* Python 3
* Uses 7-segment digit representation
* JSON for move storage and reuse

---

Feel free to tweak or let me know if you want a shorter or more casual version!
