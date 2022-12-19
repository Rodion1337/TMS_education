CREATE TABLE users ( id INTEGER NOT NULL UNIQUE, "first_name" TEXT NOT NULL, "last_name" TEXT NOT NULL, "gender" TEXT NOT NULL, 
"login" TEXT NOT NULL UNIQUE, "email" TEXT NOT NULL UNIQUE, "register_date" REAL NOT NULL, PRIMARY KEY("id") )

CREATE TABLE category ( category_id INTEGER NOT NULL UNIQUE, "category_title" TEXT UNIQUE, PRIMARY KEY("category_id" AUTOINCREMENT) )

REATE TABLE posts ( id_post INTEGER NOT NULL UNIQUE, "title" TEXT, "date_created" INTEGER, "content" TEXT, "post_author_id" INTEGER, 
"post_category_id" INTEGER, FOREIGN KEY("post_author_id") REFERENCES "users"("login"), FOREIGN KEY("post_category_id") REFERENCES "category"("category_title"), PRIMARY KEY("id" AUTOINCREMENT) )