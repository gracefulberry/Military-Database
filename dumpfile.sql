-- SCHEMA
DROP DATABASE IF EXISTS `ASH`;
CREATE SCHEMA `ASH`;
USE `ASH`;


-- TABLES
DROP TABLE IF EXISTS `MATERIAL`;
CREATE TABLE `MATERIAL` (
  `Name` varchar(255) NOT NULL,
  `Quantity` int NOT NULL,
  `Cost` float NOT NULL,
  PRIMARY KEY (`Name`)
);

DROP TABLE IF EXISTS `WINGS`;
CREATE TABLE `WINGS` (
  `Wings` varchar(255) NOT NULL,
  `Budget` int NOT NULL,
  PRIMARY KEY (`Wings`)
);

DROP TABLE IF EXISTS `VEHICLE`;
CREATE TABLE `VEHICLE` (
  `ChassisNo` int NOT NULL,
  `Model` char(4) NOT NULL,
  `Mileage` float NOT NULL,
  `PassengerCapacity` int,
  PRIMARY KEY (`ChassisNo`, `Model`)
);

DROP TABLE IF EXISTS `PURPOSES`;
CREATE TABLE `PURPOSES` (
  `ChassisNo` int NOT NULL,
  `Model` char(4) NOT NULL,
  `Purpose` varchar(255) NOT NULL,
  FOREIGN KEY (`ChassisNo`, `Model`) REFERENCES `VEHICLE` (`ChassisNo`, `Model`),
  PRIMARY KEY (`ChassisNo`,`Model`,`Purpose`)
);

DROP TABLE IF EXISTS `TRIP`;
CREATE TABLE `TRIP` (
  `RecieptNumber` int NOT NULL AUTO_INCREMENT,
  `Distance` float NOT NULL,
  `ChassisNo` int NOT NULL,
  `Model` char(4) NOT NULL,
  FOREIGN KEY (`ChassisNo`, `Model`) REFERENCES `VEHICLE` (`ChassisNo`, `Model`),
  PRIMARY KEY (`RecieptNumber`)
);

DROP TABLE IF EXISTS `PERSONNEL`;
CREATE TABLE `PERSONNEL` (
  `IDnumber` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Regiment` varchar(255),
  `Rnk` int NOT NULL,
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `MEDIC`;
CREATE TABLE `MEDIC` (
  `IDnumber` int NOT NULL,
  `Specialization` varchar(255),
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `CIVIL`;
CREATE TABLE `CIVIL` (
  `IDnumber` int NOT NULL,
  `Civil` varchar(255),
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `SOLDIER`;
CREATE TABLE `SOLDIER` (
  `IDnumber` int NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `TECH`;
CREATE TABLE `TECH` (
  `IDnumber` int NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `INTEL`;
CREATE TABLE `INTEL` (
  `IDnumber` int NOT NULL,
  `Date` Date NOT NULL,
  `Time` Time NOT NULL,
  `Content` varchar(255) NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `SOLDIER` (`IDnumber`),
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);

DROP TABLE IF EXISTS `SIG`;
CREATE TABLE `SIG` (
  `IDnumber` int NOT NULL,
  `Date` Date NOT NULL,
  `Time` Time NOT NULL,
  `Content` varchar(255) NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `TECH` (`IDnumber`),
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);


-- relationships
DROP TABLE IF EXISTS `BELONGS_TO`;
CREATE TABLE `BELONGS_TO` (
  `IDnumber` int,
  `ChassisNo` int,
  `Model` char(4),
  `MatName` varchar(255),
  `WingName` varchar(255) NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  FOREIGN KEY (`ChassisNo`, `Model`) REFERENCES `VEHICLE` (`ChassisNo`, `Model`),
  FOREIGN KEY (`MatName`) REFERENCES `MATERIAL` (`Name`),
  FOREIGN KEY (`WingName`) REFERENCES `WINGS` (`Wings`),
  PRIMARY KEY (`IDnumber`, `ChassisNo`, `Model`, `MatName`, `WingName`)
);

DROP TABLE IF EXISTS `SUPERVISION`;
CREATE TABLE `SUPERVISION` (
  `SIDnumber` int,
  `IDnumber` int,
  FOREIGN KEY (`SIDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`SIDnumber`, `IDnumber`)
);


-- Insert

-- WINGS
INSERT INTO WINGS (Wings, Budget)
VALUES ('Ground', 200000);

INSERT INTO WINGS (Wings, Budget)
VALUES ('Air', 800000);

INSERT INTO WINGS (Wings, Budget)
VALUES ('Marine', 600000);


-- MATERIAL
INSERT INTO MATERIAL (Name, Quantity, Cost)
VALUES ('FlameThrower', 17, 15000);

INSERT INTO MATERIAL (Name, Quantity, Cost)
VALUES ('Missiles', 78, 35000);

