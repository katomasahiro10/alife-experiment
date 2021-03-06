import random
from setting import *

class Task_without_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]

    def get_reward(self, no:int) -> float:
        return self.rewards[no]

    def dotask(self,agent):
        total_reward = 0
        agent.history = ''
        agent.histories = ['','','','','','']
        for No in range(6):
            agent.reset()

            if No == 0:
                self.rewards = [1.0, 0.3, 0.0]
            elif No == 1:
                self.rewards = [1.0, 0.0, 0.3]
            elif No == 2:
                self.rewards = [0.3, 1.0, 0.0]
            elif No == 3:
                self.rewards = [0.0, 1.0, 0.3]
            elif No == 4:
                self.rewards = [0.3, 0.0, 1.0]
            elif No == 5:
                self.rewards = [0.0, 0.3, 1.0]

            for step in range(STEP_NUM):

                #question phase
                input_vector = [1,0,0,0,0,0,0,0]
                output = agent.get_output_with_update(input_vector)
                output_vec = [0,0,0]
                output_vec[output.index(max(output))] = 1
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
                output = agent.get_output_with_update(feedback_vector)


        return total_reward

class Task_with_accident:
    def __init__(self):
        self.rewards = [0.0, 0.3, 1.0]

    def get_reward(self, no:int) -> float:
        return self.rewards[no]

    def dotask(self,agent):
        total_reward = 0
        agent.histories = ['','','','','','']
        for No in range(6):
            agent.reset()

            if No == 0:
                self.rewards = [1.0, 0.3, 0.0]
                self.rewards2 = [0.0, 0.3, 0.0]
                self.accident_step = random.randint(5,8)
            elif No == 1:
                self.rewards = [1.0, 0.0, 0.3]
                self.rewards2 = [0.0, 0.0, 0.3]
                self.accident_step = random.randint(5,8)
            elif No == 2:
                self.rewards = [0.3, 1.0, 0.0]
                self.rewards2 = [0.3, 0.0, 0.0]
                self.accident_step = random.randint(5,8)
            elif No == 3:
                self.rewards = [0.0, 1.0, 0.3]
                self.rewards2 = [0.0, 0.0, 0.3]
                self.accident_step = random.randint(5,8)
            elif No == 4:
                self.rewards = [0.3, 0.0, 1.0]
                self.rewards2 = [0.3, 0.0, 0.0]
                self.accident_step = random.randint(5,8)
            elif No == 5:
                self.rewards = [0.0, 0.3, 1.0]
                self.rewards2 = [0.0, 0.3, 0.0]
                self.accident_step = random.randint(5,8)

            for step in range(STEP_NUM):
                
                #question phase
                input_vector = [1,0,0,0,0,0,0,0]
                output = agent.get_output_with_update(input_vector)
                output_vec = [0,0,0]
                output_vec[output.index(max(output))] = 1
                previous_output = output_vec

                if(step != self.accident_step and step != self.accident_step+1):
                    reward = self.rewards[ output_vec.index(max(output_vec)) ]
                else:
                    reward = self.rewards2[ output_vec.index(max(output_vec)) ]

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
                output = agent.get_output_with_update(feedback_vector)

            if(agent.histories[No][self.accident_step] == 'x' and \
                agent.histories[No][self.accident_step+1] == 'c'):
                agent.histories[No] += 'S'
                total_reward += 2.0

        return total_reward
