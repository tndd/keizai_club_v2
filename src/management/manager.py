from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Manager:
    pwd: str = Path(__file__).resolve().parent
    file_category: str = 'content_category.yml'
    file_location: str = 'content_location.yml'
    file_page_url: str = 'content_page_url.yml'

    def load_content_category(self) -> dict:
        with open(f'{self.pwd}/{self.file_category}', 'r') as f:
            d = yaml.safe_load(f)
        return d

    def load_content_location(self) -> dict:
        with open(f'{self.pwd}/{self.file_location}', 'r') as f:
            d = yaml.safe_load(f)
        return d

    def load_content_page_url(self) -> dict:
        with open(f'{self.pwd}/{self.file_page_url}', 'r') as f:
            d = yaml.safe_load(f)
        return d

    def store_content_location(self, data: dict) -> None:
        with open(f'{self.pwd}/{self.file_location}', 'w') as f:
            yaml.dump(data, f)

    def store_content_page_url(self, data: dict) -> None:
        with open(f'{self.pwd}/{self.file_page_url}', 'w') as f:
            yaml.dump(data, f)

    def append_content_page_url(self, data: dict, timestamp: str) -> None:
        d = self.load_content_page_url()
        d[timestamp] = data
        self.store_content_page_url(d)


def main() -> None:
    m = Manager()
    print(m.get_category_url_pages('aaa'))


if __name__ == '__main__':
    main()
