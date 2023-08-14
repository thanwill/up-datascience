create database dw_inep;
use dw_inep;

# Criação das tabelas dimensão

create Table dim_uf (
    tf_curso bigint,
    uf varchar(2)
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
);

create table dim_ano (
    tf_ano bigint,
    ano varchar(4) ,
);

create table if not exists fact_matricula (
    tf_ano bigint,
    tf_curso bigint,
    tf_uf bigint,
    tf_municipio bigint,
    tf_ies bigint,
    tf_modalidade bigint,
    qtd_alunos bigint
);

