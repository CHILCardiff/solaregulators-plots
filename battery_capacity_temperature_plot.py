import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import battery weight and cost data
battery_data = pd.read_csv('rolls_batt_temp_capacity.csv')
battery_data['Usable capacity percentage'] = battery_data['Usable capacity percentage'].str.rstrip('%').astype('float')
battery_data.sort_values(by='Temperature degC', ascending=False)

ps_battery_data = pd.read_csv('powersonic_temp_capacity.csv')
ps_battery_data.sort_values(by='Temperature')



fig, ax1 = plt.subplots()

# plot Rolls battery data
ax1.plot(battery_data['Temperature degC'], battery_data['Usable capacity percentage'], 'x', label='Rolls')

# plot Power-Sonic battery data
ax1.plot(ps_battery_data['Temperature'],ps_battery_data['Capacity based on 25C as nominal'], '+', label='Power-Sonic')

ax1.set_xlim(30, -35)
ax1.set_ylim(0, 105)
ax1.grid(visible=True, which='major', axis='y')
ax1.legend()


ax1.set_xlabel('Temperature, °C')
ax1.set_ylabel('Usable battery capacity (percentage of capacity at 25 °C)')


plt.savefig('rolls_battery_temp_capacity.png')