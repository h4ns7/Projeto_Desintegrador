/CRIAÇÃO DA TABELA ALUNO/
DROP TABLE IF EXISTS ALUNO CASCADE;
CREATE TABLE ALUNO (
	IDALUNO SERIAL PRIMARY KEY NOT NULL,
	NOME VARCHAR(70) NOT NULL,
	EMAIL VARCHAR(40) NOT NULL,
	CPF VARCHAR(14) UNIQUE NOT NULL,
  GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M' ,'F')),
  LOGRADOURO VARCHAR(70) NOT NULL,
  CELULAR VARCHAR(15) UNIQUE NOT NULL
);

 /CRIAÇÃO DA TABELA INSTRUTOR/
DROP TABLE IF EXISTS INSTRUTOR CASCADE;
CREATE TABLE INSTRUTOR (
	IDINSTRUTOR SERIAL PRIMARY KEY NOT NULL,
	NOME VARCHAR(70) NOT NULL,
	EMAIL VARCHAR(40) NOT NULL,
	CPF VARCHAR(15) UNIQUE NOT NULL,
  GENERO CHAR(1) NOT NULL CHECK( GENERO IN ('M' ,'F')),
  LOGRADOURO VARCHAR(70) NOT NULL,
  CELULAR VARCHAR(15) NOT NULL,
	VALORHORA NUMERIC (6,2) NOT NULL
);

/CRIAÇÃO DA TABELA CURSO/
DROP TABLE IF EXISTS CURSO CASCADE;
CREATE TABLE CURSO(
	IDCURSO SERIAL PRIMARY KEY NOT NULL,
	NOME_CURSO VARCHAR(40) NOT NULL,
	CARGA_HORARIA VARCHAR (10) NOT NULL,
	VALOR NUMERIC(6,2) NOT NULL
);

/CRIAÇÃO DA TABELA TURMA/
DROP TABLE IF EXISTS TURMA CASCADE;
CREATE TABLE TURMA( 
	IDTURMA SERIAL PRIMARY KEY NOT NULL,
	ID_CURSO INTEGER NOT NULL,
	ID_INSTRUTOR INTEGER NOT NULL,
	PERIODO CHAR(10) NOT NULL CHECK( PERIODO IN ('MATUTINO','VESPERTINO','NOTURNO')),
	SALA_TURMA CHAR(1) NOT NULL CHECK ( SALA_TURMA IN ('1','2','3') ),
	FOREIGN KEY(ID_CURSO) REFERENCES CURSO(IDCURSO) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(ID_INSTRUTOR) REFERENCES INSTRUTOR(IDINSTRUTOR) ON DELETE CASCADE ON UPDATE CASCADE 
);

/RELACINAMENTO NXN CRIA-SE OUTRA TABELA COMBINANDO SUAS CHAVES/
DROP TABLE IF EXISTS CURSO_TURMA CASCADE;
CREATE TABLE CURSO_TURMA (
	IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	IDTURMA INTEGER REFERENCES TURMA(IDTURMA),
	PRIMARY KEY (IDCURSO, IDTURMA)
);

/CRIAÇÃO DA TABELA HISTORICO/
DROP TABLE IF EXISTS HISTORICO CASCADE;
CREATE TABLE HISTORICO(
	IDHISTORICO SERIAL PRIMARY KEY NOT NULL,
	ID_ALUNO INTEGER NOT NULL,
	NUMERO_DE_VOLTAS SMALLINT NOT NULL,
	VELOCIDADE VARCHAR(10) NOT NULL,
	TEMPO VARCHAR(10) NOT NULL,
	VOLTA_MAIS_RAPIDA SMALLINT NOT NULL,
	NOTA NUMERIC (4,2) NOT NULL,
	RESULTADO CHAR(10) NOT NULL CHECK( RESULTADO IN ('APROVADO','REPROVADO')),
	FOREIGN KEY(ID_ALUNO) REFERENCES ALUNO (IDALUNO) ON DELETE CASCADE ON UPDATE CASCADE 
);


