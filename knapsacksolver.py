import numpy as np
from itertools import product

class KnapsackSolver:
    def __init__(self, num_variable):
        self.num_variable = num_variable
        self.constraint = None
        self.objective = None
        self.max = None
        self.solver = None
        self.solve_status = False
        self._optimal_cost = None
        self._optimal_choose = None
        
    # Util function
    def __check_num_variable(self, coefficient):    
        if coefficient != self.num_variable:
            print('The coefficient dimension is not equal to number of variable!')
            return False
        else:
            return True
        
    def __check_attributes(self):
        check_keys = ['num_variable','constraint','objective','max','solver']
        for key in check_keys:
            value = getattr(self, key, None)  
            if value is None:
                print(f"{key} is None")
                return False
        return True
    
    # Getter function 
    @property
    def optimal_cost(self):
        if self.solve_status and self._optimal_cost is not None:
            return self._optimal_cost
        else:
            raise Exception('Call the Solver !')

    @property
    def optimal_choose(self):
        if self.solve_status and self._optimal_choose is not None:
            return self._optimal_choose
        else:
            raise Exception('Call the Solver !')

    # Constraint 
    def add_weight(self, weight_coef):
        num_weight_coef = len(weight_coef)
        if self.__check_num_variable(num_weight_coef):
            self.constraint = np.array(weight_coef)
            print(f'Constraint function added {self.constraint} !')
        else:
            raise Exception('Please adjust your weight')

    # Objective
    def add_cost(self, cost_coef):
        num_cost_coef = len(cost_coef)
        if self.__check_num_variable(num_cost_coef):
            self.objective = np.array(cost_coef)
            print(f'Objective function added {self.objective} !')
        else:
            raise Exception('Please adjust your cost')

    # Bound
    def add_max_weight(self, max_weight):
        if isinstance(max_weight, int):
            self.max = max_weight
            print(f'Max Bound added {self.max} !')
        else:
            raise TypeError("max_weight must be an int")

    def add_solver(self, solver='brute_force'):
        if solver == 'brute_force':
            self.solver = np.array(list(product([0, 1], repeat=self.num_variable)))
            print(f'Solver added ({solver}) !')
        else:
            raise Exception('Please choose available solver')

    def solve(self):
        if self.__check_attributes():
            try:
                weights = np.dot(self.solver, self.constraint)
                costs = np.dot(self.solver, self.objective)

                weights[weights > self.max] = -1
                costs[weights == -1] = -1

                self._optimal_cost = np.max(costs)
                indices_max = np.where(costs == self._optimal_cost)[0]
                self._optimal_choose = self.solver[indices_max]

                self.solve_status = True

                print('Solve Successfuly!')
            except:
                raise Exception('Numpy calculation error')
        else:
            raise Exception('Some data or solver not defined yet')