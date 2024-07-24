import configparser
import linecache



config = configparser.ConfigParser()
config.read("config.ini")
print(config.get('Default','config_path'))
print(config.get('Default','config_time'))

#input = str(input('Value: '))

#config.write('Default','config_time', '11')

print(config["Default"]["config_time"])