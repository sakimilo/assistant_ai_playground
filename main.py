import yaml
from persona import compose_poem, calculate_math

with open("config/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

if __name__ == "__main__":

    print(config)