insert into estado values ('SP', 'São Paulo')

insert into cidade values ('1', 'Votorantim', 'SP')

insert into cidade (Codcidade, Nomecidade, Cdestado)
values ('2', 'Sorocaba', 'SP')


insert into estado values ('RJ', 'Rio de Janeiro')

insert into cidade values ('3', 'Rio de Janeiro', 'RJ')

insert into cidade (Codcidade, Nomecidade, Cdestado)
values ('4','Copacabana', 'RJ')


select Nomecidade, cidade.cdestado, Nomeestado from cidade
left join estado on cidade.cdestado = estado.cdestado