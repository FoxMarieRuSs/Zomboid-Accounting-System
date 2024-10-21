import argparse
from src.inventory import Inventory

def main():
    parser = argparse.ArgumentParser(description='Zomboid Inventory System')
    parser.add_argument('--file', required=True, help='CSV file with inventory data')
    args = parser.parse_args()

    inv = Inventory(args.file)
    print("Inventory loaded!")

if __name__ == '__main__':
    main()
