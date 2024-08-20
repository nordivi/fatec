alter table cidade
add primary key (codcidade)

alter table cidade
add cdestado char(2) not null, teste varchar(1) null

alter table cidade drop column teste

alter table cidade alter column cdestado varchar(2)