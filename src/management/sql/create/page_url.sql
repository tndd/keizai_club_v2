CREATE TABLE IF NOT EXISTS page_url (
    `timestamp` INTEGER NOT NULL,
    `page_url` TEXT NOT NULL,
    `page_title` TEXT NOT NULL,
    `page_date` TEXT NOT NULL,
    `category` TEXT NOT NULL,
    `parent_url` TEXT NOT NULL,
    PRIMARY KEY(`timestamp`, `page_url`)
)
;
