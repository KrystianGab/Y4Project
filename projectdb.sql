USE projectdb;


drop TABLE if exists result
;
drop TABLE if exists army1
;
drop TABLE if exists army2
;


create table result (
	resultID int AUTO_INCREMENT,
	p1points VARCHAR (10) NOT NULL,
	p2points VARCHAR (10) NOT NULL,
	constraint pk_match primary key (resultID)
) 
;
create TABLE army1 (
	army1ID int AUTO_INCREMENT,
   resultID int NOT NULL,
	unit1 VARCHAR (50) NOT NULL, 
	unit2 VARCHAR (50),
	unit3 VARCHAR (50),
	unit4 VARCHAR (50),
	unit5 VARCHAR (50),
	unit6 VARCHAR (50),
	unit7 VARCHAR (50),
	unit8 VARCHAR (50),
	unit9 VARCHAR (50),
	unit10 VARCHAR (50),
	unit11 VARCHAR (50),
	unit12 VARCHAR (50),
	unit13 VARCHAR (50),
	unit14 VARCHAR (50),
	unit15 VARCHAR (50),
	unit16 VARCHAR (50),
	unit17 VARCHAR (50),
	unit18 VARCHAR (50),
	unit19 VARCHAR (50),
	unit20 VARCHAR (50),
	unit21 VARCHAR (50),
	unit22 VARCHAR (50),
	unit23 VARCHAR (50),
	unit24 VARCHAR (50),
	unit25 VARCHAR (50),
	constraint fk_army1 foreign key (resultID)
		references result (resultID),
	constraint pk_army1 primary key (army1ID)
) 
;
create table army2 (
	army2ID int AUTO_INCREMENT,
   resultID int NOT NULL,
	unit1 VARCHAR (50) NOT NULL, 
	unit2 VARCHAR (50),
	unit3 VARCHAR (50),
	unit4 VARCHAR (50),
	unit5 VARCHAR (50),
	unit6 VARCHAR (50),
	unit7 VARCHAR (50),
	unit8 VARCHAR (50),
	unit9 VARCHAR (50),
	unit10 VARCHAR (50),
	unit11 VARCHAR (50),
	unit12 VARCHAR (50),
	unit13 VARCHAR (50),
	unit14 VARCHAR (50),
	unit15 VARCHAR (50),
	unit16 VARCHAR (50),
	unit17 VARCHAR (50),
	unit18 VARCHAR (50),
	unit19 VARCHAR (50),
	unit20 VARCHAR (50),
	unit21 VARCHAR (50),
	unit22 VARCHAR (50),
	unit23 VARCHAR (50),
	unit24 VARCHAR (50),
	unit25 VARCHAR (50),
	constraint fk_army2 foreign key (resultID)
		references result (resultID),
	constraint pk_army2 primary key (army2ID)
) 
;