/CRIAÇÃO DA TABELA PROVA/
DROP TABLE IF EXISTS PROVA CASCADE;
CREATE TABLE PROVA(
	IDPROVA SERIAL PRIMARY KEY NOT NULL,
	ID_ALUNO INTEGER NOT NULL,
	NOME_PROVA VARCHAR (80) NOT NULL,
	TIPO_PROVA CHAR(7)  NOT NULL CHECK ( TIPO_PROVA IN ('PRÁTICA','TEÓRICA') ),
	NOTA NUMERIC(4,2) NOT NULL,
	DATA_PROVA DATE NOT NULL,
	VALOR NUMERIC(6,2) NOT NULL,
	SALA CHAR(1) NOT NULL CHECK ( SALA IN ('0', '1','2','3') ),
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO(IDALUNO) ON DELETE CASCADE ON UPDATE CASCADE 
);

/RELACINAMENTO NXN CRIA-SE OUTRA TABELA COMBINANDO SUAS CHAVES/
DROP TABLE IF EXISTS CURSO_PROVA CASCADE;
CREATE TABLE CURSO_PROVA (
	IDCURSO INTEGER REFERENCES CURSO(IDCURSO),
	IDPROVA INTEGER REFERENCES PROVA(IDPROVA),
	PRIMARY KEY(IDCURSO, IDPROVA)	
);


/CRIAÇÃO DA TABELA MATRICULA/
DROP TABLE IF EXISTS MATRICULA CASCADE;
CREATE TABLE MATRICULA(
	IDMATRICULA INTEGER PRIMARY KEY,
	DATA_MATRICULA DATE NOT NULL,
	ID_ALUNO INTEGER NOT NULL,
	ID_CURSO INTEGER NOT NULL, 
	ID_TURMA INTEGER NOT NULL,
	ID_HISTORICO INTEGER,
	FOREIGN KEY (ID_ALUNO) REFERENCES ALUNO (IDALUNO) ON DELETE CASCADE ON UPDATE CASCADE ,
	FOREIGN KEY (ID_CURSO) REFERENCES CURSO (IDCURSO) ON DELETE CASCADE ON UPDATE CASCADE ,
	FOREIGN KEY (ID_TURMA) REFERENCES TURMA (IDTURMA) ON DELETE CASCADE ON UPDATE CASCADE ,
	FOREIGN KEY (ID_HISTORICO) REFERENCES HISTORICO (IDHISTORICO) ON DELETE CASCADE ON UPDATE CASCADE 
);



