CREATE DATABASE EX1;
use EX1;

-- Item 1 --
create table Professores (
Id int Primary Key,
Nome varchar(50),
Disciplina varchar(15)
)

-- Item 2 --
insert into Professores
values (1, 'Ana Oliveira', 'Portugu�s')

-- Item 3 --
update Professores
set Nome = 'Ana Silva' where Id=1


-- Item 4 --
insert into Professores
values (2, 'Victor', 'Matem�tica'),
(3, 'Ana', 'Ci�ncias'),
(4, 'Lucas', 'Hist�ria'),
(5, 'Anne', 'Ingl�s'),
(6, 'Enzo', 'Teatro'),
(7, 'Yago', 'Geografia'),
(8, 'Giulia', 'Alem�o'),
(9, 'Luciana', 'Reda��o'),
(10, 'Vanessa', 'L�gica'),
(11, 'Miguel', 'Programa��o')

-- Item 5 --
delete from Professores where Id = 2

-- Item 6 --
create table Turmas (
Id int Primary Key,
Nome varchar(50),
ProfessorResponsavel int,
FOREIGN KEY(ProfessorResponsavel) REFERENCES Professores(Id)
)


-- Item 7 --
insert into Turmas 
values (1, '9A', 1)

-- Item 8 --
insert into Turmas
values (2, '1A', 1),
(3, '1B', 3),
(4, '1C', 4),
(5, '2A', 6),
(6, '2B', 7),
(7, '2C', 8),
(8, '3A', 9),
(9, '3B', 5),
(10, '3C', 11),
(11, '6C', 10)

-- Item 9 --
create table Alunos (
Id int Primary Key,
Nome varchar(50),
DataNascimento date,
TurmaId int,
FOREIGN KEY(TurmaId) REFERENCES Turmas(Id)
)

-- Item 10 --
insert into Alunos
values (1, 'Maria Souza', '2005-10-15', 1)

-- Item 11 --
update Alunos
set Nome = 'Maria da Silva' where Id = 1

-- Item 12 -- 
insert into Alunos
values (2, 'Enzo Miguel', '2005-11-11', 2),
(3, 'Luciana Couto', '2006-09-12', 4),
(4, 'Miguel Werneck', '2005-07-11', 3),
(5, 'Amanda Teixeira', '2006-05-12', 5),
(6, 'Vanessa Baker', '2006-03-12', 7),
(7, 'J�lia Soares', '2005-03-13', 9),
(8, 'Ana J�lia', '2006-11-14', 8),
(9, 'Mel', '2006-11-15', 6),
(10, 'Hugo', '2006-12-19', 11),
(11, 'Theo', '2004-11-22', 10)

-- Item 13 -- 
delete from Alunos where Id=2

-- Item 14 -- 
create table Notas (
Id int Primary Key,
AlunoId int,
Disciplina varchar(15),
Nota decimal(5,2),
FOREIGN KEY(AlunoId) REFERENCES Alunos(Id)
)

-- Item 15 --
insert into Notas values (1, 1, 'Matem�tica', 8.5)

-- Item 16 -- 
update Notas set Nota = 9 where Id = 1

-- Item 17 -- 
insert into Notas
values (2, 3, 'Matem�tica', 2.9),
(3, 4,  'Ingl�s', 4.2),
(4, 5,  'Portugu�s', 7.3),
(5,6,  'Geografia', 8.5),
(6,7, 'Programa��o', 2.7),
(7,8, 'Matem�tica', 9.9),
(8,9, 'Matem�tica', 10),
(9,10, 'Ingl�s', 6.2),
(10,11, 'Alem�o', 1.1),
(11,1, 'Geografia', 10)

-- Item 18 --
delete from Notas where Id = 1

-- Item 19 --
create table Matriculas (
Id int Primary Key,
AlunoId int,
TurmaId int,
DataMatricula date,
FOREIGN KEY(AlunoId) REFERENCES Alunos(Id),
FOREIGN KEY(TurmaId) REFERENCES Turmas(Id)
)


-- Item 20 --
insert into Matriculas values (1, 1, 1, '2022-02-15')

-- Item 21 -- 
insert into Matriculas
values (2, 3, 3, '2022-02-15'),
(3, 4, 2, '2022-03-16'),
(4, 5,  4, '2022-11-17'),
(5,6,  5, '2022-06-22'),
(6,7, 6, '2022-07-21'),
(7,8, 11, '2022-11-13'),
(8,9, 9, '2022-01-01'),
(9,10, 1, '2022-01-09'),
(10,11, 10, '2022-02-08'),
(11,1, 8, '2022-01-08')
-- Como foram criados 11 alunos e exclu�do 1 (10), ter� uma matr�cula de aluno repetido.