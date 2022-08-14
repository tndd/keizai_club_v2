from dataclasses import dataclass
from pathlib import Path
from typing import List

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
            d = yaml.dump(data, f)

    def store_content_page_url(self, data: dict) -> None:
        with open(f'{self.pwd}/{self.file_page_url}', 'w') as f:
            d = yaml.dump(data, f)
        return d

    def get_categories_url(self) -> List[str]:
        data_category = self.load_content_category()
        return [url for url in data_category.keys()]


def main() -> None:
    m = Manager()
    print(m.get_categories_url())


if __name__ == '__main__':
    main()
