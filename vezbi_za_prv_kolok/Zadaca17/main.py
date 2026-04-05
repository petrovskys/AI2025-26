from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))

    problem.addConstraint(AllDifferentConstraint(),variables)

    problem.addConstraint(lambda B,D,E: B%2==1 and D%2==1 and E%2==1,["B","D","E"])
    problem.addConstraint(MinSumConstraint(100),["A","B","C"])
    problem.addConstraint(ExactSumConstraint(150),["D","E"])
    problem.addConstraint(lambda F: (F%10)%4==0,["F"])






    print(problem.getSolution())