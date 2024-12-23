import pandas as pd
import matplotlib.pyplot as plt
from set_of_airlines import SetOfAirlines
import numpy as np

print('This code was finished on Dec 1st 2024')
print('This code was written by Emiliano Lane, Samuel Wilson, and Abhigna Isukamatla')
print('The purpose of this code is to disect and produce detailed info from an excel sheet in order to answer the question: "Does the airline you fly effect the chance your flight is canceled or significantly delayed?"')

dataframe = pd.read_csv("On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_2024_1.csv")

set_of_airlines = SetOfAirlines(dict(tuple(dataframe.groupby('Reporting_Airline'))))
set_of_airlines.fill_na("LateAircraftDelay")
set_of_airlines.fill_na("WeatherDelay")
set_of_airlines.fill_na("CarrierDelay")
set_of_airlines.fill_na("SecurityDelay")

delay_minutes = set_of_airlines.avg_delay_minutes_all()
late_aircraft_delay = set_of_airlines.avg_column_all("LateAircraftDelay")
weather_delay = set_of_airlines.avg_column_all("WeatherDelay")
carrier_delay = set_of_airlines.avg_column_all("CarrierDelay")
security_delay = set_of_airlines.avg_column_all("SecurityDelay")

total_bars = 0.8
number_of_bars = 5
bar_width = total_bars/number_of_bars
x_values = np.arange(len(delay_minutes.keys()))
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx(); ax3 = ax1.twinx(); ax4 = ax1.twinx(); ax5 = ax1.twinx()

ax1.bar(x_values - bar_width*2, delay_minutes.values(), bar_width, label="Average delay")
ax1.set_xlabel("Airline"); ax1.set_ylabel("Average Arrival Delay (minutes)")

ax2.bar(x_values - bar_width, late_aircraft_delay.values(), bar_width, color="orange", label="Average delay due to late aircraft")
ax3.bar(x_values, weather_delay.values(), bar_width, color="lightgreen", label="Average delay due to weather")
ax4.bar(x_values + bar_width, carrier_delay.values(), bar_width, color="purple", label="Average carrier delay")
ax5.bar(x_values + bar_width*2, security_delay.values(), bar_width, color="gray", label="Average delay due to security")

ax2.set_ylim(ax1.get_ylim()); ax3.set_ylim(ax1.get_ylim()); ax4.set_ylim(ax1.get_ylim()); ax5.set_ylim(ax1.get_ylim())
ax1.set_xticks(x_values)
ax1.set_xticklabels(delay_minutes.keys(), rotation=90)
plt.tight_layout()
plt.title("Average Arrival Delay in Minutes for Certain Airlines")
plt.subplots_adjust(left=0.05, top=0.95, bottom=0.21)


def create_legend():
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    h3, l3 = ax3.get_legend_handles_labels()
    h4, l4 = ax4.get_legend_handles_labels()
    h5, l5 = ax5.get_legend_handles_labels()

    handles = h1 + h2 + h3 + h4 + h5
    labels = l1 + l2 + l3 + l4 + l5

    ax1.legend(handles, labels, loc="upper right")

create_legend()
plt.show()

class SetOfAirlines:
    airline_names = {
        "AA": "American Airlines",
        "UA": "United Airlines",
        "9E": "Endeavor Air",
        "AS": "Alaska Airlines",
        "B6": "JetBlue Airways",
        "DL": "Delta Air Lines",
        "F9": "Frontier Airlines",
        "G4": "Allegiant Air",
        "HA": "Hawaiian Airlines",
        "MQ": "Envoy Air",
        "NK": "Spirit Airlines",
        "OH": "Jetstream",
        "OO": "Skywest Airlines",
        "WN": "Southwest Airlines",
        "YX": "Republic Airlines",
    }

    def __init__(self, dictionary):
        self.input_dict = dictionary
        self.airlines = {}
        for key in self.input_dict:
            airline_name = key

            # Apply airline name if available
            if SetOfAirlines.airline_names.__contains__(key):
                airline_name = SetOfAirlines.airline_names[key]

            self.airlines[airline_name] = (Airline(self.input_dict[key]))

    def __str__(self):
        return f"{self.airlines}"

    def fill_na(self, column_name):
        for key in self.airlines.keys():
            self.airlines[key].fill_na(column_name)

    def avg_delay_minutes_all(self):
        delays_dict = {}
        for key in self.airlines.keys():
            delays_dict[key] = float(self.airlines[key].avg_delay_minutes())

        return delays_dict

    def avg_column_all(self, column_name):
        column_averages_dict = {}
        for key in self.airlines.keys():
            column_averages_dict[key] = float(self.airlines[key].avg_column(column_name))

        return column_averages_dict
    
