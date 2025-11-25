from settings import config
from api import create_app
from pprint import pprint

app = create_app()

def main():
    pprint(config.model_dump())


if __name__ == "__main__":
    main()
