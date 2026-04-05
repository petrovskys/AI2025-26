from searching_framework import Problem, astar_search

class Climb(Problem):
    def __init__(self,initial,allowed):
        super().__init__(initial)
        self.allowed=allowed
    def goal_test(self, state):
        man,house,_=state

        return man == house

    def successor(self,state):
        succ = {}
        (mx,my),(hx,hy),d = state
        moves = {
            "Wait" : (0,0),
            "Up 1" : (0,+1),
            "Up 2" : (0,+2),
            "Up-right 1" : (+1,+1),
            "Up-right 2" : (+2,+2),
            "Up-left 1" : (-1,+1),
            "Up-left 2" : (-2,+2),
        }
        for move,(x,y) in moves.items():
            nmx,nmy=x+mx,y+my
            if d == 'left':
                nhx=hx-1
            else:
                nhx=hx+1
            newdir=d
            if nhx == 0:
                newdir='right'
            elif nhx == 4:
                newdir='left'
            if (nmx,nmy) not in self.allowed and (nmx,nmy)!=(nhx,hy):
                continue
            if not (0<=nmx<5 and 0<=nmy<9):
                continue


            succ[move]=(nmx,nmy),(nhx,hy),newdir
        return succ
    def h(self,node):
        (mx,my),(hx,hy),_=node.state
        return abs((hy-my))/2
    def actions(self, state):
        return self.successor(state).keys()
    def result(self,state,action):
        return self.successor(state)[action]
if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]

    man = tuple(map(int,input().split(",")))
    house = tuple(map(int,input().split(",")))
    direction=input()
    initial = man,house,direction
    problem = Climb(initial,allowed)
    result = astar_search(problem,problem.h)
    if result is None:
        print("No Solution!")
    else: print(result.solution())