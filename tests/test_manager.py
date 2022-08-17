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
    expd_tbl_names = ['category', 'location', 'page_url']
    table_names = [n[0] for n in m.cur.execute(query_get_tables).fetchall()]
    assert expd_tbl_names == table_names
    # validate table info
    expd_tbl_info = {
        "category": [(0, 'url', 'TEXT', 1, None, 1), (1, 'name', 'TEXT', 1, None, 0), (2, 'name_jp', 'TEXT', 1, None, 0)],
        "location": [(0, 'content_location', 'TEXT', 1, None, 1), (1, 'page_url', 'TEXT', 1, None, 0), (2, 'media_type', 'TEXT', 1, None, 0), (3, 'file_name', 'TEXT', 1, None, 0), (4, 'dest', 'TEXT', 1, None, 0), (5, 'content_text', 'TEXT', 0, None, 0)],
        "page_url": [(0, 'timestamp', 'TEXT', 1, None, 1), (1, 'page_url', 'TEXT', 1, None, 2), (2, 'page_title', 'TEXT', 1, None, 0), (3, 'page_date', 'TEXT', 1, None, 0), (4, 'category', 'TEXT', 1, None, 0), (5, 'parent_url', 'TEXT', 1, None, 0)]
    }
    for name in table_names:
        query_table_info = f"PRAGMA table_info('{name}');"
        print(m.cur.execute(query_table_info).fetchall())
        assert expd_tbl_info[name] == m.cur.execute(query_table_info).fetchall()


# def test_select_category() -> None:
#     m = get_manager_for_test()
#     l = m.select_category()
#     print(l)


def main() -> None:
    pass
    test_init_db()


if __name__ == '__main__':
    main()
