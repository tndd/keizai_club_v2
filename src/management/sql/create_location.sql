CREATE TABLE IF NOT EXISTS `location`(
    `content_location` TEXT NOT NULL,
    `page_url` TEXT NOT NULL,
    `media_type` TEXT NOT NULL,
    `file_name` TEXT NOT NULL,
    `dest` TEXT NOT NULL,
    `content_text` TEXT
    PRIMARY KEY(`content_location`)
)
;
