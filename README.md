# 🧮 knapsack-solver

A simple Python class to solve the **0-1 Knapsack problem** using brute-force search.

> ⚠️ This project is for my educational purposes.
>
> - How combinatorial problems work  
> - Numpy operations and vectorized logic  
> - Class design in Python  


## ✨ Features

- ✅ Clean class-based design  
- 🔍 Getter methods for easy result access  
- ⚙️ Constraint, Objective, and Solver setup via method calls  
- ⚡ Uses NumPy for efficient vectorized operations  


## Installation
Clone the repo or copy the `knapsack_solver.py` file.

## Notes
- Suitable for small problem sizes (due to brute-force complexity).
- Future work: implement dynamic programming or heuristic solvers.

## Usage
```python
import numpy as np
from knapsack_solver import KnapsacSolver

num_variable = 10 # ( < 30 or computer expolde 🤣) 
cost = np.random.randint(low=10, high=100, size=num_variable)
weight = np.random.randint(low=10, high=100, size=num_variable)
max_weight = 100

solver = KnapsacSolver(num_variable)
solver.add_cost(cost)
solver.add_weight(weight)
solver.add_max_weight(max_weight)

# Solver (Only brute_force 😢)
solver.add_solver(solver='brute_force')

# call solver
solver.solve()

optimal_cost = solver.optimal_cost
optimal_choose = solver.optimal_choose

print(f"Optimal cost: {optimal_cost}")
print("Optimal selection(s):")
for selection in optimal_choose:
    print(selection)
