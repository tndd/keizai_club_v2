from src.management.manager import Manager


def get_manager_for_test() -> Manager:
    return Manager(database='__test.db')


def test_init_db() -> None:
    # initialize database
    m = get_manager_for_test()
    m.cur.execute('drop table if exists category;')
    m.cur.execute('drop table if exists location;')
    m.cur.execute('drop table if exists page_url;')
    m.conn.commit()
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


def test_select_category() -> None:
    m = get_manager_for_test()
    expd_rows_category = [
        ('https://keizaiclub.com/category/%e8%bf%91%e6%9c%aa%e6%9d%a5%e4%ba%88%e6%b8%ac', 'near_future', '近未来予測'),
        ('https://keizaiclub.com/category/zatsudan', 'wrestling_chat', 'プロレス雑談'),
        ('https://keizaiclub.com/category/%e3%83%a9%e3%82%a4%e3%83%96qa', 'live_qa', 'ライブQ&A'),
        ('https://keizaiclub.com/category/%e3%83%9d%e3%83%83%e3%83%89%e3%82%ad%e3%83%a3%e3%82%b9%e3%83%86%e3%82%a3%e3%83%b3%e3%82%b0', 'podcast', '世界経済Q&A')
    ]
    assert expd_rows_category == m.select_category()


def test_insert_select_location() -> None:
    m = get_manager_for_test()
    insert_rows = [
        ('test_row_a1', 'a2', 'a3', 'a4', 'a5', 'a6'),
        ('test_row_a1', 'a2_', 'a3_', 'a4_', 'a5_', 'a6_'),     # violation primary key
        ('test_row_a1_', 'a2', 'a3_', 'a4', 'a5', 'a6_'),       # violation unique
        ('test_row_b1', 'b2', 'b3', 'b4', 'b5', 'b6'),
        ('test_row_c1', 'c2', 'c3', 'c4', 'c5', 'c6')
    ]
    m.insert_location(insert_rows)
    expd_rows = [
        ('test_row_a1', 'a2', 'a3', 'a4', 'a5', 'a6'),
        ('test_row_b1', 'b2', 'b3', 'b4', 'b5', 'b6'),
        ('test_row_c1', 'c2', 'c3', 'c4', 'c5', 'c6')
    ]
    assert expd_rows == m.select_location()


def main() -> None:
    test_insert_select_location()


if __name__ == '__main__':
    main()
