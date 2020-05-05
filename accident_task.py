import random
from enum import IntEnum

from setting import *

class Rule(IntEnum):
    I   = 1
    II  = 2
    III = 3
    IV  = 4
    V   = 5
    VI  = 6


class Task_without_accident:
    def __init__(self):
        self.rule = Rule(random.randint(1,6))
        print(self.rule)

    def get_reward(self, action: int, is_accident:bool = False) -> float:
        if(self.rule == Rule.I):
            reward_vec = [1.0, 0.3, 0.0]
        elif(self.rule == Rule.II):
            reward_vec = [1.0, 0.0, 0.3]
        elif(self.rule == Rule.III):
            reward_vec = [0.3, 1.0, 0.0]
        elif(self.rule == Rule.IV):
            reward_vec = [0.0, 1.0, 0.3]
        elif(self.rule == Rule.V):
            reward_vec = [0.3, 0.0, 1.0]
        elif(self.rule == Rule.VI):
            reward_vec = [0.0, 0.3, 1.0]

        if(is_accident):
            reward_vec = [0.0 if i == 1.0 else i for i in reward_vec]

        print(reward_vec)

        return reward_vec[ action ]

    def execute_task(self, agent) -> int:
        total_reward = 0
        agent.history = ''

        for i in range(STEP_NUM):
            #question phase
            input_vector = [1,0,0,0,0,0,0,0]
            tmp_output = agent.get_output_with_update(input_vector)
            output_vec = [0,0,0]
            output_vec[tmp_output.index(max(tmp_output))] = 1
            previous_output = output_vec
            reward = self.rewards[ output_vec.index(max(output_vec)) ]
            total_reward += reward

            if(reward == 0.0):
                agent.histories[No] += 'x'
                feedback = [1,0,0]
            elif(reward == 0.3):
                agent.histories[No] += 'c'
                feedback = [0,1,0]
            elif(reward == 1.0):
                feedback = [0,0,1]
                agent.histories[No] += 'o'

            #feedback phase
            feedback_vector=[0,1]
            feedback_vector += previous_output
            feedback_vector += feedback
            tmp_output = agent.get_output_with_update(feedback_vector)


        return total_reward

if __name__=='__main__':
    t = Task_without_accident()
    print(t.rule)
    reward = t.get_reward(1)
    print(reward)
    reward = t.get_reward(1,True)
    print(reward)
