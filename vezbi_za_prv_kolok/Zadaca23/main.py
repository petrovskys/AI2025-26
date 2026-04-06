from constraint import *

if __name__ == '__main__':

    bands = dict()

    band_info = input()
    while band_info != 'end':
        band, time, genre = band_info.split(' ')
        bands[band] = (genre, time)
        band_info = input()

    total_time=dict(

    )
    for key in bands.keys():
        if bands[key][1] not in total_time.keys():
            total_time[bands[key][1]]=int(bands[key][0])
        else:
            total_time[bands[key][1]]+=int(bands[key][0])
    variables=[]
    short_bands=[]

    for key in bands.keys():
        variables.append(key+" (('"+bands[key][1]+"', '"+bands[key][0]+"'))")
        if int(bands[key][0])<80:
            short_bands.append(key + " (('" + bands[key][1] + "', '" + bands[key][0] + "'))")


    domain = [f'S{i + 1}' for i in range(3)]

    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    for key,value in total_time.items():
        li=[]
        if value<=300 and value != 240:
            for keyb in bands.keys():
                if(bands[keyb][1]==key):
                    li.append(keyb+" (('"+bands[keyb][1]+"', '"+bands[keyb][0]+"'))")
            problem.addConstraint(AllEqualConstraint(),li)

    def only_one_twohour(x,y,band1,band2):
        nband1=band1.split(" ")[0]
        nband2=band2.split(" ")[0]
        if int(bands[nband1][0]) == int(bands[nband2][0]) == 120:
            return x!=y
        return True
    for i,band1 in enumerate(variables):
        for band2 in variables[i+1:]:
            problem.addConstraint(lambda x,y,z=band1,a=band2:only_one_twohour(x,y,z,a),[band1,band2])


    def max_five_short(stage, *args):
        return args.count(stage) <= 5


    for s in domain:
        problem.addConstraint(
            lambda *args, stage=s: max_five_short(stage, *args),
            short_bands
        )

    result = problem.getSolution()

    sorted_result = dict(sorted(result.items(), key=lambda x: int(x[0].split("Band")[1].split(" ")[0])))

    for k, v in sorted_result.items():
        print(f"{k}: {v}")
