#%%
import pandas as pd
import numpy as np

# Load data files into dataframes with separator "|" or ","
bnc = pd.read_csv("../data/nhis_edu/nsc2_edu_bnc.txt", sep="|")
bnd = pd.read_csv("../data/nhis_edu/nsc2_edu_bnd.txt", sep="|")
g1e = pd.read_csv("../data/nhis_edu/nsc2_edu_g1e.txt", sep="|", encoding='cp949')
m20 = pd.read_csv("../data/nhis_edu/nsc2_edu_m20.txt", sep=",")

# Correct birth year in bnd and convert to numeric
bnd['BTH_YYYY'] = bnd['BTH_YYYY'].replace('1921LE', '1921').astype(int)
# Add randomness to birth year
np.random.seed(1234)
bnd['BTH_YYYY'] = bnd['BTH_YYYY'] + np.random.choice(range(10), size=len(bnd))

