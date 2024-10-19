import gymnasium as gym
from gymnasium import Env
from gymnasium import spaces
from pig import pig
import numpy as np
import random

class geneEnv(Env):

    def __init__(self,geneNum,generation_popul,episode_len):
        self.generation_popul = generation_popul
        self.geneNum = geneNum

        action_ranges = [generation_popul] * (generation_popul * geneNum)
        observ_ranges = [len(pig.phenoInt)] * (generation_popul * geneNum)
        self.action_space = spaces.MultiDiscrete(action_ranges)
        self.observation_space = spaces.MultiDiscrete(observ_ranges)
        self.state = self.make_generation()
        self.episode_len = episode_len
        

    def reset(self,seed=None):
        if seed is not None:
            self.seed(seed)
        
        self.state = self.make_generation()
        info = {}

        return self.get_obs(), info

    def seed(self, seed=None):
        np.random.seed(seed)
        random.seed(seed)


    def get_obs(self):#표현형을 숫자 리스트로 변환
        obs_list = []

        for pigG in self.state:
            #print("debug",pigG.phenotype)
            for g in range(self.geneNum):
                obs_list.append(pigG.phenotype[g])

        for i in range(len(obs_list)):

            obs_list[i] = pig.phenoInt[obs_list[i]]

            #print(self.episode_len, obs_list[i])
        obs_list = np.array(obs_list,dtype=int)

        return obs_list


    def step(self, action):#action은 세대 순서를 재배치한 벡터, action[i]=i허용 #안겹치게 추가해야함

        nextGen = []
        self.episode_len -= 1

        for i in range(0,len(action)-1,2):
            for j in range(2):
                next_gene = []
                gene1 = self.state[action[i]].trans()
                gene2 = self.state[action[i+1]].trans()   

                for g in range(self.geneNum):
                    next_gene.append([gene1[g],gene2[g]])##2 allele
                child = pig(next_gene)
                nextGen.append(child)
        
        reward = 0
        totalPheno = []
        for g in range(self.geneNum):
            phenoCnt = [0 for i in range(len(pig.phenoInt))]

            for babyPig in nextGen:
                phenoCnt[pig.phenoInt[babyPig.phenotype[g]]] += 1
            
            #reward -= np.std(phenoCnt)
            
            for goals in pig.goalPheno[g]:
                reward += phenoCnt[goals]
            
                
            totalPheno.append(phenoCnt)

        if self.episode_len <= 0:
            done = True
        else:
            done = False
        truncated = False
        info = {}

        return self.get_obs(), reward, done, truncated, info
        

    def make_generation(self):
        ret_genereation = []

        for i in range(self.generation_popul):
            make_gene = []
            for g in range(self.geneNum):
                make_one_gene = []
                for j in range(2):
                    make_one_gene.append(random.choice(pig.alleleList[g]))
                make_gene.append(make_one_gene)
            
            ret_genereation.append(pig(make_gene))
        
        return ret_genereation
        