-- POPULANDO A TABELA DE ALUNO
INSERT INTO ALUNO VALUES (default, 'Lucas Pereira', 'lukinhas.pereira@email.com', '615.911.780-70', 'M', 'Rua Mozart, 89 - Vila Arco-Iris', '(11) 94002-8922');
INSERT INTO ALUNO VALUES (default, 'Diego Müller', 'diego.muller@email.com', '046.832.670-71', 'M', 'Rua das Araras, 101 - Jardim Labitária', '(11) 91214-2356');
INSERT INTO ALUNO VALUES (default, 'Darcilei Alves', 'darci.alves@email.com', '418.912.730-27', 'F', 'Av. Python, 56 - Bairro Butantan', '(11) 94397-9574');
INSERT INTO ALUNO VALUES (default, 'Rafael Silva', 'rafael.silva@email.com', '990.469.710-82', 'M', 'Rua Caminho do Mar, 21 - Grajáu', '(11) 92526-4083');
INSERT INTO ALUNO VALUES (default, 'José Mbappé', 'jose.mbappe@email.com', '614.305.470-30', 'M', 'Rua dos Pombos, 57 - Vila Paris', '(11) 2179-4866');
INSERT INTO ALUNO VALUES (default, 'Marcos Casimero', 'marcos.casimero@email.com', '714.454.460-81', 'M', 'Rua Real Madrid, 01 - Bairro Das Clarezas', '(11) 3103-9149');
INSERT INTO ALUNO VALUES (default, 'Cristiane Paula Oliveira', 'cris.oliveira@email.com', '911.158.630-37', 'F', 'Rua Ângelo Cristianini, 89 - Vila Belmiro', '(11) 2103-1803');
INSERT INTO ALUNO VALUES (default, 'Rodrigo Correa', 'rodrigo.correa@email.com', '572.349.710-33', 'M', 'Rua Maças da Primavera, 569 - Vila das Mêrces', '(11) 2213-6151');
INSERT INTO ALUNO VALUES (default, 'Maria Clara Neves', 'maria.neves@email.com', '403.332.150-01', 'F', 'Rua Frei Lisboa, 687 - Jardim Madalena', '(11) 2821-1050');
INSERT INTO ALUNO VALUES (default, 'Luiz Ferreira', 'luiz.ferreira@email.com', '856.376.860-33', 'M', 'Av. Yearvant Kissayian, 235 - Vila Joaniza', '(11) 3207-3733');
INSERT INTO ALUNO VALUES (default, 'Carlos Eduardo Rodrigues', 'cadu.rodrigues@email.com', '439.709.610-41', 'M', 'Rua Zavuvus, 27 - Vila Santa Clara', '(11) 2594-6632');
INSERT INTO ALUNO VALUES (default, 'Vinicius Junior Santos', 'vini.malvadeza@email.com', '718.073.800-09', 'M', 'Rua Copacabana, 1457 - Detroit', '(11) 2788-3796');
INSERT INTO ALUNO VALUES (default, 'Bruna Reis', 'bruna.reis@email.com', '336.368.990-07', 'F', 'Av. Rio Grande, 42 - Vila Das Rosas', '(11) 2313-8313');
INSERT INTO ALUNO VALUES (default, 'Milena Castro', 'milena.castro@email.com', '916.934.930-47', 'F', 'Av. Frei Dom João, 987 - Ipiranga', '((11) 3837-0605');
INSERT INTO ALUNO VALUES (default, 'Sandra Pichum', 'sandra.pichum@email.com', '533.962.080-80', 'F', 'Av. Bento XV, 63 - Vila Missionária', '(11) 2031-5895');
INSERT INTO ALUNO VALUES (default, 'Maria Eduarda Ribeiro', 'maria.ribeiro@email.com', '655.569.270-73', 'F', 'Av. Miguel Yunes, 1002 - Interlagos', '(11) 3253-73132');
INSERT INTO ALUNO VALUES (default, 'Gabriel Florentino', 'biel.florentino@email.com', '287.710.530-00', 'M', 'Rua Frei Dom Costa, 99 - Jardim Selma', '(11) 3082-8418');
INSERT INTO ALUNO VALUES (default, 'Julia Meneses', 'juh.meneses@email.com', '240.069.240-89', 'F', 'AV. Ponte Nova, 36 - Vila Palmares', '(11) 2642-8883');
INSERT INTO ALUNO VALUES (default, 'Giovanna Lopes', 'giovanna.lopes@email.com', '405.888.490-81', 'F', 'Rua Luciano Moratore, 77 - Vila Atlântica', '(11) 3307-5756');
INSERT INTO ALUNO VALUES (default, 'Hugo Mol', 'hugo.mol@email.com', '993.717.390-61', 'M', 'Rua Papa Gregório, 347 - Vila Atlântica', '(11) 2555-3077');

select * from aluno;

