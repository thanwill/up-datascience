-- Active: 1693166335377@@127.0.0.1@3306@dw_inep
CREATE DATABASE IF NOT EXISTS dw_inep;

USE dw_inep;

CREATE TABLE IF NOT EXISTS dim_uf (
    tf_uf bigint,
    uf varchar(100)
);

CREATE TABLE IF NOT EXISTS dim_municipio (
    tf_municipio bigint,
    municipio varchar(100)
);

CREATE TABLE IF NOT EXISTS dim_ies (
    tf_ies bigint,
    ies varchar(100)
);

CREATE TABLE IF NOT EXISTS dim_modalidade (
    tf_modalidade bigint,
    modalidade varchar(100)
);

CREATE TABLE IF NOT EXISTS dim_curso (
    tf_curso bigint,
    curso varchar(200)
) ;


CREATE TABLE IF NOT EXISTS dim_ano (
    tf_ano bigint,
    ano varchar(4) 
) ;
CREATE TABLE IF NOT EXISTS fact_matricula (
    tf_ano bigint,
    tf_curso bigint,
    tf_uf bigint,
    tf_municipio bigint,
    tf_ies bigint,
    tf_modalidade bigint,
    matriculados bigint
);