class Airline:
    def __init__(self, df):
        self.df = df

    def __str__(self):
        return f"{self.df}"

    def fill_na(self, column_name):
        self.df.fillna({column_name: 0}, inplace=True)

    def avg_delay_minutes(self):
        return self.df["ArrDelayMinutes"].mean()

    def avg_column(self, column_name):
        return self.df[column_name].mean()




#Late Aircraft
total_bars = 0.8
number_of_bars = 1
bar_width = total_bars/number_of_bars
x_values = np.arange(len(delay_minutes.keys()))
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx(); ax3 = ax1.twinx(); ax4 = ax1.twinx(); ax5 = ax1.twinx()

ax1.bar(x_values - bar_width*2, delay_minutes.values(), bar_width, label="Average delay")
ax1.set_xlabel("Airline"); ax1.set_ylabel("Average Arrival Delay (minutes)")

ax2.bar(x_values - bar_width, late_aircraft_delay.values(), bar_width, color="orange", label="Average delay due to late aircraft")
ax2.set_ylim(ax1.get_ylim()); ax3.set_ylim(ax1.get_ylim()); ax4.set_ylim(ax1.get_ylim()); ax5.set_ylim(ax1.get_ylim())
ax1.set_xticks(x_values)
ax1.set_xticklabels(delay_minutes.keys(), rotation=90)
plt.tight_layout()
plt.title("Average Delay Due to Late Aircraft in Minutes for Certain Airlines")
plt.subplots_adjust(left=0.05, top=0.95, bottom=0.21)


def create_legend():
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    

    handles = h1 + h2 
    labels = l1 + l2 

    ax1.legend(handles, labels, loc="upper right")

create_legend()
plt.show()

#Weather
total_bars = 0.8
number_of_bars = 1
bar_width = total_bars/number_of_bars
x_values = np.arange(len(delay_minutes.keys()))
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx(); ax3 = ax1.twinx(); ax4 = ax1.twinx(); ax5 = ax1.twinx()

ax1.bar(x_values - bar_width*2, delay_minutes.values(), bar_width, label="Average delay")
ax1.set_xlabel("Airline"); ax1.set_ylabel("Average Arrival Delay (minutes)")

ax2.bar(x_values, weather_delay.values(), bar_width, color="lightgreen", label="Average delay due to weather")
ax2.set_ylim(ax1.get_ylim()); ax3.set_ylim(ax1.get_ylim()); ax4.set_ylim(ax1.get_ylim()); ax5.set_ylim(ax1.get_ylim())
ax1.set_xticks(x_values)
ax1.set_xticklabels(delay_minutes.keys(), rotation=90)
plt.tight_layout()
plt.title("Average Delay Due to Weather in Minutes for Certain Airlines")
plt.subplots_adjust(left=0.05, top=0.95, bottom=0.21)


def create_legend():
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    

    handles = h1 + h2 
    labels = l1 + l2 

    ax1.legend(handles, labels, loc="upper right")

create_legend()
plt.show()

#Security
total_bars = 0.8
number_of_bars = 1
bar_width = total_bars/number_of_bars
x_values = np.arange(len(delay_minutes.keys()))
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx(); ax3 = ax1.twinx(); ax4 = ax1.twinx(); ax5 = ax1.twinx()

ax1.bar(x_values - bar_width*2, delay_minutes.values(), bar_width, label="Average delay")
ax1.set_xlabel("Airline"); ax1.set_ylabel("Average Arrival Delay (minutes)")

ax2.bar(x_values + bar_width*2, security_delay.values(), bar_width, color="gray", label="Average delay due to security")
ax2.set_ylim(ax1.get_ylim()); ax3.set_ylim(ax1.get_ylim()); ax4.set_ylim(ax1.get_ylim()); ax5.set_ylim(ax1.get_ylim())
ax1.set_xticks(x_values)
ax1.set_xticklabels(delay_minutes.keys(), rotation=90)
plt.tight_layout()
plt.title("Average Delay Due to Security in Minutes for Certain Airlines")
plt.subplots_adjust(left=0.05, top=0.95, bottom=0.21)


def create_legend():
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    

    handles = h1 + h2 
    labels = l1 + l2 

    ax1.legend(handles, labels, loc="upper right")

create_legend()
plt.show()
