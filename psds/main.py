import pandas as fd
from scipy.stats  import trim_mean
import numpy as np
import wquantiles
import os
import os.path as path
# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
# print(os.getcwd())
cwd = os.path.dirname(os.path.realpath(__file__))

state = fd.read_csv(path.join(cwd, 'data/state.csv'))
population = state['Population']
print('평균: ', population.mean())
print('중간값: ', population.median())
print('절사평균: ',trim_mean(population, 0.1)) # 10% 제외 
# 가중평균 / 가중중간값
print('가중평균: ', np.average(state['Murder.Rate'], weights=state['Population']))
print('가중중간값: ', wquantiles.median(state['Murder.Rate'], weights=state['Population']))