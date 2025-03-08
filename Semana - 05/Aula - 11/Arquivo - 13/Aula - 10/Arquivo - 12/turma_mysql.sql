create database if not exists turma;
use turma;
drop table if exists aluno;

create table aluno(
	id int primary key auto_increment,
    nome varchar(50) not null,
    nota1 float not null,
    nota2 float not null
);

insert into aluno values
(0, 'LP', 4, 5),
(0, 'Gustavo', 7, 8),
(0, 'Mari', 9, 9),
(0, 'Bartô', 6, 7);