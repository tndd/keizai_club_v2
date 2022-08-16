import sqlite3
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Manager:
    pwd: str = Path(__file__).resolve().parent
    database: str = 'main.db'

    def __post_init__(self) -> None:
        self.conn = sqlite3.connect(f'{self.pwd}/{self.database}')
        self.cur = self.conn.cursor()

    def create_category(self) -> None:
        with open(f'{self.pwd}/sql/create_category.sql') as f:
            query = f.read()
        self.cur.execute(query)
        self.conn.commit()

    def create_page_url(self) -> None:
        with open(f'{self.pwd}/sql/create_page_url.sql') as f:
            query = f.read()
        self.cur.execute(query)
        self.conn.commit()

    def create_location(self) -> None:
        with open(f'{self.pwd}/sql/create_location.sql') as f:
            query = f.read()
        self.cur.execute(query)
        self.conn.commit()

    def insert_category(self) -> None:
        with open(f'{self.pwd}/sql/insert_category.sql') as f:
            query = f.read()
        self.cur.execute(query)
        self.conn.commit()



def main() -> None:
    m = Manager()
    m.create_page_url()
    # m.insert_category()
    # print(m.get_category_url_pages('aaa'))


if __name__ == '__main__':
    main()
