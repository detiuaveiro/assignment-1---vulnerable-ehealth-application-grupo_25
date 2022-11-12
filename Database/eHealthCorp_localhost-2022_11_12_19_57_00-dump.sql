-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: eHealthCorp
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Analise`
--

DROP TABLE IF EXISTS `Analise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Analise` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Id_Pac` int NOT NULL,
  `Data_Emi` date NOT NULL,
  `Data_Val` date DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Analise_Paciente_null_fk` (`Id_Pac`),
  CONSTRAINT `Analise_Paciente_null_fk` FOREIGN KEY (`Id_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Analise`
--

LOCK TABLES `Analise` WRITE;
/*!40000 ALTER TABLE `Analise` DISABLE KEYS */;
/*!40000 ALTER TABLE `Analise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Consulta`
--

DROP TABLE IF EXISTS `Consulta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Consulta` (
  `Num_Cons` int NOT NULL AUTO_INCREMENT,
  `ID_Med` int NOT NULL,
  `ID_Pac` int NOT NULL,
  `Cod_Esp` int NOT NULL,
  `Data` datetime NOT NULL,
  PRIMARY KEY (`Num_Cons`,`ID_Med`),
  KEY `Consulta_Especialidade_null_fk` (`Cod_Esp`),
  KEY `Consulta_Médico_null_fk` (`ID_Med`),
  KEY `Consulta_Paciente_null_fk` (`ID_Pac`),
  CONSTRAINT `Consulta_Especialidade_null_fk` FOREIGN KEY (`Cod_Esp`) REFERENCES `Especialidade` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Consulta_Médico_null_fk` FOREIGN KEY (`ID_Med`) REFERENCES `Medico` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Consulta_Paciente_null_fk` FOREIGN KEY (`ID_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consulta`
--

LOCK TABLES `Consulta` WRITE;
/*!40000 ALTER TABLE `Consulta` DISABLE KEYS */;
INSERT INTO `Consulta` VALUES (1,2,1,1,'2022-11-15 00:00:00');
/*!40000 ALTER TABLE `Consulta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Diagnostico`
--

DROP TABLE IF EXISTS `Diagnostico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Diagnostico` (
  `Cod_Doenca` int NOT NULL,
  `Id_Pac` int NOT NULL,
  PRIMARY KEY (`Cod_Doenca`,`Id_Pac`),
  KEY `Diagnostico_Paciente_null_fk` (`Id_Pac`),
  CONSTRAINT `Diagnostico_Doenca_null_fk` FOREIGN KEY (`Cod_Doenca`) REFERENCES `Doenca` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Diagnostico_Paciente_null_fk` FOREIGN KEY (`Id_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Diagnostico`
--

LOCK TABLES `Diagnostico` WRITE;
/*!40000 ALTER TABLE `Diagnostico` DISABLE KEYS */;
INSERT INTO `Diagnostico` VALUES (5,1);
/*!40000 ALTER TABLE `Diagnostico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doenca`
--

DROP TABLE IF EXISTS `Doenca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Doenca` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  `Cod_Esp` int NOT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Doenca_Especialidade_null_fk` (`Cod_Esp`),
  CONSTRAINT `Doenca_Especialidade_null_fk` FOREIGN KEY (`Cod_Esp`) REFERENCES `Especialidade` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doenca`
--

LOCK TABLES `Doenca` WRITE;
/*!40000 ALTER TABLE `Doenca` DISABLE KEYS */;
INSERT INTO `Doenca` VALUES (1,'Arrhythmia',2),(2,'High Blood Pressure',2),(3,'Acne',3),(4,'Vitiligo',3),(5,'Common Cold',1),(6,'Asthma',1);
/*!40000 ALTER TABLE `Doenca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Especialidade`
--

DROP TABLE IF EXISTS `Especialidade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Especialidade` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Especialidade`
--

LOCK TABLES `Especialidade` WRITE;
/*!40000 ALTER TABLE `Especialidade` DISABLE KEYS */;
INSERT INTO `Especialidade` VALUES (1,'Medicina Interna'),(2,'Cardiologia'),(3,'Dermatologia'),(4,'Medicina Dentária'),(5,'Ortopedia');
/*!40000 ALTER TABLE `Especialidade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Med_Pac`
--

DROP TABLE IF EXISTS `Med_Pac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Med_Pac` (
  `ID_Pac` int NOT NULL,
  `ID_Med` int NOT NULL,
  PRIMARY KEY (`ID_Med`,`ID_Pac`),
  KEY `Med_Pac_Paciente_null_fk` (`ID_Pac`),
  CONSTRAINT `Med_Pac_Médico_null_fk` FOREIGN KEY (`ID_Med`) REFERENCES `Medico` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Med_Pac_Paciente_null_fk` FOREIGN KEY (`ID_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Med_Pac`
--

LOCK TABLES `Med_Pac` WRITE;
/*!40000 ALTER TABLE `Med_Pac` DISABLE KEYS */;
INSERT INTO `Med_Pac` VALUES (1,2);
/*!40000 ALTER TABLE `Med_Pac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medicamento`
--

DROP TABLE IF EXISTS `Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medicamento` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicamento`
--

LOCK TABLES `Medicamento` WRITE;
/*!40000 ALTER TABLE `Medicamento` DISABLE KEYS */;
INSERT INTO `Medicamento` VALUES (1,'Bromax'),(2,'Clarinex'),(3,'Accuretic'),(4,'Retin-A'),(5,'Accutane'),(6,'Diprivan');
/*!40000 ALTER TABLE `Medicamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medico`
--

DROP TABLE IF EXISTS `Medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medico` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Num_Medico` char(4) NOT NULL,
  `Cod_Esp` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Médico_Especialidade_null_fk` (`Cod_Esp`),
  CONSTRAINT `Médico_Especialidade_null_fk` FOREIGN KEY (`Cod_Esp`) REFERENCES `Especialidade` (`Codigo`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `Médico_Utilizador_null_fk` FOREIGN KEY (`ID`) REFERENCES `Utilizador` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medico`
--

LOCK TABLES `Medico` WRITE;
/*!40000 ALTER TABLE `Medico` DISABLE KEYS */;
INSERT INTO `Medico` VALUES (2,'0001',1);
/*!40000 ALTER TABLE `Medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Paciente` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Num_Utente` char(9) NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Paciente_Utilizador_null_fk` FOREIGN KEY (`ID`) REFERENCES `Utilizador` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
INSERT INTO `Paciente` VALUES (1,'273134778'),(3,'240496930');
/*!40000 ALTER TABLE `Paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescricao`
--

DROP TABLE IF EXISTS `Prescricao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prescricao` (
  `Cod_Medic` int NOT NULL,
  `Num_Consulta` int NOT NULL,
  `Id_Med` int NOT NULL,
  PRIMARY KEY (`Id_Med`,`Num_Consulta`,`Cod_Medic`),
  KEY `Prescricao_Consulta_null_fk` (`Num_Consulta`),
  KEY `Prescricao_Medicamento_null_fk` (`Cod_Medic`),
  CONSTRAINT `Prescricao_Consulta_null_fk` FOREIGN KEY (`Num_Consulta`) REFERENCES `Consulta` (`Num_Cons`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Prescricao_Medicamento_null_fk` FOREIGN KEY (`Cod_Medic`) REFERENCES `Medicamento` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Prescricao_Médico_null_fk` FOREIGN KEY (`Id_Med`) REFERENCES `Medico` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescricao`
--

LOCK TABLES `Prescricao` WRITE;
/*!40000 ALTER TABLE `Prescricao` DISABLE KEYS */;
/*!40000 ALTER TABLE `Prescricao` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Teste`
--

DROP TABLE IF EXISTS `Teste`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Teste` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Cod_Anal` int NOT NULL,
  `Procedimento` varchar(100) NOT NULL,
  `Valor_Min` float NOT NULL,
  `Valor_Max` float NOT NULL,
  `Unidades` varchar(10) NOT NULL,
  `Resultado` float NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Teste_Analise_null_fk` (`Cod_Anal`),
  CONSTRAINT `Teste_Analise_null_fk` FOREIGN KEY (`Cod_Anal`) REFERENCES `Analise` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teste`
--

LOCK TABLES `Teste` WRITE;
/*!40000 ALTER TABLE `Teste` DISABLE KEYS */;
/*!40000 ALTER TABLE `Teste` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Utilizador`
--

DROP TABLE IF EXISTS `Utilizador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Utilizador` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Tel` char(9) DEFAULT NULL,
  `Password` varchar(100) NOT NULL,
  `Idade` int DEFAULT NULL,
  `Morada` varchar(100) DEFAULT NULL,
  `NIF` char(9) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Utilizador`
--

LOCK TABLES `Utilizador` WRITE;
/*!40000 ALTER TABLE `Utilizador` DISABLE KEYS */;
INSERT INTO `Utilizador` VALUES (1,'Artur Correia','art.afo@ua.pt','930577403','1904',20,'Quinta do Bosque, Lote 110, 2ºEsq','262190185'),(2,'Ana Filipa Gomes','afgomes@mail.pt',NULL,'1234',NULL,NULL,'112773456'),(3,'Daniel Carvalho','dl.carvalho@ua.pt','962368016','0000',25,'Sever do Vouga','222222222');
/*!40000 ALTER TABLE `Utilizador` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-12 19:57:00