-- POPULANDO A TABELA DE INSTRUTOR
INSERT INTO INSTRUTOR VALUES (default, 'Rogério Vieira', 'rogerio.vieira@pilotschool.com', '554.367.280-22', 'M', 'Rua Querubim, 332 - Vila Maria', '(11) 2109-7830', 550.00);
INSERT INTO INSTRUTOR VALUES (default, 'Rodney Ribeiro', 'rodney.ribeiro@pilotschool.com', '036.390.380-10', 'M', 'Av. Imaculada Conceição, 92 - Interlagos', '(11) 2460-1928', 650.00);
INSERT INTO INSTRUTOR VALUES (default, 'Regina Bachega', 'regina.bachega@pilotschool.com', '120.021.880-92', 'F', 'Rua Ernesto Torres, 01 - Vila Camburiu', '(11) 2193-8724', 550.00);
INSERT INTO INSTRUTOR VALUES (default, 'Atena Deveche', 'atena.deveche@pilotschool.com', '955.457.610-20', 'F', 'Rua Carlos Augusto, 4156 - Pinheiros', '(11) 3245-3174', 650.00);
INSERT INTO INSTRUTOR VALUES (default, 'Antonella Novais', 'antonella.novais@pilotschool.com', '068.294.910-88', 'F', 'Av. Brigadeiro Faria, 2358 - Vila Nova Conceição', '(11) 3313-3235', 650.00);
INSERT INTO INSTRUTOR VALUES (default, 'Isaias Lima', 'isaias.lima@pilotschool.com', '289.722.460-69', 'M', 'Rua Pampilho, 3657 - Santo Amaro', '(11) 3737-1651', 550.00);

select * from instrutor;

-- POPULANDO A TABELA DE CURSO
INSERT INTO CURSO VALUES (default, 'Direção Defensiva', '8h', 4050.99);
INSERT INTO CURSO VALUES (default, 'Direção Esportiva', '20h', 6500.99);

select * from curso;

-- POPULANDO A TABELA DE TURMA
INSERT INTO TURMA VALUES (default, 1, 1, 'MATUTINO', 1);
INSERT INTO TURMA VALUES (default, 2, 2, 'MATUTINO', 2);
INSERT INTO TURMA VALUES (default, 1, 3, 'VESPERTINO', 1);
INSERT INTO TURMA VALUES (default, 2, 4, 'VESPERTINO', 2);
INSERT INTO TURMA VALUES (default, 1, 5, 'NOTURNO', 2);
INSERT INTO TURMA VALUES (default, 2, 6, 'NOTURNO', 1);

select * from turma;

-- POPULANDO A TABELA DE CURSO_TURMA
INSERT INTO curso_turma VALUES (1, 1);
INSERT INTO curso_turma VALUES (2, 2);
INSERT INTO curso_turma VALUES (1, 3);
INSERT INTO curso_turma VALUES (2, 4);
INSERT INTO curso_turma VALUES (1, 5);
INSERT INTO curso_turma VALUES (2, 6);

select * from curso_turma;

-- POPULANDO A TABELA DE PROVA
INSERT INTO PROVA VALUES (default, 1, 'Prova Prática Defensiva', 'PRÁTICA', 8, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 0, 'Prova Prática Defensiva', 'PRÁTICA', 7, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 5, 'Prova Prática Defensiva', 'PRÁTICA', 9, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 7, 'Prova Prática Defensiva', 'PRÁTICA', 10, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 8, 'Prova Prática Defensiva', 'PRÁTICA', 6, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 9, 'Prova Prática Defensiva', 'PRÁTICA', 4, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 11, 'Prova Prática Defensiva', 'PRÁTICA', 9, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 10, 'Prova Prática Defensiva', 'PRÁTICA', 7, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 15, 'Prova Prática Defensiva', 'PRÁTICA', 0, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 17, 'Prova Prática Defensiva', 'PRÁTICA', 10, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 19, 'Prova Prática Defensiva', 'PRÁTICA', 8, '2022-11-18', 50.00, 0);
INSERT INTO PROVA VALUES (default, 1, 'Prova Teórica Defensiva', 'TEÓRICA', 8, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 3, 'Prova Teórica Defensiva', 'TEÓRICA', 7, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 5, 'Prova Teórica Defensiva', 'TEÓRICA', 9, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 7, 'Prova Teórica Defensiva', 'TEÓRICA', 10, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 8, 'Prova Teórica Defensiva', 'TEÓRICA', 6, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 9, 'Prova Teórica Defensiva', 'TEÓRICA', 4, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 11, 'Prova Teórica Defensiva', 'TEÓRICA', 9, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 13, 'Prova Teórica Defensiva', 'TEÓRICA', 7, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 15, 'Prova Teórica Defensiva', 'TEÓRICA', 3, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 17, 'Prova Teórica Defensiva', 'TEÓRICA', 10, '2022-11-22', 50.00, 3);
INSERT INTO PROVA VALUES (default, 19, 'Prova Prática Defensiva', 'TEÓRICA', 8, '2022-11-22', 50.00, 3);

