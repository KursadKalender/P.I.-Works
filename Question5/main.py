import pandas as pd
import math
import statistics

data = pd.read_csv('country_vaccination_stats.csv')

#print(data.head())

country_min_list = {}
country_data_dict = {}
country_median = {}

for index, country in enumerate(data['country']):
    if not (country in country_data_dict):
        country_data_dict[country] = []
    if not (country in country_median):
        country_median[country] = 0
    if not (country in country_min_list):
        country_min_list[country] = float('inf')
    if not (data['daily_vaccinations'][index] is None) and data['daily_vaccinations'][index] < country_min_list.get(country):
        country_min_list[country] = data['daily_vaccinations'][index]


for index, vaccination in enumerate(data['daily_vaccinations']):
    if math.isnan(data['daily_vaccinations'][index]):
        if country_min_list.get(data['country'][index]) == float('inf'):
            country_min_list[data['country'][index]] = 0
        data['daily_vaccinations'][index] = country_min_list.get(data['country'][index])
    country_data_dict.get(data['country'][index]).append(data['daily_vaccinations'][index])


for country in country_median:
    country_median[country] = (statistics.median(country_data_dict[country]))
values = (sorted(country_median.items(), key=lambda x:x[1], reverse=True))[:3]
print(values)
