import configparser
import os

config = configparser.ConfigParser()
config_file = "config.ini"

if not os.path.exists(config_file):
    raise FileNotFoundError(f"The configuration file {config_file} does not exist")

# Lê o arquivo de configuração local
config.read(config_file)

# Exibindo o tipo do objeto
print(type(config))

# Acessando a versão de forma correta
print(config["general"]["app_name"])

for secao in config.sections():
    print(secao)
    for chave, valor in config.items(secao):
        print(f"{chave} - {valor}")
