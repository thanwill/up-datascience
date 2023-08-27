-- Active: 1693166335377@@127.0.0.1@3306
create database dw_inep;
use dw_inep;

create Table dim_uf (
    tf_uf bigint,
    uf varchar(100)
);

create Table dim_municipio (
    tf_municipio bigint,
    municipio varchar(100)
);

create Table dim_ies (
    tf_ies bigint,
    ies varchar(100)
);

create table dim_modalidade (
    tf_modalidade bigint,
    modalidade varchar(100)
);

create Table dim_curso (
    tf_curso bigint,
    curso varchar(100)
) ;
create table dim_ano (
    tf_ano bigint,
    ano varchar(4) 
) ;
CREATE TABLE fact_matricula (
    tf_ano bigint,
    tf_curso bigint,
    tf_uf bigint,
    tf_municipio bigint,
    tf_ies bigint,
    tf_modalidade bigint,
    qtd_alunos bigint
);

INSERT INTO fact_matricula (matriculas, tf_municipio, tf_uf)

SELECT * FROM 
( SELECT 100 as matriculas ) as fact_matricula, 
( select tf_municipio from dim_municipio WHERE municipio = 'Curitiba') as tf_municipio,
( select tf_uf from dim_uf WHERE uf = 'Paraná') as tf_uf;

SELECT * FROM dim_municipio;
SELECT * FROM dim_uf;
SELECT * FROM fact_matricula;
