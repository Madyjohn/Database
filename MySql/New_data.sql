create database python_db1;
use python_db1;
create table user(
ID int auto_increment primary key,
NAME varchar(50),
AGE int,
CITY varchar(50)
);

select * from user;
insert into user(NAME,AGE,CITY)values('johnson',23,'chennai'),('kalai',22,'chennai'),('mukesh',22,'chennai');
show tables;
desc user;
select* from user;
