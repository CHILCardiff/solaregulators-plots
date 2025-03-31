import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import regulator data
reg_data = pd.read_csv('regulators-tests.csv')

# make combined make/model column
reg_data["Make/model"] = reg_data['Manufacturer'] + " " +  reg_data['Model number']

# drop unnecessary column
reg_data.drop('Measured night consumption (A)',axis='columns', inplace=True)

# rename column
reg_data.rename(columns={"mA":"Measured night consumption (mA)"}, inplace=True)

# create data subset for regulators <4.5A rating
small_reg_data = reg_data[reg_data['Rated current (A)'] <4.5] 
small_reg_data_sorted = small_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
small_reg_data_sorted.drop('Rated current (A)', axis='columns', inplace=True)

print(small_reg_data_sorted)

ax = small_reg_data_sorted.plot.bar(x='Make/model', rot=0)

# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_title('Currrent consumption of regulators rated to <4.5A')
ax.set_ylabel('Current, mA')

plt.savefig('small_regulators.png')

# 5A-class regulators

# create data subset for regulators >4.5A <7 rating
medium_reg_data = reg_data[reg_data['Rated current (A)'].between(4.5, 7)] 
medium_reg_data_sorted = medium_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
medium_reg_data_sorted.drop('Rated current (A)', axis='columns', inplace=True)

print(medium_reg_data_sorted)

ax = medium_reg_data_sorted.plot.bar(x='Make/model')

# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_title('Currrent consumption of regulators rated to 4.5 - 7A')
ax.set_ylabel('Current, mA')


# apply wordwrap to labels

import textwrap
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0)

wrap_labels(ax, 10)

plt.subplots_adjust(bottom = 0.22)

plt.savefig('medium_regulators.png')

# 10A-class regulators

# create data subset for regulators >9 <11 rating
medium_reg_data = reg_data[reg_data['Rated current (A)'].between(9, 50)] 
medium_reg_data_sorted = medium_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
medium_reg_data_sorted.drop('Rated current (A)', axis='columns', inplace=True)

print(medium_reg_data_sorted)

ax = medium_reg_data_sorted.plot.bar(x='Make/model', figsize=(10,8))

# Add some text for labels, title and custom x-axis tick labels, etc.

ax.set_title('Currrent consumption of regulators rated to >9A')
ax.set_ylabel('Current, mA')

wrap_labels(ax, 10)

plt.subplots_adjust(bottom = 0.22)

plt.savefig('big_regulators.png')