INSERT INTO MATERIAL (Name, Quantity, Cost)
VALUES ('Bazooka', 23, 20000);

INSERT INTO MATERIAL (Name, Quantity, Cost)
VALUES ('LandMines', 56, 5000);


-- VEHICLE
INSERT INTO VEHICLE (ChassisNo, Model, Mileage, PassengerCapacity)
VALUES (9899, 'MX55', 12, 6);

INSERT INTO VEHICLE (ChassisNo, Model, Mileage, PassengerCapacity)
VALUES (6723, 'FL12', 6, 18);

INSERT INTO VEHICLE (ChassisNo, Model, Mileage, PassengerCapacity)
VALUES (7522, 'BK98', 2, 35);

INSERT INTO VEHICLE (ChassisNo, Model, Mileage, PassengerCapacity)
VALUES (5546, 'OT45', 1, 65);


-- TRIP
INSERT INTO TRIP (RecieptNumber, Distance, ChassisNo, Model)
VALUES (1, 100, 5546, 'OT45');

INSERT INTO TRIP (RecieptNumber, Distance, ChassisNo, Model)
VALUES (1, 70, 9899, 'MX55');

INSERT INTO TRIP (RecieptNumber, Distance, ChassisNo, Model)
VALUES (1, 125, 7522, 'BK98');

-- PURPOSES
INSERT INTO PURPOSES (ChassisNo, Model, Purpose)
VALUES (9899, 'MX55', 'MultiTerrain');

INSERT INTO PURPOSES (ChassisNo, Model, Purpose)
VALUES (6723, 'FL12', 'FamLuggage');

INSERT INTO PURPOSES (ChassisNo, Model, Purpose)
VALUES (7522, 'BK98', 'Biking');

INSERT INTO PURPOSES (ChassisNo, Model, Purpose)
VALUES (5546, 'OT45', 'OffRoader');


-- PERSONNEL
INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Jack Reaper', 'Alpha', 5);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('John Legend', 'Delta', 7);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Mary Gold', 'Zulu', 9);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Harry Potter', 'Delta', 5);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Percy Jackson', 'Zulu', 5);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Rock Johnson', 'Alpha', 3);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Mr.Robot', 'Alpha', 7);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Micky Mouse', 'Zulu', 7);

INSERT INTO PERSONNEL (Name, Regiment, Rnk)
VALUES ('Flint Cameron', 'Delta', 5);


-- MEDIC
INSERT INTO MEDIC (IDnumber)
VALUES (2);

INSERT INTO MEDIC (IDnumber)
VALUES (3);


-- CIVIL
INSERT INTO CIVIL (IDnumber)
VALUES (8);

INSERT INTO CIVIL (IDnumber)
VALUES (9);


-- SOLDIER
INSERT INTO SOLDIER (IDnumber)
VALUES (4);

INSERT INTO SOLDIER (IDnumber)
VALUES (5);

INSERT INTO SOLDIER (IDnumber)
VALUES (6);


-- TECH
INSERT INTO TECH (IDnumber)
VALUES (1);

INSERT INTO TECH (IDnumber)
VALUES (7);


-- INTEL
INSERT INTO INTEL (IDnumber, Date, Time, Content)
VALUES (4, '2020-01-01', '00:00', 'Happy new year!');

INSERT INTO INTEL (IDnumber, Date, Time, Content)
VALUES (5, '2020-03-20', '00:00', 'Home! Here we come.');

INSERT INTO INTEL (IDnumber, Date, Time, Content)
VALUES (6, '2020-08-10', '00:00', 'Take me back :(');


-- SIGNAL
INSERT INTO SIG (IDnumber, Date, Time, Content)
VALUES (1, '2020-03-15', '00:00', 'Life is going great!');

INSERT INTO SIG (IDnumber, Date, Time, Content)
VALUES (7, '2020-05-23', '00:00', 'Home is fun but I miss hanging out with friends');


-- SUPERVISION
INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (1, 7);

INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (6, 4);

INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (6, 5);

INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (9, 8);

INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (2, 3);

INSERT INTO SUPERVISION (SIDnumber, IDnumber)
VALUES (5, 4);

-- BELONGS_TO
INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (1, 9899, 'MX55', 'FlameThrower', 'Marine');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (9, 9899, 'MX55', 'FlameThrower', 'Marine');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (4, 9899, 'MX55', 'Bazooka', 'Marine');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (2, 7522, 'BK98', 'Bazooka', 'Ground');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (8, 7522, 'BK98', 'Bazooka', 'Ground');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (5, 5546, 'OT45', 'LandMines', 'Ground');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (6, 5546, 'OT45', 'LandMines', 'Ground');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (7, 6723, 'FL12', 'FlameThrower', 'Air');

INSERT INTO BELONGS_TO (IDnumber, ChassisNo, Model, MatName, WingName)
VALUES (3, 6723, 'FL12', 'FlameThrower', 'Air');


