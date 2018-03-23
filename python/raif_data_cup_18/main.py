#! /usr/bin/python

import pandas as p
import matplotlib.pyplot as plt

plt.style.use('ggplot')
data = p.read_csv(filepath_or_buffer='train_set.csv')

data[:2][:5].plot()
