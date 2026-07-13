from database.connection import test_connection
from database.schema import create_tables


def main():
    print("=== Catalyst Scanner ===")
    print("Application started")

    test_connection()

    create_tables()


if __name__ == "__main__":
    main()