#%% Data collection

import pandas as pd
data = pd.read_csv('data/ArmadilloData.csv')

#%% Model definition

from bayreb.models import model_2R2C
m = model_2R2C()

p = m.get_parameters()

#%% Prior specification
prior = 0

#%% Learning
from bayreb.learning import batch_mcmc
posterior = batch_mcmc.learn(model = m, prior = prior, data = data)

#%% Testing posterior
import bayreb.validation as bv
foo = bv.acf(model = m, theta = 0, data = data)