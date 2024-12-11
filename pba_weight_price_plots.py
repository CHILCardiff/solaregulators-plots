import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import battery weight and cost data
battery_data = pd.read_csv('PBA_cost_weight_model.csv')
battery_data.sort_values(by='Capacity (Ah, 20hr rate)')

# let's do weight first

plt.figure(1)

# scatter points
plt.scatter(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Weight (kg)'])

# calculate linear trendline
trendfit = np.polyfit(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Weight (kg)'], 1)
trendline = np.poly1d(trendfit)

# plot trendline
plt.plot(battery_data['Capacity (Ah, 20hr rate)'], trendline(battery_data['Capacity (Ah, 20hr rate)']))

# add titles
plt.xlabel('Battery capacity (Ah, 20hr rate)')
plt.ylabel('Battery weight, kg')
plt.title('Lead-acid battery weight vs capacity')

eqn_string = "%s" % trendline 

# add equation
plt.text(10, 35, ("y = %s" % eqn_string.strip()))

plt.savefig('battery_weight.png')

# now price

plt.figure(2)
# scatter points
plt.scatter(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Price euro'])

# calculate linear trendline
pricetrendfit = np.polyfit(battery_data['Capacity (Ah, 20hr rate)'], battery_data['Price euro'], 1)
pricetrendline = np.poly1d(pricetrendfit)


# plot trendline
plt.plot(battery_data['Capacity (Ah, 20hr rate)'], pricetrendline(battery_data['Capacity (Ah, 20hr rate)']))

# add titles
plt.xlabel('Battery capacity (Ah, 20hr rate)')
plt.ylabel('Battery price, euros')
plt.title('Lead-acid battery price vs capacity')

eqn_string = "%s" % pricetrendline 


# add equation
plt.text(10, 300, ("y = %s" % eqn_string.strip()))

plt.savefig('battery_price.png')