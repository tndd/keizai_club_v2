INSERT OR IGNORE INTO page_url (
    `timestamp`,
    `page_url`,
    `page_title`,
    `page_date`,
    `category`,
    `parent_url`
)
VALUES(?, ?, ?, ?, ?, ?)
;
