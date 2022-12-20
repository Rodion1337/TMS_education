INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Rodion","Kotaliov","boy","Radik1337Blr","radikmotocross@gmail.com",2022-20-12);

INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Vovchik","Danilov","boy","Bro27","Bro27@gmail.com",2022-01-12);

INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Ahmed","Ibragimov","boy","Dyx","Dyx@gmail.com",2022-20-11);

INSERT INTO users(first_name,last_name,gender,login,email,register_date)
VALUES("Egor","Yzon","idiot","Yzik","Yzik1973@gmail.com",2021-13-11);



INSERT INTO category(category_id,category_title)
VALUES('1','Drift');

INSERT INTO category(category_id,category_title)
VALUES('2','Drug');

INSERT INTO category(category_id,category_title)
VALUES('3','Cyber');

INSERT INTO category(category_id,category_title)
VALUES('4','Science');


INSERT INTO posts(title, date_created,content,post_author_id,post_category_id)
VALUES("What is Quantum Computing?", 2021-01-18,"Quantum computing is a rapidly-emerging technology that harnesses the laws of quantum mechanics to solve problems too complex for classical computers", 1, 4);

INSERT INTO posts(title, date_created,content,post_author_id,post_category_id)
VALUES("чемпионат дрифта 2022!",10-10-2022,"Чемпионом РДС становится Георгий Чивчян набрав в лично зачёте 275 баллов", 2, 1);