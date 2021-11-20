# Game Configuration
import json

def read_config():
  with open('config/config.json', 'r') as f:
    return json.load(f)


# Unpack our configurations
config = read_config()