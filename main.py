import argparse
import datetime
from collections import OrderedDict, defaultdict
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

YEAR_OF_CREATION_WINERY = 1920


def main():
    age = (
        datetime.datetime.today().year - YEAR_OF_CREATION_WINERY
    )
    parser = argparse.ArgumentParser(
        description='Запускает сайт по адресу http://127.0.0.1:8000'
    )
    parser.add_argument('-p', '--path',
                        help='Путь к файлу с напитками, формат .xlsx',
                        type=str,
                        default='table_wine.xlsx')
    args = parser.parse_args()
    drinks = pd.read_excel(args.path).fillna('').to_dict('records')
    drinks_for_template = defaultdict(list)
    for drink in drinks:
        drinks_for_template[drink['Категория']].append(drink)
    drinks_for_template = OrderedDict(sorted(drinks_for_template.items(),
                                      key=lambda x: x[0]))

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
        age=age,
        drinks_for_template=drinks_for_template
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ in '__main__':
    main()
