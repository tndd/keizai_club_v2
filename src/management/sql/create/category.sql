CREATE TABLE IF NOT EXISTS `category` (
    `url` TEXT not null,
    `name` TEXT not null UNIQUE,
    `name_jp` TEXT not null UNIQUE,
    primary key (`url`)
)
;
