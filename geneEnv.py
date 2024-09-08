import gymnasium as gym
from gymnasium import Env
from gymnasium.spaces import Box
from pig import pig
import numpy as np
import random

class geneEnv(Env):

    def __init__(self,geneNum,generation_popul,episode_len):
        self.generation_popul = generation_popul
        self.geneNum = geneNum
        self.action_space = []
        self.observaton_space = []
        self.state = self.make_generation()
        self.episode_len = episode_len
        

    def reset(self):
        self.state = self.make_generation()

    def get_obs(self):
        obs_list = []
        for pig in self.state:
            get_gene_list = np.array(pig.genes)
            obs_list.extend(np.ravel(get_gene_list,order='C'))

        for i in range(len(obs_list)):
            obs_list[i] = pig.alleleInt[obs_list[i]]
        obs_list = np.array([obs_list],dtype=int)

        return obs_list


    def step(self, action):#action은 세대 순서를 재배치한 벡터, action[i]=i허용
        nextGen = []
        self.episode_len -= 1

        for i in range(0,len(action)-1,2):
            for j in range(2):
                next_gene = []
                gene1 = self.state[i].trans()
                gene2 = self.state[i+1].trans()   

                for g in range(self.geneNum):
                    next_gene.append([gene1[g],gene2[g]])##2 allele
                child = pig(next_gene)
                nextGen.append(child)
        
        reward = 0
        totalPheno = []
        for g in range(self.numGen):
            phenoCnt = [0 for i in range(len(pig.phenoInt))]

            for babyPig in nextGen:
                phenoCnt[pig.phenoInt[babyPig.phenotype[g]]] += 1
            
            reward -= np.std(phenoCnt)
            totalPheno.append(phenoCnt)

        if self.episode_len <= 0:
            done = True
        else:
            done = False

        info = {}

        return self.get_obs(), reward, done, info
        

    def make_generation(self):
        ret_genereation = []

        for g in range(self.generation_popul):
            make_gene = []
            for i in range(2):
                make_gene.append(random.choice(pig.alleleList))
            make_gene = [make_gene]
            ret_genereation.append(pig(make_gene))
        
        return ret_genereation
        


env = geneEnv(1,10,100)
print(env)