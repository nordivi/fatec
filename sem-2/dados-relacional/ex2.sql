CREATE DATABASE EX02;
use EX02;

-- Item 1 --
create table Tbl_Clientes (
Id int Primary Key,
Nome varchar(50),
Email varchar(100),
Telefone  varchar(15)
)

-- Item 2 --
insert into Tbl_Clientes
values (1, 'João Silva', 'joao@email.com',  '(11) 1234-5678')

-- Item 3 --
INSERT INTO Tbl_Clientes
VALUES (2, 'Ana Souza', 'ana.souza@example.com', '(11) 98765-4321'),
(3, 'Carlos Pereira', 'carlos.pereira@example.com', '(21) 97654-3210'),
(4, 'Beatriz Lima', 'beatriz.lima@example.com', '(31) 96543-2109'),
(5, 'Eduardo Costa', 'eduardo.costa@example.com', '(41) 95432-1098'),
(6, 'Fernanda Martins', 'fernanda.martins@example.com', '(51) 94321-0987'),
(7, 'Gabriel Silva', 'gabriel.silva@example.com', '(61) 93210-9876'),
(8, 'Juliana Oliveira', 'juliana.oliveira@example.com', '(71) 92109-8765'),
(9, 'Lucas Almeida', 'lucas.almeida@example.com', '(81) 91098-7654'),
(10, 'Mariana Rodrigues', 'mariana.rodrigues@example.com', '(91) 90987-6543'),
(11, 'Pedro Santos', 'pedro.santos@example.com', '(11) 89876-5432');


-- Item 4 --
update Tbl_Clientes
set Telefone = '(11) 8765-4321' where Id = 1

-- Item 5 --
create table Tbl_Produtos (
Id int Primary Key,
Nome varchar(50),
Preco decimal,
Estoque  int,
)

-- Item 6 --
insert into Tbl_Produtos
values (1, 'Camiseta', 29.99,  100)


-- Item 7 --
INSERT INTO Tbl_Produtos VALUES
(2, 'Smartphone X20', 299.99, 150),
(3, 'Laptop Pro 15', 1199.99, 30),
(4, 'Fone de Ouvido Wireless', 89.99, 75),
(5, 'Relógio Fitness Tracker', 149.50, 40),
(6, 'Câmera DSLR 4K', 899.99, 25),
(7, 'Tablet Ultra HD', 499.00, 60),
(8, 'Caixa de Som Bluetooth', 79.95, 100),
(9, 'Teclado Mecânico RGB', 129.90, 55),
(10, 'Mouse Gamer Elite', 69.75, 85),
(11, 'Monitor 27" 4K', 299.20, 20);

-- Item 8 --
update Tbl_Produtos
set Preco = 39.99 where Id = 1

-- Item 9 --
create table Tbl_Pedidos (
Id int Primary Key,
ClienteId int,
ProdutoId int,
Quantidade int,
DataPedido date,
FOREIGN KEY(ClienteId) REFERENCES Tbl_Clientes(Id),
FOREIGN KEY(ProdutoId) REFERENCES Tbl_Produtos(Id)
)

-- Item 10 --
insert into Tbl_Pedidos
values (1, 1, 1, 2, GETDATE())

-- Item 11 --
update Tbl_Pedidos
set Quantidade = 3 where Id = 1

-- Item 12 -- 
INSERT INTO Tbl_Pedidos (Id, ClienteId, ProdutoId, Quantidade, DataPedido) VALUES
(4, 3, 2, 1, '2024-08-01'),
(6, 2, 3, 2, '2024-08-02'),
(2, 5, 4, 1, '2024-08-03'),
(5, 4, 5, 3, '2024-08-04'),
(3, 8, 6, 2, '2024-08-05'),
(9, 7, 7, 5, '2024-08-06'),
(8, 6, 8, 1, '2024-08-07'),
(7, 11, 9, 4, '2024-08-08'),
(11, 10, 10, 2, '2024-08-09'),
(10, 9, 11, 1, '2024-08-10');

-- Item 13 -- 
create table Tbl_Funcionarios (
Id int Primary Key,
Nome varchar(50),
Cargo varchar(50),
Salario decimal,
)

-- Item 14 -- 
insert into Tbl_Funcionarios
values (1, 'Maria Santos', 'Gerente', 5000 )

-- Item 15 --
update Tbl_Funcionarios set Salario = 6000 where Id = 1

-- Item 16 -- 
INSERT INTO Tbl_Funcionarios VALUES
(2, 'Mariana Santos', 'Analista de Sistemas', 7500.00),
(3, 'Ricardo Oliveira', 'Gerente de Projetos', 10500.00),
(4, 'Laura Martins', 'Desenvolvedora Front-End', 6200.00),
(5, 'Pedro Almeida', 'Coordenador de TI', 8500.00),
(6, 'Ana Beatriz', 'Assistente Administrativo', 3400.00),
(7, 'Lucas Silva', 'Especialista em Banco de Dados', 9000.00),
(8, 'Fernanda Costa', 'Designer Gráfico', 4500.00),
(9, 'Tiago Pereira', 'Consultor de Marketing', 7800.00),
(10, 'Juliana Castro', 'Engenheira de Software', 9500.00),
(11, 'Gabriel Souza', 'Analista de Suporte', 5000.00);

-- Item 17 -- 
create table Tbl_Vendas (
Id int Primary Key,
ProdutoId int,
Quantidade int,
ValorTotal int,
DataVenda date,
FOREIGN KEY(ProdutoId) REFERENCES Tbl_Produtos(Id),
)

-- Item 18 --
insert into Tbl_Vendas
values (1, 1, 2, 79.98, GETDATE() )

-- Item 19 --
INSERT INTO Tbl_Vendas VALUES
(2, 2, 3, 899.97, '2024-08-01'),
(3, 4, 1, 1199.99, '2024-08-02'),
(4, 3, 5, 449.95, '2024-08-03'),
(5, 6, 2, 299.00, '2024-08-04'),
(6, 5, 1, 899.99, '2024-08-05'),
(7, 7, 4, 1996.00, '2024-08-06'),
(8, 9, 3, 239.85, '2024-08-07'),
(9, 8, 6, 779.40, '2024-08-08'),
(10, 11, 2, 139.50, '2024-08-09'),
(11, 10, 1, 299.20, '2024-08-10');


-- Item 20 --
delete from Tbl_Vendas where Id = 1