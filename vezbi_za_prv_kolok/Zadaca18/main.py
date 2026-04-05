from constraint import *

if __name__ == '__main__':
    solver=input()

    solver_map = {
        "BacktrackingSolver": BacktrackingSolver(),
        "RecursiveBacktrackingSolver": RecursiveBacktrackingSolver(),
        "MinConflictsSolver": MinConflictsSolver()
    }
    problem = Problem(solver_map[solver])
    for i in range(81):
        problem.addVariable(i,list(range(1,10)))

    for x in [0,9,18,27,36,45,54,63,72]:
        problem.addConstraint(AllDifferentConstraint(),list(range(x,x+9)))

    for x in range(9):
        problem.addConstraint(AllDifferentConstraint(), [x+i*9 for i in range(9)])

    for x in [0,27,54]:
        for y in [0,3,6]:
            unique=[]
            for i in range(3):
                for j in range(3):
                    unique.append(x+y+i*9+j)
            problem.addConstraint(AllDifferentConstraint(),unique)
    print(problem.getSolution())