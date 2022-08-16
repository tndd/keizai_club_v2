import sqlite3
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List


class QueryGroup(Enum):
    CREATE = 'create'
    INSERT = 'insert'
    SELECT = 'select'

@dataclass
class Manager:
    pwd: str = Path(__file__).resolve().parent
    database: str = 'main.db'

    def __post_init__(self) -> None:
        self.conn = sqlite3.connect(f'{self.pwd}/{self.database}')
        self.cur = self.conn.cursor()

    def load_query(self, group: QueryGroup, name: str) -> str:
        with open(f'{self.pwd}/sql/{group.value}/{name}.sql') as f:
            query = f.read()
        return query

    def execute_query(self, query: str) -> None:
        self.cur.execute(query)
        self.conn.commit()

    def execute_queries(self, queries: List[str]) -> None:
        for q in queries:
            self.cur.execute(q)
        self.conn.commit()

    def create_category(self) -> None:
        query = self.load_query(QueryGroup.CREATE, 'category')
        self.execute_query(query)

    def create_page_url(self) -> None:
        query = self.load_query(QueryGroup.CREATE, 'page_url')
        self.execute_query(query)

    def create_location(self) -> None:
        query = self.load_query(QueryGroup.CREATE, 'location')
        self.execute_query(query)

    def create_tables(self) -> None:
        self.create_category()
        self.create_page_url()
        self.create_location()

    def insert_category(self) -> None:
        query = self.load_query(QueryGroup.INSERT, 'category')
        self.execute_query(query)

    def init_db(self) -> None:
        self.create_tables()
        self.insert_category()



def main() -> None:
    m = Manager()
    m.init_db()
    # m.insert_category()
    # print(m.get_category_url_pages('aaa'))


if __name__ == '__main__':
    main()
