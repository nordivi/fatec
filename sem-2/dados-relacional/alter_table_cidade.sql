alter table cidade drop constraint PK__Cidade__9ED2CA96ADC94C7A

alter table cidade add constraint pk_codcidade primary key (codcidade)

alter table estado add primary key (cdestado)

alter table cidade add foreign key (cdestado) references estado (cdestado)
