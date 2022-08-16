CREATE TABLE IF NOT EXISTS `location`(
    `content_location` TEXT NOT NULL,
    `page_url` TEXT NOT NULL UNIQUE,
    `media_type` TEXT NOT NULL,
    `file_name` TEXT NOT NULL UNIQUE,
    `dest` TEXT NOT NULL UNIQUE,
    `content_text` TEXT,
    PRIMARY KEY(`content_location`)
)
;
