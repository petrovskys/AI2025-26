from searching_framework import Problem, astar_search
class ChoveceKonSvojotDom(Problem):
    def __init__(self,initial,walls,n,goal):
        super().__init__(initial,goal)
        self.walls=walls
        self.n=n
    def goal_test(self, state):
        (chovekX,chovekY)=state

        return (chovekX,chovekY)==self.goal

    def successor(self, state):
        succ={}
        (x,y)=state
        moves={
            "Right 2":(+2,0),
            "Right 3":(+3,0),
            "Left":(-1,0),
            "Up":(0,+1),
            "Down":(0,-1)
        }

        for move,(nx,ny) in moves.items():
            newx=x+nx
            newy=y+ny

            if not ((0<=newx<n) and (0<=newy<n)):
                continue
            if (newx,newy) in self.walls:
                continue

            if move=="Right 2":
                if (newx-1,newy) in self.walls:
                    continue

            if move=="Right 3":
                if (newx-1,newy) in self.walls or (newx-2,newy) in self.walls:
                    continue
            succ[move]=(newx,newy)



        return succ


    def h(self,node):
        (x,y)=node.state
        (xn,yn)=self.goal

        return abs(xn-x)//3+abs(yn-y)

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    n=int(input())
    wall=int(input())
    walls=()
    for i in range(wall):
        walls+=(tuple(map(int,input().split(","))),)
    (chovekX,chovekY)=tuple(map(int,input().split(",")))
    (kukjaX,kukjaY)=tuple(map(int,input().split(",")))
    initial=(chovekX,chovekY)
    goal=(kukjaX,kukjaY)
    problem=ChoveceKonSvojotDom(initial,walls,n,goal)
    result=astar_search(problem,problem.h)
    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")