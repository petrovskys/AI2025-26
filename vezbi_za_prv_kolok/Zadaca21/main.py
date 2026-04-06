from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    variables = [paper+" ("+papers[paper]+")" for paper in papers.keys()]

    count= dict()

    for paper,type in papers.items():
        if type not in count.keys():
            count[type]=1
        else:
            count[type]+=1

    domain = [f'T{i + 1}' for i in range(num)]
    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    def variable_count_constraint(*args):
        for t in domain:
            if args.count(t)>4 :
                return False
        return True
    for type,amount in count.items():
        li=[]
        if amount <= 4:
            for name,typep in papers.items():
                if(type==typep):
                    li.append(name+" ("+type+")")
            problem.addConstraint(AllEqualConstraint(),li)


    problem.addConstraint(variable_count_constraint,variables)

    result = problem.getSolution()
    sorted_solution = dict(sorted(result.items(), key=lambda x: int(x[0].split("Paper")[1].split(" ")[0])))

    # Add the required print section
    for k,v in sorted_solution.items():
        print(k+": "+v)
