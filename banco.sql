
/*CRIAÇÃO DA TABELA ALUNO*/

CREATE TABLE IF NOT EXISTS ALUNO (
	IDALUNO SERIAL PRIMARY KEY NOT NULL,
	NOME VARCHAR(70) NOT NULL,
	EMAIL VARCHAR(40) NOT NULL,
	CPF VARCHAR(15) UNIQUE,
  GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M' ,'F')),
  LOGRADOURO VARCHAR(70) NOT NULL,
  CELULAR VARCHAR(11) NOT NULL
);



/*CRIAÇÃO DA TABELA ENDEREÇO*/

/*
CREATE TABLE ENDERECO(
	IDENDERECO SERIAL PRIMARY KEY NOT NULL,
	RUA VARCHAR(30) NOT NULL,
	BAIRRO VARCHAR(30) NOT NULL,
	CIDADE VARCHAR (30) NOT NULL,
	ESTADO_CADASTRO ESTADO NOT NULL,
	NUMERO VARCHAR(10) NOT NULL,
	CEP VARCHAR(10) NOT NULL,
	ID_ALUNO INTEGER UNIQUE,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO),
	ID_INSTRUTOR INTEGER UNIQUE,
	FOREIGN KEY (ID_INSTRUTOR) REFERENCES INSTRUTOR (IDINSTRUTOR)
);

*/

/* CRIAÇÃO ENUM PARA TELEFONE

/* CREATE TYPE TIPO AS ENUM('RES','COM','CEL');

CRIAÇÃO DA TABELA TELEFONE

CREATE TABLE TELEFONE(
	IDTELEFONE INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	TIPO_NUMERO TIPO NOT NULL,
	NUMERO VARCHAR(11) NOT NULL,
	ID_ALUNO INTEGER,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO),
	ID_INSTRUTOR INTEGER,
	FOREIGN KEY (ID_INSTRUTOR) REFERENCES INSTRUTOR (IDINSTRUTOR)
	
);

*/

/* CRIAÇÃO ENUM PARA CURSO */

CREATE TYPE CARGA AS ENUM('20 Horas','40 Horas','60 Horas');

/*CRIAÇÃO DA TABELA CURSO*/

CREATE TABLE CURSO(
	IDCURSO INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	NOME_CURSO VARCHAR(30) NOT NULL,
	CARGA_HORARIA CARGA NOT NULL,
	VALOR NUMERIC(6,2) NOT NULL
);

/* CRIAÇÃO ENUM PARA TURMA */

CREATE TYPE PERIODO AS ENUM('Matutino','Vespertino','Noturno');
CREATE TYPE SALA_TURMA AS ENUM('1','2','3');


/*CRIAÇÃO DA TABELA TURMA*/


CREATE TABLE TURMA(
	IDTURMA INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	HORARIO PERIODO  NOT NULL,
	SALA SALA_TURMA NOT NULL,
	ID_INSTRUTOR INTEGER,
	FOREIGN KEY(ID_INSTRUTOR) REFERENCES INSTRUTOR(IDINSTRUTOR)
);

/*RELACINAMENTO NXN CRIA-SE OUTRA TABELA COMBINANDO SUAS CHAVES*/

CREATE TABLE CURSO_TURMA (
	IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	IDTURMA INTEGER REFERENCES TURMA(IDTURMA),
	PRIMARY KEY (IDCURSO,IDTURMA)

);


/*CRIAÇÃO DA TABELA INSTRUTOR*/

CREATE TABLE INSTRUTOR(
	IDINSTRUTOR INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	NOME VARCHAR(30) NOT NULL,
	SEXO_INSTRUTOR SEXO,
	EMAIL VARCHAR(50) UNIQUE,
	CPF VARCHAR(15) UNIQUE,
	DATA_NASCIMENTO DATE NOT NULL

);



/* CRIAÇÃO ENUM PARA HISTORICO */

CREATE TYPE APROVADO AS ENUM('Aprovado','Reprovado');

/*CRIAÇÃO DA TABELA HISTORICO*/

CREATE TABLE HISTORICO(
	IDHISTORICO INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	APROVACAO APROVADO NOT NULL,
	VELOCIDADE NUMERIC (6,2) NOT NULL,
	FREQUENCIA NUMERIC (4,2),
	VOLTA_MAIS_RAPIDA NUMERIC (6,2) UNIQUE NOT NULL,
	NOTA NUMERIC (4,2) NOT NULL

);




/*CRIAÇÃO DA TABELA PROVA*/

CREATE TABLE PROVA(
	IDPROVA INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	NOME_PROVA VARCHAR (30) NOT NULL,
	NOTA NUMERIC(4,2) NOT NULL,
	DATA_PROVA DATE NOT NULL,
	VALOR NUMERIC(6,2) NOT NULL,
	SALA SALA_TURMA NOT NULL,
	ID_ALUNO INTEGER,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO)
);

/*RELACINAMENTO NXN CRIA-SE OUTRA TABELA COMBINANDO SUAS CHAVES*/

CREATE TABLE CURSO_PROVA (
	IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	IDPROVA INTEGER REFERENCES PROVA(IDPROVA),
	PRIMARY KEY(IDCURSO,IDPROVA)
	
);


/*CRIAÇÃO DA TABELA MATRICULA*/

CREATE TABLE MATRICULA(
	IDMATRICULA INTEGER DEFAULT NEXTVAL('INCREMENTO_ID') PRIMARY KEY,
	DATA_MATRICULA DATE NOT NULL,
	ID_ALUNO INTEGER,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO),
	ID_TURMA INTEGER,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO),
	ID_HISTORICO INTEGER,
	FOREIGN KEY (ID_HISTORICO) REFERENCES HISTORICO(IDHISTORICO)
);