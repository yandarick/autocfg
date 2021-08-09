import pandas as pd
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

hostname = 'sw1'
df = pd.read_excel('xls/switch.xlsx', sheet_name=hostname, header=0)
df = df[df['INTERFACE'] != "CUSTOM_CONFIG"]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

template = env.get_template('interface.j2')
precfg = template.render(df=df)
print(precfg)

with open('precfg/' + hostname + '.txt', 'w') as f:
    f.write(precfg)