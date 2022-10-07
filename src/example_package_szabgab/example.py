import sys
def add_one(number):
    return number + 1

def run():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} NUMBER")
    print(add_one(int(sys.argv[1])))

if __name__ == '__main__':
    run()

