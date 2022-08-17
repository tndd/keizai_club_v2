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
    query_get_tables = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY NAME;"
    expected_table_names = [('category',), ('location',), ('page_url',)]
    table_names = m.cur.execute(query_get_tables).fetchall()
    assert expected_table_names == table_names
    # print(m.cur.fetchall())
    # print(m.cur.execute("PRAGMA table_info('category')").fetchall())


# def test_select_category() -> None:
#     m = get_manager_for_test()
#     l = m.select_category()
#     print(l)


def main() -> None:
    pass
    test_init_db()


if __name__ == '__main__':
    main()
