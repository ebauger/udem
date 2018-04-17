create table Sources
(
  id   int auto_increment
    primary key,
  html text null,
  constraint Source_id_uindex
  unique (id)
)
  comment 'History of the HTML page'
  engine = InnoDB;

create table States
(
  id                int auto_increment
    primary key,
  state             varchar(20) not null,
  last_verification datetime    null,
  firstime          datetime    null,
  last_changes      datetime    null,
  number_versions   int         null,
  constraint States_id_uindex
  unique (id),
  constraint States_state_uindex
  unique (state)
)
  engine = InnoDB;

create table Tags
(
  id      int auto_increment
    primary key,
  name_fr varchar(20) not null,
  name_en varchar(20) null,
  constraint Tags_id_uindex
  unique (id),
  constraint Tags_name_fr_uindex
  unique (name_fr),
  constraint Tags_name_en_uindex
  unique (name_en)
)
  engine = InnoDB;

create table Websites
(
  id   int auto_increment
    primary key,
  name varchar(20) null,
  url  text        null,
  constraint Websites_id_uindex
  unique (id)
)
  engine = InnoDB;

create table Pages
(
  id          int auto_increment
    primary key,
  url         varchar(2083) not null,
  last_time   int           null,
  first_time  int           null,
  last_access int           null,
  website_id  int           null,
  state_id    int           null,
  source_id   int           null,
  constraint Pages_id_uindex
  unique (id),
  constraint Pages_Websites_id_fk
  foreign key (website_id) references Websites (id),
  constraint Pages_States_id_fk
  foreign key (state_id) references States (id),
  constraint Pages_Sources_id_fk
  foreign key (source_id) references Sources (id)
)
  engine = InnoDB;

create index Pages_Sources_id_fk
  on Pages (source_id);

create index Pages_States_id_fk
  on Pages (state_id);

create index Pages_Websites_id_fk
  on Pages (website_id);

create table Tags_Pages
(
  page_id int not null,
  tag_id  int not null,
  constraint Tags_Pages_page_id_uindex
  unique (page_id),
  constraint Tags_Pages_tag_id_uindex
  unique (tag_id),
  constraint Tags_Pages_Pages_id_fk
  foreign key (page_id) references Pages (id),
  constraint Tags_Pages_Websites_id_fk
  foreign key (page_id) references Websites (id),
  constraint Tags_Pages_Tags_id_fk
  foreign key (tag_id) references Tags (id)
)
  engine = InnoDB;

create table Tags_Websites
(
  website_id int null,
  tag_id     int null,
  constraint Tags_Websites_Websites_id_fk
  foreign key (website_id) references Websites (id),
  constraint Tags_Websites_Tags_id_fk
  foreign key (tag_id) references Tags (id)
)
  engine = InnoDB;

create index Tags_Websites_Tags_id_fk
  on Tags_Websites (tag_id);

create index Tags_Websites_Websites_id_fk
  on Tags_Websites (website_id);

