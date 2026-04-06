from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    lecture_slots_AI = input()
    lecture_slots_ML = input()
    lecture_slots_R = input()
    lecture_slots_BI = input()

    AI_lectures_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_lectures_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_lectures_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                         "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_lectures_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_exercises_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_exercises_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_exercises_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Add the variables here--------------------
    variables_ai=[]
    variables_ml=[]
    variables_r=[]
    variables_bi=[]
    for i in range(int(lecture_slots_AI)):
        variables_ai.append("AI_lecture_"+str(i+1))
    for i in range(int(lecture_slots_ML)):
        variables_ml.append("ML_lecture_"+str(i+1))
    for i in range(int(lecture_slots_R)):
        variables_r.append("R_lecture_"+str(i+1))
    for i in range(int(lecture_slots_BI)):
        variables_bi.append("BI_lecture_"+str(i+1))
    problem.addVariables(variables_ai,AI_lectures_domain)
    problem.addVariables(variables_ml,ML_lectures_domain)
    problem.addVariables(variables_r,R_lectures_domain)
    problem.addVariables(variables_bi,BI_lectures_domain)

    # ---Add the constraints here----------------
    problem.addVariable("AI_exercises",AI_exercises_domain)
    problem.addVariable("ML_exercises",ML_exercises_domain)
    problem.addVariable("BI_exercises",BI_exercises_domain)

    all_variables=variables_ai+variables_ml+variables_r+variables_bi+["AI_exercises"]+["ML_exercises"]+["BI_exercises"]

    def no_overlap_constraint(lecture1,lecture2):
        t1 = lecture1.split("_")
        t2 = lecture2.split("_")
        day1,time1=t1[0],t1[1]
        day2,time2=t2[0],t2[1]

        if day1==day2:
            if int(time1)==int(time2):
                return False
            else:
                if abs(int(time1)-int(time2)) < 2:
                    return False

        return True
    for i,lecture1 in enumerate(all_variables):
        for lecture2 in all_variables[i+1:]:
            problem.addConstraint(lambda x,y: no_overlap_constraint(x,y),[lecture1,lecture2])

    def mashinsko_constraint(*lectures,exercise):
        for lecture in lectures:
            lecture_time=lecture.split("_")
            exercise_time=exercise.split("_")
            if lecture_time==exercise_time:
                return False
        return True
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)