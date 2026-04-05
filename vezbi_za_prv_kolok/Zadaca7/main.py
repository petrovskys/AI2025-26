from searching_framework import *


class Robot(Problem):
    def __init__(self, initial, m1_pos, m2_pos, m1_steps, m2_steps, walls):
        super().__init__(initial)
        self.m1_pos = m1_pos
        self.m2_pos = m2_pos
        self.m1_steps = m1_steps
        self.m2_steps = m2_steps
        self.walls = walls

    def goal_test(self, state):
        _, _, _, collectm1, collectm2, repair1_done, repair2_done = state
        return repair1_done and repair2_done

    def successor(self, state):
        (x, y), repair1_progress, repair2_progress, collectm1, collectm2, repair1_done, repair2_done = state
        succ = {}
        moves = {"Up": (0,+1), "Down": (0,-1), "Left": (-1,0), "Right": (+1,0)}

        for move, (nx, ny) in moves.items():
            new_x, new_y = x+nx, y+ny
            if new_x < 0 or new_x > 9 or new_y < 0 or new_y > 9:
                continue
            if (new_x, new_y) in self.walls:
                continue


            new_r1_progress = 0
            new_r2_progress = 0

            new_collectm1 = collectm1
            new_collectm2 = collectm2

            if (new_x, new_y) in collectm1:
                ls = list(collectm1)
                ls.remove((new_x, new_y))
                new_collectm1 = tuple(sorted(ls))


            elif (new_x, new_y) in collectm2 and repair1_done:
                ls = list(collectm2)
                ls.remove((new_x, new_y))
                new_collectm2 = tuple(sorted(ls))

            succ[move] = (
                (new_x, new_y),
                new_r1_progress,
                new_r2_progress,
                new_collectm1,
                new_collectm2,
                repair1_done,
                repair2_done
            )


        if (x, y) == self.m1_pos and len(collectm1) == 0 and not repair1_done:
            new_progress = repair1_progress + 1
            if new_progress == self.m1_steps:

                succ["Repair"] = (x, y), 0, 0, collectm1, collectm2, True, repair2_done
            else:
                succ["Repair"] = (x, y), new_progress, repair2_progress, collectm1, collectm2, False, repair2_done


        if (x, y) == self.m2_pos and len(collectm2) == 0 and repair1_done and not repair2_done:
            new_progress = repair2_progress + 1
            if new_progress == self.m2_steps:
                succ["Repair"] = (x, y), 0, 0, collectm1, collectm2, repair1_done, True
            else:
                succ["Repair"] = (x, y), repair1_progress, new_progress, collectm1, collectm2, repair1_done, False

        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())
    parts_M1 = int(input())
    to_collect_M1 = tuple(sorted([tuple(map(int, input().split(','))) for _ in range(parts_M1)]))
    parts_M2 = int(input())
    to_collect_M2 = tuple(sorted([tuple(map(int, input().split(','))) for _ in range(parts_M2)]))

    walls = [(4,0),(5,0),(7,5),(8,5),(9,5),(1,6),(1,7),(0,6),(0,8),(0,9),(1,9),(2,9),(3,9)]


    initial = robot_start_pos, 0, 0, to_collect_M1, to_collect_M2, False, False

    problem = Robot(initial, M1_pos, M2_pos, M1_steps, M2_steps, walls)
    result = breadth_first_graph_search(problem)

    if result is None:
        print("No Solution!")
    else:
        print(result.solution())