from src.management.manager import Manager


def get_manager_for_test() -> Manager:
    return Manager(database='__test.db')


def test_init_db() -> None:
    m = get_manager_for_test()
    m.init_db()


def main() -> None:
    test_init_db()


if __name__ == '__main__':
    main()
