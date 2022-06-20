Drop table if exists clientes;

Create table clientes(
    id_cliente       integer primary key autoincrement,
    nombre           varchar(50) not null,
    email            varchar(50) not null,
    numero_telefono  varchar(20) not null
);


insert into clientes(nombre,email,numero) values ("Luis","luis@icloud.com",      "7758889999");
insert into clientes(nombre,email,numero) values ("Gustabo","gustabo@icloud.com","7767777888");
insert into clientes(nombre,email,numero) values ("Kevin","kevin@icloud.com",    "7759966655");


Select * From clientes;
