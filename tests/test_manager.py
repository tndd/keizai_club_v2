from src.management.manager import Manager


def get_manager_for_test() -> Manager:
    return Manager(database='__test.db')


def test_init_db() -> None:
    # prepare
    m = get_manager_for_test()
    m._drop_tables()
    # test method
    m.init_db()
    # validate table name
    m.cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY NAME;")
    print(m.cur.fetchall())

def test_select_category() -> None:
    m = get_manager_for_test()
    l = m.select_category()
    print(l)


def main() -> None:
    test_init_db()


if __name__ == '__main__':
    main()
