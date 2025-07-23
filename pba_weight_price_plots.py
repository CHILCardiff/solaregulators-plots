import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import battery weight and cost data
battery_data = pd.read_csv('PBA_cost_weight_model.csv')
battery_data.sort_values(by='Capacity (Ah, 20hr rate)')

# let's do weight first

#plt.figure(1)
fig, (ax1,ax2) = plt.subplots(2, sharex=True)

# scatter points
ax1.scatter(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Weight (kg)'])

# calculate linear trendline
trendfit = np.polyfit(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Weight (kg)'], 1)
trendline = np.poly1d(trendfit)

# plot trendline
ax1.plot(battery_data['Capacity (Ah, 20hr rate)'], trendline(battery_data['Capacity (Ah, 20hr rate)']))

# add titles

ax1.set_ylabel('Battery mass, kg')
#plt.title('Lead-acid battery mass vs capacity')

eqn_string = "%s" % trendline 

# add equation
ax1.text(10, 35, ("y = %s" % eqn_string.strip()))

#fig.savefig('battery_weight.png')

# now price

#plt.figure(2)
# scatter points
ax2.scatter(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Price euro'])

# calculate linear trendline
pricetrendfit = np.polyfit(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Price euro'], 1)
pricetrendline = np.poly1d(pricetrendfit)


# plot trendline
ax2.plot(battery_data['Capacity (Ah, 20hr rate)'], pricetrendline(battery_data['Capacity (Ah, 20hr rate)']))

# add titles
#plt.xlabel('Battery capacity (Ah, 20hr rate)')
ax2.set_xlabel('Battery capacity (Ah, 20hr rate)')
ax2.set_ylabel('Battery price, euros')
#plt.title('Lead-acid battery price vs capacity')

eqn_string = "%s" % pricetrendline 


# add equation
ax2.text(10, 300, ("y = %s" % eqn_string.strip()))

plt.savefig('battery_mass_price.png')