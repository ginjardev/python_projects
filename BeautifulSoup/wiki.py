import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"

response = requests.get(url).text

doc = BeautifulSoup(response, "html.parser")

my_table = doc.find("table", class_="wikitable sortable plainrowheaders")

th_tags = my_table.find_all('th')

names = []

for elem in th_tags:
    a_links = elem.find_all("a")
    for i in a_links:
        names.append(i.string)

# print(names)


final_list = names[9:]
states = []

for str in final_list:
    if len(str) > 3:
        states.append(str)
# print(states)

divs = my_table.find_all("div")
pop = []
for i in divs:
    pop.append(i.text)
# print(pop)

final_pop = []
for i in pop:
    if len(i) > 3:
        final_pop.append(i)




import pandas as pd
df = pd.DataFrame()

df['state'] = states
df['population'] = final_pop

df.to_csv('us_state_pop.csv')
print(df)