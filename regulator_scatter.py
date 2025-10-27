import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# import regulator data
reg_data = pd.read_csv('regulators-tests.csv')

# make combined make/model column
reg_data["Regulator under test"] = reg_data['Manufacturer'] + " " +  reg_data['Model number']

# drop unnecessary columns
#reg_data.drop('Measured night consumption (A)',axis='columns', inplace=True)
#reg_data.drop('Approx price (EUR)',axis='columns', inplace=True)

# rename column
reg_data.rename(columns={"mA":"Measured night consumption (mA)"}, inplace=True)

# create data subset for regulators with measured consumption under 0.5mA
#small_reg_data = reg_data[reg_data['Measured night consumption (mA)'] <0.5] 
#small_reg_data_sorted = small_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
#small_reg_data.drop('Rated current (A)', axis='columns', inplace=True)

#print(small_reg_data)

#gs_kw = dict(height_ratios=[2, 1])
#fig, (ax1,ax2) = plt.subplots(nrows=2, figsize=(7,7), layout="constrained", gridspec_kw=gs_kw) # 7 x 10 inches

#small_reg_data.plot.barh(x='Regulator under test', rot=0, ax=ax2, legend=False, fontsize=10, label='_nolegend')
#ax2.invert_yaxis()




# Add some text for labels, title and custom x-axis tick labels, etc.

# apply wordwrap to labels

import textwrap
def wrap_labels(ax, width, break_long_words=False):
    labels = []
    for label in ax.get_xticklabels():
        text = label.get_text()
        labels.append(textwrap.fill(text, width=width,
                      break_long_words=break_long_words))
    ax.set_xticklabels(labels, rotation=0, fontsize=10)

#wrap_labels(ax2, 7)


# ax.set_title('Currrent consumption of regulators rated to <4.5A')
#ax2.set_xlabel('Current, mA')

# plt.savefig('small_regulators.png')

# 5A-class regulators

# create data subset for regulators >4.5A <7 rating
#medium_reg_data = reg_data[reg_data['Rated current (A)'].between(4.5, 7)] 
#medium_reg_data_sorted = medium_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
#medium_reg_data_sorted.drop('Rated current (A)', axis='columns', inplace=True)

#print(medium_reg_data_sorted)

#medium_reg_data_sorted.plot.bar(x='Make/model', ax=ax2, legend=False)

# Add some text for labels, title and custom x-axis tick labels, etc.

# ax.set_title('Currrent consumption of regulators rated to 4.5 - 7A')
#ax2.set_ylabel('Current, mA')




#wrap_labels(ax2, 7)

#plt.subplots_adjust(bottom = 0.22)

#fig.savefig('small_medium_regulators.png')

# 10A-class regulators

# create data subset for regulators >9 <11 rating
#medium_reg_data = reg_data[reg_data['Rated current (A)'].between(9, 50)] 
#medium_reg_data_sorted = medium_reg_data.sort_values(by = 'Measured night consumption (mA)')

# drop unnnecessary column
#medium_reg_data_sorted.drop('Rated current (A)', axis='columns', inplace=True)

#print(medium_reg_data_sorted)


reg_data.sort_values(by = 'Measured night consumption (mA)')
#reg_data.drop('Rated current (A)', axis='columns', inplace=True)

#fig2, ax3 = plt.subplots(layout='constrained', figsize=(7,5))

fig, ax1 = plt.subplots()


sns.scatterplot(data=reg_data, ax=ax1, x='Datasheet night consumption (mA)', y='Measured night consumption (mA)', hue='Manufacturer')
# Shrink current axis by 20%
box = ax1.get_position()
ax1.set_position([box.x0, box.y0, box.width * 0.75, box.height])
sns.move_legend(ax1, "upper left", bbox_to_anchor=(1, 1))

# reference line
ref_line = range(0,26)
ax1.plot(ref_line, ref_line)

# text

ax1.text(10,15, "Perform worse than advertised", rotation=30)
ax1.text(10,5, "Perform better than advertised", rotation=30)


#add arrow annotations
#for index, row in reg_data.iterrows():
#    ax1.annotate(row['Regulator under test'], (row['Datasheet night consumption (mA)'], row['Measured night consumption (mA)']), arrowprops=dict(arrowstyle="->", relpos=[0,0]), fontsize='x-small', xytext=(40,-40), textcoords='offset points')


#adjust_text(ax1)
#ax1.invert_yaxis()

#handles, labels = mainplot.get_legend_handles_labels()

#fig.legend(loc='outside lower right', handles=handles, labels=labels)

# Add some text for labels, title and custom x-axis tick labels, etc.

# ax.set_title('Currrent consumption of regulators rated to >9A')
#ax1.set_xlabel('Current, mA')

#wrap_labels(ax1, 7)

#fig2.subplots_adjust(bottom = 0.22)

#fig.align_labels()

# add panel labels to both plots
#fig.text(0.95,0.95, "a)")
#fig.text(0.95,0.17, "b)")

fig.savefig('measured_current_scatter.png', dpi=300)



