import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics

class CCTVModel:
    def __init__(self):
        self._context = None
        self._fname = None

    @property
    def context(self) -> object:
        return self._context
    @context.setter
    def context(self, context):
        self._context = context

    @property
    def fname(self) -> object:
        return self._fname
    @fname.setter
    def fname(self, fname):
        self._fname = fname

    def new_file(self) -> str:
        return self._context + self._fname

    def new_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8')

    def csv_to_dfame(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='UTF-8')

    def xls_to_dfame(self, header, usecols) -> object:
        file = self.new_file()
        return pd.read_excel(file, encoding='UTF-8', header=header, usecols=usecols)

"""
    여기서부터 다시 작성해야 함.... 
    
    def hook_process(self)->object:
        self._context='./data/'
        self._fname = 'CCTV_in_Seoul.csv'
        cctv = self.new_dframe()
        cctv_idx = cctv.columns
        self.fname = 'population_in_Seoul.xls'
        pop = self.xls_to_dfame(2,'B,D,G,J,N')
        pop_idx = pop.columns
        print(pop_idx)
"""

    # hook_process(self)->object: 를 create_cctv_pop(self) -> object: 로 바꾸었음.
    def create_cctv_pop(self)->object:
        self._context='./data/'
        self._fname = 'CCTV_in_Seoul.csv'
        cctv = self.new_dframe()
        cctv_idx = cctv.columns
        self.fname = 'population_in_Seoul.xls'
        pop = self.xls_to_dfame(2,'B,D,G,J,N')
        pop_idx = pop.columns

        #print(pop_idx)

        cctv.rename(columns={cctv.columns[0]: '구별'}, inplace = True)
        pop.rename(columns={pop.columns[0]:'구별',
                            pop.columns[1]:'인구수',
                            pop.columns[2]:'한국인',
                            pop.columns[3]:'외국인',
                            pop.columns[4]:'고령자'}, inplace = True)

        pop.drop([0], inplace=True)
        pop.drop([26], inplace=True)

        pop['외국인비율'] = pop['외국인']/pop['인구수']*100
        pop['고령자비율'] = pop['고령자']/pop['인구수']*100

        cctv.drop(['2013년도 이전', '2014년','2015년','2016년'],1, inplace=True)
        cctv_pop = pd.merge(cctv, pop, on='구별')
        cctv_pop.set_index('구별', inplace=True)

        cor1 = np.corrcoef(cctv_pop['고령자비율'], cctv_pop['소계'])
        cor2 = np.corrcoef(cctv_pop['외국인비율'], cctv_pop['소계'])

        print('고령자비율 상관계수 {} \n 외국인비율 상관계수 {}'.format(cor1, cor2))

        cctv_pop.to_csv(self.context + 'cctv_pop.csv')
        


