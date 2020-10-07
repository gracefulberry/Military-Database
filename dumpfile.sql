DROP DATABASE IF EXISTS `ASH`;
CREATE SCHEMA `ASH`;
USE `ASH`;

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
  `RecieptNumber` int NOT NULL,
  `Distance` float NOT NULL,
  PRIMARY KEY (`RecieptNumber`)
);

DROP TABLE IF EXISTS `PERSONNEL`;
CREATE TABLE `PERSONNEL` (
  `IDnumber` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Regiment` varchar(255),
  PRIMARY KEY (`IDnumber`)
);

DROP TABLE IF EXISTS `MEDIC`;
CREATE TABLE `MEDIC` (
  `IDnumber` int NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`),
  `Specialization` varchar(255)
);

DROP TABLE IF EXISTS `CIVIL`;
CREATE TABLE `CIVIL` (
  `IDnumber` int NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`),
  `Civil` varchar(255)
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
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);

DROP TABLE IF EXISTS `SIGNAL`;
CREATE TABLE `SIGNAL` (
  `IDnumber` int NOT NULL,
  `Date` Date NOT NULL,
  `Time` Time NOT NULL,
  `Content` varchar(255) NOT NULL,
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);


/*relationships*/


CREATE TABLE `BELONGS_TO` (
  `IDnumber` int,
  `ChassisNo` int NOT NULL,
  `Model` char(4) NOT NULL,
  `MatName` varchar(255),
  `WingName` varchar(255),
  FOREIGN KEY (`ChassisNo`, `Model`) REFERENCES `VEHICLE` (`ChassisNo`, `Model`),
  FOREIGN KEY (`MatName`) REFERENCES `MATERIAL` (`Name`),
  FOREIGN KEY (`WingName`) REFERENCES `WINGS` (`Wings`),
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`IDnumber`, `ChassisNo`, `Model`, `MatName`, `WingName`)
);

CREATE TABLE `MAKES_TRIP` (
  `ChassisNo` int NOT NULL,
  `Model` char(4) NOT NULL,
  `RecieptNumber` int,
  FOREIGN KEY (`ChassisNo`, `Model`) REFERENCES `VEHICLE` (`ChassisNo`, `Model`),
  FOREIGN KEY (`RecieptNumber`) REFERENCES `TRIP` (`RecieptNumber`),
  PRIMARY KEY (`ChassisNo`,`Model`, `RecieptNumber`)
);

CREATE TABLE `Supervision` (
  `SIDnumber` int,
  `IDnumber` int,
  FOREIGN KEY (`SIDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  FOREIGN KEY (`IDnumber`) REFERENCES `PERSONNEL` (`IDnumber`),
  PRIMARY KEY (`SIDnumber`, `IDnumber`)
);

CREATE TABLE `IntelCommunication` (
  `IDnumber` int NOT NULL,
  `Date` Date NOT NULL,
  `Time` Time NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `SOLDIER` (`IDnumber`),
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);

CREATE TABLE `SignalCommunication` (
  `IDnumber` int NOT NULL,
  `Date` Date NOT NULL,
  `Time` Time NOT NULL,
  FOREIGN KEY (`IDnumber`) REFERENCES `TECH` (`IDnumber`),
  PRIMARY KEY (`IDnumber`, `Date`, `Time`)
);
