insert into estado values ('SP', 'S�o Paulo')

insert into cidade values ('1', 'Votorantim', 'SP')

insert into cidade (Codcidade, Nomecidade, Cdestado)
values ('2', 'Sorocaba', 'SP')

select * from cidade
left join estado on cidade.cdestado = estado.cdestado