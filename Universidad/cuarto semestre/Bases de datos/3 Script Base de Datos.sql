drop database if exists empresa;
create database empresa;
use empresa;

drop table if exists empleados;
drop table if exists cargo;
drop table if exists proveedores;
drop table if exists clientes;
drop table if exists sucursal;
drop table if exists productos;
drop table if exists factura;
drop table if exists detallefactura;

create table cargo(
	codigo char(2),
	nombre varchar(15),
	salario int(9) default 1000000,
	primary key(codigo));

create table proveedores(
	nit varchar(10),
	nombre varchar(15),
	direccion varchar(30),
	telefono char(7),
	contacto char(20),
	primary key(nit));

create table clientes(
	cedula varchar(10),
	nombres varchar(15),
	apellidos varchar(15),
	direccion varchar(30),
	telefono char(7),
	primary key(cedula));

create table empleados(
	codigo char(5),
	nombres varchar(15),
	apellidos varchar(15),
	direccion varchar(30),
	telefono char(7),
	fe_nacimiento date,
	fe_ingreso date,
	estado char(1) default "1",
	sucursal char(2),
	cargo char(2), primary key(codigo));

create table sucursal(
	codigo char(2),
	nombre varchar(30),
	direccion varchar(30),
	gerente char(5),
	primary key(codigo));

alter table empleados add CONSTRAINT FKSUCURSAL foreign key(sucursal) references sucursal(codigo) on delete cascade;
alter table sucursal add CONSTRAINT FKGERENTE foreign key(gerente) references empleados(codigo) on delete cascade;

create table productos(
	codigo char(5),
	nombre varchar(30),
	pcompra float(6,0),
	pventa float(6,0),
	cantidad int(4),
	proveedor varchar(10),
	primary key(codigo));

create table factura(
	consecutivo int(5),
	fecha date,
	cliente varchar(10),
	vendedor char(5),
	sucursal char(2),
	tipo char(1) default "1",
	primary key(consecutivo));

alter table factura add CONSTRAINT FKCLIENTE foreign key(cliente) references clientes(cedula) on delete cascade;
alter table factura add CONSTRAINT FKVENDEDOR foreign key(vendedor) references empleados(codigo) on delete cascade;
alter table factura add CONSTRAINT FKSUCURSAL1 foreign key(sucursal) references sucursal(codigo) on delete cascade;

create table detallefactura(consecutivo int(5), producto char(5), cantidad int(3));

alter table detallefactura add CONSTRAINT FKCONSECUTIVO foreign key(consecutivo) references factura(consecutivo) on delete cascade;
alter table detallefactura add CONSTRAINT FKPRODUCTO foreign key(producto) references productos(codigo) on delete cascade;

delete from productos;
insert into productos values( "AD011","ADITIVO PARA DIESEL",8000,8400,30,"24576225-1"),--
( "AD012","ADITIVO PARA MOTORES A GASOLINA",7800,8400,20,"24576225-1"),
( "AD013","AGUA REFRIGERANTE",12000,12700,20,"24576225-1"),
( "AD014","ADITIVO LIMPIA PARABRISAS",1000,700,200,"24576225-1"),
( "AD015","CROMATOS",700,4500,130,"24576225-1"),
( "AD016","GRASA RETINAX * 250 GMS",8000,8400,20,"24576225-1"),
( "AD017","GRASA AZUL DE LITIO",9400,9600,30,"24576225-1"),
( "AD018","GRASA AZUL DE LITIO",8000,8400,30,"24576225-1"),
( "AD019","SILICONA EMULSIONADA",7000,8400,20,"24576225-1"),
( "AD020","SILICONA AZUL",4400,5200,10,"24576225-1"),
( "AD021","SILICONA ROJA",4400,5200,8,"24576225-1"),
( "AD022","SILICONA AZUL",4400,5200,0,"24576225-1"),
( "OT023","BILLETERAS DOCUMENTOS",5000,3500,0,"24576225-1"),
( "OT024","TOALLAS - DULCE ABRIGO",3000,2750,1,"24576225-1");


