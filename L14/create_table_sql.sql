CREATE TABLE users ( user_id INTEGER NOT NULL UNIQUE, 
first_name TEXT NOT NULL, 
last_name TEXT NOT NULL, 
gender TEXT NOT NULL, 
login TEXT NOT NULL UNIQUE, 
email TEXT NOT NULL UNIQUE, 
register_date date NOT NULL, 
PRIMARY KEY(user_id AUTOINCREMENT) );

CREATE TABLE category ( category_id INTEGER NOT NULL UNIQUE, 
category_title TEXT UNIQUE, 
PRIMARY KEY(category_id AUTOINCREMENT) );

CREATE TABLE posts ( post_id INTEGER NOT NULL UNIQUE, 
title TEXT NOT NULL, 
date_created DATE NOT NULL, 
content varchar(140), 
post_author_id INTEGER NOT NULL, 
post_category_id INTEGER NOT NULL, 
FOREIGN KEY(post_author_id) REFERENCES users(user_id), 
FOREIGN KEY(post_category_id) REFERENCES category(category_id), 
PRIMARY KEY(post_id AUTOINCREMENT) );