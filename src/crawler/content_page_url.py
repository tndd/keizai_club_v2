from datetime import datetime
from typing import List

from src.crawler.general import get_driver
from src.management.manager import Manager


def generate_url_pages(url: str) -> List[str]:
    urls = [url]
    for i in range(2, 1000):
        urls.append(f'{url}/page/{i}')
    return urls


def main() -> None:
    ts = datetime.now().strftime("%Y%m%d%H%M%S")
    manager = Manager()
    # driver = get_driver()
    content_category = manager.load_content_category()
    page_url = {}
    for url_base, v in content_category.items():
        page_url[v['name']] = {}
        for url in generate_url_pages(url_base):
            # driver.get(url)
            urls = [f'test/data/{i}' for i in range(10)]
            page_url[v['name']][url] = urls
    manager.append_content_page_url(page_url, ts)


if __name__ == '__main__':
    main()
