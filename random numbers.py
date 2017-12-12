import numpy as np
import scipy
from scipy import stats
random_uni_rvs = stats.uniform.rvs(size = 10)
print random_uni_rvs
random_beta_rvs = stats.beta.rvs(size = 10, a=4, b=2)
print random_beta_rvs
