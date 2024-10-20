import gymnasium as gym
from gymnasium import Env
from gymnasium import spaces
from pig import pig
import numpy as np
import random
from geneEnv import geneEnv

class flockEnv(geneEnv):#geneEnv 상속. step만 오버로딩

    def step(self):#action은 세대 순서를 재배치한 벡터, action[i]=i허용 #안겹치게 추가해야함
        
        
        rewards = []
        for pigG in self.state:
            reward = 0
            for g in range(self.geneNum):
                if pig.phenoInt[pigG.phenotype[g]] in pig.goalPheno[g]:
                    reward += 1
            rewards.append(reward)
            
        sorted_pigs = [pig for _, pig in sorted(zip(rewards, self.state), key=lambda x: x[0], reverse=True)]
            
        
        nextGen = []
        self.episode_len -= 1

        for i in range(0,len(sorted_pigs)-1,2):
            for j in range(2):
                next_gene = []
                gene1 = sorted_pigs[i].trans()
                gene2 = sorted_pigs[i+1].trans()   

                for g in range(self.geneNum):
                    next_gene.append([gene1[g],gene2[g]])##2 allele
                child = pig(next_gene)
                nextGen.append(child)
        
        

        if self.episode_len <= 0:
            done = True
        else:
            done = False
        truncated = False
        info = {}
        total_reward = sum(rewards)
        self.state = nextGen

        return self.get_obs(), total_reward, done, truncated, info
