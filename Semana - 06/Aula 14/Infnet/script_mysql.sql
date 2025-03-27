DROP DATABASE IF EXISTS infnet;

CREATE DATABASE infnet;

USE infnet;

CREATE TABLE aluno (
    id_aluno INT PRIMARY KEY auto_increment,
    nome_aluno VARCHAR(50) NOT NULL
);

CREATE TABLE endereco (
    id_endereco INT PRIMARY KEY auto_increment,
    rua VARCHAR(50) NOT NULL,
    id_aluno INT NOT NULL UNIQUE,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
);

CREATE TABLE email (
    id_email INT PRIMARY KEY auto_increment,
    mail VARCHAR(50) NOT NULL,
    id_aluno INT NOT NULL,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno)
);

CREATE TABLE disciplina (
    id_disciplina INT NOT NULL AUTO_INCREMENT,
    nome_disciplina VARCHAR(30) NOT NULL,
    creditos INT NOT NULL,
    PRIMARY KEY (id_disciplina)
);

CREATE TABLE aluno_disciplina (
    id_aluno INT NOT NULL,
    id_disciplina INT NOT NULL,
    PRIMARY KEY (id_aluno, id_disciplina),
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina(id_disciplina)
);