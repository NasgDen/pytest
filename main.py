from src.utils import calculate_tax, calculate_taxes


def main():
    print(calculate_taxes([2, 4, 6], 10))
    print(calculate_tax(50.2222, 5, 0, 3))


if __name__ == "__main__":
    main()