INSERT INTO PROVA VALUES (default, 2, 'Prova Prática Esportiva', 'PRÁTICA', 8, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 4, 'Prova Prática Esportiva', 'PRÁTICA', 7, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 6, 'Prova Prática Esportiva', 'PRÁTICA', 9, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 8, 'Prova Prática Esportiva', 'PRÁTICA', 10, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 10, 'Prova Prática Esportiva', 'PRÁTICA', 6, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 12, 'Prova Prática Esportiva', 'PRÁTICA', 4, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 14, 'Prova Prática Esportiva', 'PRÁTICA', 9, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 16, 'Prova Prática Esportiva', 'PRÁTICA', 7, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 17, 'Prova Prática Esportiva', 'PRÁTICA', 3, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 18, 'Prova Prática Esportiva', 'PRÁTICA', 10, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 20, 'Prova Prática Esportiva', 'PRÁTICA', 8, '2022-11-18', 80.00, 0);
INSERT INTO PROVA VALUES (default, 2, 'Prova Teórica Esportiva', 'TEÓRICA', 8, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 4, 'Prova Teórica Esportiva', 'TEÓRICA', 7, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 6, 'Prova Teórica Esportiva', 'TEÓRICA', 9, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 8, 'Prova Teórica Esportiva', 'TEÓRICA', 10, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 10, 'Prova Teórica Esportiva', 'TEÓRICA', 6, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 12, 'Prova Teórica Esportiva', 'TEÓRICA', 4, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 14, 'Prova Teórica Esportiva', 'TEÓRICA', 9, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 16, 'Prova Teórica Esportiva', 'TEÓRICA', 7, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 17, 'Prova Teórica Esportiva', 'TEÓRICA', 3, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 18, 'Prova Teórica Esportiva', 'TEÓRICA',10, '2022-11-22', 80.00, 2);
INSERT INTO PROVA VALUES (default, 20, 'Prova Teórica Esportiva', 'TEÓRICA', 8, '2022-11-22', 80.00, 2);

select * from prova;

-- POPULANDO A TABELA DE HISTORICO
INSERT INTO historico VALUES (default, 1, 10, '100 KM/H', '2min00s785', 3, 7.8, 'APROVADO');
INSERT INTO historico VALUES (default, 2, 10, '200 KM/H', '1min53s689', 2, 8.6, 'APROVADO');
INSERT INTO historico VALUES (default, 3, 10, '80 KM/H', '3min13s785', 5, 4.7, 'REPROVADO');
INSERT INTO historico VALUES (default, 4, 10, '202 KM/H', '1min36s735', 7, 8.0, 'APROVADO');
INSERT INTO historico VALUES (default, 5, 10, '110 KM/H', '1min59s547', 2, 9.1, 'APROVADO');
INSERT INTO historico VALUES (default, 6, 10, '220 KM/H', '1min01s785', 1, 9.6, 'APROVADO');
INSERT INTO historico VALUES (default, 7, 10, '100 KM/H', '2min13s720', 9, 7.0, 'APROVADO');
INSERT INTO historico VALUES (default, 8, 10, '100 KM/H', '3min13s785', 6, 3.9, 'REPROVADO');
INSERT INTO historico VALUES (default, 9, 10, '98 KM/H', '2min00s455', 4, 8.0, 'APROVADO');
INSERT INTO historico VALUES (default, 10, 10, '210 KM/H', '1min47s689', 8, 8.9, 'APROVADO');
INSERT INTO historico VALUES (default, 11, 10, '100 KM/H', '2min56s585', 10, 7.0, 'APROVADO');
INSERT INTO historico VALUES (default, 12, 10, '180 KM/H', '2min30s365', 3, 5.7, 'REPROVADO');
INSERT INTO historico VALUES (default, 13, 10, '70 KM/H', '4min20s785', 3, 6.1, 'APROVADO');
INSERT INTO historico VALUES (default, 14, 10, '250 KM/H', '0min59s869', 7, 9.7, 'APROVADO');
INSERT INTO historico VALUES (default, 15, 10, '90 KM/H', '3min45s298', 3, 7.6, 'APROVADO');
INSERT INTO historico VALUES (default, 16, 10, '110 KM/H', '3min48s654', 8, 2.0, 'REPROVADO');
INSERT INTO historico VALUES (default, 17, 10, '50 KM/H', '3min13s785', 9, 2.5, 'REPROVADO');
INSERT INTO historico VALUES (default, 18, 10, '230 KM/H', '1min10s812', 5, 9.5, 'APROVADO');
INSERT INTO historico VALUES (default, 19, 10, '110 KM/H', '2min30s785', 6, 9.0, 'APROVADO');
INSERT INTO historico VALUES (default, 20, 10, '228 KM/H', '1min16s797', 7, 8.9, 'APROVADO');

