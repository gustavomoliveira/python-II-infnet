.open banco.db
.mode table

drop table if exists contas;

create table contas(
	id integer primary key autoincrement,
	nome char(50) not null,
	saldo real not null);

INSERT INTO contas VALUES (null, 'André', 100);
INSERT INTO contas VALUES (null, 'Larissa', 200);
INSERT INTO contas VALUES (null, 'Mateus', 300);
INSERT INTO contas VALUES (null, 'Rafael', 400);