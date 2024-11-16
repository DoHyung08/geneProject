import gymnasium as gym
from gymnasium import Env
from gymnasium import spaces
from pig import pig
import numpy as np
import random
from geneEnv import geneEnv

class ratioEnv(geneEnv):#geneEnv 상속. step만 오버로딩
    
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
            
            
            sumCnt = sum(phenoCnt)
            phenoRatio = [100 * x / sumCnt for x in phenoCnt]
            
            for i in range(len(pig.phenoInt)):
                reward -= (phenoRatio[i] - pig.goalRatio[i])**2 + (phenoRatio[i] - pig.goalRatio[i])
                
            totalPheno.append(phenoCnt)
        reward /= self.geneNum * len(pig.phenoInt)
        
        if reward > -30:
            done = True

        if self.episode_len <= 0:
            done = True
        else:
            done = False
        truncated = False
        info = {}
        self.state = nextGen

        return self.get_obs(), reward, done, truncated, info