insert into productos values( "AC001","MOBIL 15W40 * 1/4",10600,9600,300,"24573748-2"),
( "AC002","MOBIL DELVAC 50",8500,9700,114,"24573748-2"),
( "AC003","ACEITE SPIRAX 140 * 1/4",12000,12500,187,"24573748-2"),
( "AC004","ACEITE SPIRAX 250 * 1/4",12000,12600,300,"24573748-2"),
( "AC005","ACEITE RIMULA 15W40 * 1/4",11000,11700,63,"24573748-2"),
( "AC006","ACEITE RIMULA 20W60",11500,12700,45,"24573748-2"),
( "AC007","ACEITE RIMULA D 50 * 1/4",10000,10800,25,"24573748-2"),
( "AC008","ACEITE RIMULA D * 1/4 GRANEL",9200,9600,300,"24573748-2"),
( "AC009","VALVULINA XXX * 1/4",5000,5700,421,"24573748-2"),
( "AC010","ACEITE TECTION 50 * 1/4",12000,13200,0,"24573748-2"),
( "AC011","ACEITE URSA 50",8600,9600,0,"24573748-2");

delete from proveedores;
INSERT INTO PROVEEDORES VALUES("24576225-1","PETROLABS DE COLOMBIA","AV CRA 68 No. 85A-23","2174563","FRANCIA ELENA CUBIDES");
INSERT INTO PROVEEDORES VALUES("24573748-2","INSERCOL S.A","AUTOPISTA SUR VIA A GIRON","6231089","RICARDO MENDOZA GOMEZ");

delete from clientes;
INSERT INTO  CLIENTES VALUES
("4377130","LEONARDO FABIO","VALENCIA RICO","CRA 27 # 21-11","7393592"),
("92227452","VICTOR MANUEL","PARRA VARGAS","MANZANA 11 # 3 MONTEVIDEO","7408247"),
("75080501","GUSTAVO ADOLFO","TOLOZA","CL 21 15-09 AP 601 EDIF. JOSE MARIA CORDOBA","7442125"),
("18396606","FABIAN","SUAREZ RODRIGUEZ","CRA 15 18N-13 AP 301","7466147"),
("18400000","CARLOS HERNAN","SUAREZ RODRIGUEZ","CRA 14 11-36","7424090"),
("7777777777","CLIENTES VARIOS ARMENIA","CLIENTES VARIOS","ARMENIA","7373737"),
("33819984","LUZ MARINA","GIRON PEREA","CRA 20 9-65","7482659"),
("33819986","LUCY","GOMEZ PE?UELA","CL 9 14-08 LOCAL 1","7456949"),
("33872000","ROSEMARY","RAMIREZ GOMEZ","CLL 5 No. 20-00 B 18 APTO 403","7455264"),
("41375231","SANDRA JENNY","BERSH ARIAS","CRA 13 19-29 EDIFICIO PLAZUELA","7440874"),
("77074523","TIBERIO","ORTIZ","CL 9 17-35","7468814");


DELETE FROM CARGO;
INSERT INTO CARGO VALUES
("01","GERENTE",4900000),
("02","SECRETARIA",1000000),
("03","VENDEDOR",890000),
("04","AUXILIAR CONTABLE",890000),
("05","CONTADOR",2155000),
("06","OPERADOR", 890000),
("07","CAJERO",1115000);

INSERT INTO SUCURSAL(codigo,nombre,direccion) VALUES
("01","SUCURSAL ESTACION TERPEL","CLL 19N VIA PEREIRA"),
("02","PARADOR DE CAMIONES","KM 2 VIA AL VALLE"),
("03","ESTACION DE SERVICIO VERSALLES","KM 18 VIA IBAGUE");

DELETE FROM EMPLEADOS;
INSERT INTO EMPLEADOS VALUES
("01-01","ENRIQUE","LONDONO VILLEGAS","CL 15 12-53","7454043",date_format("1970-05-30","%y-%m-%d"),date_format("2022-10-01","%y-%m-%d"),"1","01","01"),
("01-02","FERNANDO","CARDOZO SANTA","CL 17 26A-18","7403719",date_format("1976-03-21","%y-%m-%d"),date_format("2021-01-15","%y-%m-%d"),"1","02","01"),
("01-03","GLORIA","PATINO GARCIA","CL 15 20-24","7455890",date_format("1970-12-24","%y-%m-%d"),date_format("2006-06-30","%y-%m-%d"),"1","03","01"),
("03-01","ERSAIN","CASTANO LOPEZ","CL 8 23E-105","7466603",date_format("1981-02-19","%y-%m-%d"),date_format("2018-01-01","%y-%m-%d"),"1","01","03"),
("03-02","MAURICIO","CRUZ PINO","CRA 17 20-32","7485180",date_format("1985-04-13","%y-%m-%d"),date_format("2018-01-01","%y-%m-%d"),"1","01","03"),
("03-03","MONICA TATIANA","GARAVITO","CRA 18 10-32","7385580",date_format("1988-04-13","%y-%m-%d"),date_format("2007-06-01","%y-%m-%d"),"1","01","03");


