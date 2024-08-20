create table NotaFiscal (
Num_Nota int not null,
Cod_Cli int not null,
Serie_Nota varchar(10) not null,
Emissao_Nota smalldatetime null,
Vtot_Nota SmallMoney not null,

Constraint PK_NotaFiscal Primary Key(Num_Nota),
Constraint FK_Cliente Foreign Key(Cod_Cli) References cliente(Cod_Cli)
)
select * from NotaFiscal
