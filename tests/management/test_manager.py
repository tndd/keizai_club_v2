from src.management.manager import Manager


def get_manager_for_test() -> Manager:
    return Manager(database='__test.db')


def test_init_db() -> None:
    m = get_manager_for_test()
    m.init_db()

def test_select_category() -> None:
    m = get_manager_for_test()
    l = m.select_category()
    print(l)


def main() -> None:
    test_select_category()


if __name__ == '__main__':
    main()
