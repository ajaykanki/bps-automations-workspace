from settings import config
from pprint import pprint

def main():
    pprint(config.model_dump())


if __name__ == "__main__":
    main()
