import datetime
from collections import OrderedDict, defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

ALL_DEMAND = pd.read_excel('wine3.xlsx').fillna('').to_dict('record')

age = (
    datetime.datetime.today() -
    datetime.datetime.strptime('1920-01-01', '%Y-%m-%d')
)
age = int(age.days // (365.25))

dict_demand = defaultdict(list)
for demand in ALL_DEMAND:
    dict_demand[demand['Категория']].append(demand)
dict_demand = OrderedDict(sorted(dict_demand.items(), key=lambda x: x[0]))


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
rendered_page = template.render(
    age=age,
    dict_demand=dict_demand
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
