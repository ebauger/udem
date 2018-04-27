USE udem_part2;
create table html_version
(
  id          int auto_increment
    primary key,
  page_url_id int,
  html        text null
);

create table page_status
(
  id               int auto_increment
    primary key,
  description_name varchar(20)
);

create table tag
(
  id      int auto_increment
    primary key,
  name_fr varchar(20) not null,
  name_en varchar(20) not null

);

create table tag_website_page_url
(
  id         int auto_increment primary key,
  tag_id     int not null,
  page_id    int null,
  website_id int null
);

create table website
(
  id       int auto_increment
    primary key,
  name     varchar(20)   null,
  root_url varchar(2083) null
);

create table page_url
(
  id         int auto_increment
    primary key,
  website_id int,
  url_path   varchar(2083) not null,
  last_check int           null,
  first_time int           null,
  last_time  int           null
);

