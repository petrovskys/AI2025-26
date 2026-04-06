from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # Add the domains
    problem.addVariable("Marija_attendance", [0,1])
    problem.addVariable("Simona_attendance", [1])
    problem.addVariable("Petar_attendance", [0,1])
    problem.addVariable("time_meeting", [13,14,16,19])
    petar_sloboden=[12,13,16,17,18,19]
    maria_slobodna=[14,15,18]
    # ----------------------------------------------------

    # ---Add the constraints----------------
    problem.addConstraint(MinSumConstraint(1),["Marija_attendance","Petar_attendance"])
    problem.addConstraint(lambda x,z,slots=(12,13,16,17,18,19): x==0 or z in slots,["Petar_attendance","time_meeting"])
    problem.addConstraint(lambda x,y,slots=(14,15,18): x==0 or y in slots, ["Marija_attendance","time_meeting"])

    # ----------------------------------------------------


    keys = ["Simona_attendance", "Marija_attendance", "Petar_attendance", "time_meeting"]

    for solution in problem.getSolutions():
        print({k: solution[k] for k in keys})