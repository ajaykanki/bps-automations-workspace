from settings import config

def main():
    print(config.model_dump())
    print("Hello from worker!")


if __name__ == "__main__":
    main()