update sucursal set gerente="01-01" where codigo="01";
update sucursal set gerente="01-02" where codigo="02";
update sucursal set gerente="01-03" where codigo="03";

delete from factura;
INSERT INTO FACTURA VALUES
(1,DATE_FORMAT("2018-02-01","%y-%m-%d"),"33819984","03-01","01","1"),
(2,DATE_FORMAT("2018-02-01","%y-%m-%d"),"18396606","03-01","01","1"),
(3,DATE_FORMAT("2018-02-01","%y-%m-%d"),"18396606","03-01","01","1"),
(4,DATE_FORMAT("2018-02-02","%y-%m-%d"),"4377130","03-02","01","1"),
(5,DATE_FORMAT("2018-02-02","%y-%m-%d"),"18400000","03-01","01","2"),
(6,DATE_FORMAT("2018-02-02","%y-%m-%d"),"7777777777","03-01","01","1"),
(7,DATE_FORMAT("2018-02-02","%y-%m-%d"),"7777777777","03-02","01","1"),
(8,DATE_FORMAT("2018-02-02","%y-%m-%d"),"4377130","03-01","01","1"),
(9,DATE_FORMAT("2018-02-03","%y-%m-%d"),"92227452","03-01","01","1"),
(10,DATE_FORMAT("2018-02-03","%y-%m-%d"),"75080501","03-01","01","1"),
(11,DATE_FORMAT("2018-02-03","%y-%m-%d"),"4377130","03-01","01","1"),
(12,DATE_FORMAT("2018-02-03","%y-%m-%d"),"41375231","03-02","01","1"),
(13,DATE_FORMAT("2018-02-03","%y-%m-%d"),"41375231","03-02","01","1"),
(14,DATE_FORMAT("2018-02-03","%y-%m-%d"),"18400000","03-02","01","2"),
(15,DATE_FORMAT("2018-02-04","%y-%m-%d"),"75080501","03-02","01","1"),
(16,DATE_FORMAT("2018-02-04","%y-%m-%d"),"33872000","03-01","01","1"),
(17,DATE_FORMAT("2018-02-04","%y-%m-%d"),"18396606","03-01","01","1"),
(18,DATE_FORMAT("2018-02-04","%y-%m-%d"),"41375231","03-01","01","2"),
(19,DATE_FORMAT("2018-02-05","%y-%m-%d"),"92227452","03-01","01","1"),
(20,DATE_FORMAT("2018-02-04","%y-%m-%d"),"18400000","03-01","01","1");

delete from detallefactura;
insert into detallefactura values
(1,"AC010",1),(1,"AD011",2),(1,"AC011",1),
(2,"OT023",2),
(3,"AD011",1),(3,"AD012",2),(3,"AD013",1),(3,"AC007",1),
(4,"AD014",1),(4,"AD015",1),(4,"AD016",2),
(5,"AC008",1),(5,"AC009",1),(5,"AC010",1),
(6,"OT024",2),(6,"OT023",2),(6,"AC008",1),(6,"AC009",1),(6,"AC002",1),
(7,"AD015",1),(7,"AD016",2),
(8,"AC001",1),(8,"AC002",1),(8,"AD015",1),(8,"AD016",1),
(9,"AD020",1),(9,"AD021",5),(9,"OT023",4),(9,"AC011",6),
(10,"AC006",1),(10,"AC008",1),(10,"AD011",1),(10,"AD016",3);

insert into detallefactura values
(11,"AC010",1),(11,"AD011",2),(11,"AC011",1),
(12,"OT023",2),
(13,"AD011",1),(13,"AD012",2),(13,"AD013",1),(13,"AC007",1),
(14,"AD014",1),(14,"AD015",1),(14,"AD016",2),
(15,"AC008",1),(15,"AC009",1),(15,"AC010",1),
(16,"OT024",2),(16,"OT023",2),(16,"AC008",1),(16,"AC009",1),(16,"AC002",1),
(17,"AD015",1),(17,"AD016",2),
(18,"AC001",1),(18,"AC002",1),(18,"AD015",1),(18,"AD016",1),
(19,"AD020",1),(19,"AD021",3),(19,"OT023",4),(19,"AC011",3),
(20,"AC006",1),(20,"AC008",1),(20,"AD011",1),(20,"AD016",1);

alter table empleados add foreign key(cargo) references cargo(codigo);
alter table productos add foreign key(proveedor) references proveedores(nit);