select * from historico

-- POPULANDO A TABELA DE CURSO PROVA
INSERT INTO curso_prova VALUES(1, 1);
INSERT INTO curso_prova VALUES(1, 2);
INSERT INTO curso_prova VALUES(1, 3);
INSERT INTO curso_prova VALUES(1, 4);
INSERT INTO curso_prova VALUES(1, 5);
INSERT INTO curso_prova VALUES(1, 6);
INSERT INTO curso_prova VALUES(1, 7);
INSERT INTO curso_prova VALUES(1, 8);
INSERT INTO curso_prova VALUES(1, 9);
INSERT INTO curso_prova VALUES(1, 10);
INSERT INTO curso_prova VALUES(1, 11);
INSERT INTO curso_prova VALUES(1, 12);
INSERT INTO curso_prova VALUES(1, 13);
INSERT INTO curso_prova VALUES(1, 14);
INSERT INTO curso_prova VALUES(1, 15);
INSERT INTO curso_prova VALUES(1, 16);
INSERT INTO curso_prova VALUES(1, 17);
INSERT INTO curso_prova VALUES(1, 18);
INSERT INTO curso_prova VALUES(1, 19);
INSERT INTO curso_prova VALUES(1, 20);
INSERT INTO curso_prova VALUES(1, 21);
INSERT INTO curso_prova VALUES(1, 22);

INSERT INTO curso_prova VALUES(2, 23);
INSERT INTO curso_prova VALUES(2, 24);
INSERT INTO curso_prova VALUES(2, 25);
INSERT INTO curso_prova VALUES(2, 26);
INSERT INTO curso_prova VALUES(2, 27);
INSERT INTO curso_prova VALUES(2, 28);
INSERT INTO curso_prova VALUES(2, 29);
INSERT INTO curso_prova VALUES(2, 30);
INSERT INTO curso_prova VALUES(2, 31);
INSERT INTO curso_prova VALUES(2, 32);
INSERT INTO curso_prova VALUES(2, 33);
INSERT INTO curso_prova VALUES(2, 34);
INSERT INTO curso_prova VALUES(2, 35);
INSERT INTO curso_prova VALUES(2, 36);
INSERT INTO curso_prova VALUES(2, 37);
INSERT INTO curso_prova VALUES(2, 38);
INSERT INTO curso_prova VALUES(2, 39);
INSERT INTO curso_prova VALUES(2, 40);
INSERT INTO curso_prova VALUES(2, 41);
INSERT INTO curso_prova VALUES(2, 42);
INSERT INTO curso_prova VALUES(2, 43);
INSERT INTO curso_prova VALUES(2, 44);

select * from curso_prova;