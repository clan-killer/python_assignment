import configparser

config_file = configparser.ConfigParser()

config_file.read('sample_conf.ini')

print (config_file)


