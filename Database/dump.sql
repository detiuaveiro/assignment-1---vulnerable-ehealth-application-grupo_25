-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: eHealthCorp
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
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
  `Codigo` char(5) NOT NULL,
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
INSERT INTO `Analise` VALUES ('HGK10',1,'2022-11-15','2022-11-22');
/*!40000 ALTER TABLE `Analise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Comentario`
--

DROP TABLE IF EXISTS `Comentario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Comentario` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Autor` varchar(100) NOT NULL,
  `Texto` varchar(500) NOT NULL,
  `Data` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Comentario`
--

LOCK TABLES `Comentario` WRITE;
/*!40000 ALTER TABLE `Comentario` DISABLE KEYS */;
INSERT INTO `Comentario` VALUES (1,'Andreia Soares','Gostei muito do meu contacto com os profissionais desta plataforma! Tenho que destacar em particular a Dra. Ana Filipa Gomes, que percebe muito do produto.','2022-11-14 22:32:04'),(2,'Artur ','A plataforma é muito intuitiva e fácil de usar. No entanto, não estou muito contente com a Dra. Ana Filipa Gomes, uma vez que esta me marcou uma consulta há meia-noite. É inadmissivel!','2022-11-14 22:41:31');
/*!40000 ALTER TABLE `Comentario` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consulta`
--

LOCK TABLES `Consulta` WRITE;
/*!40000 ALTER TABLE `Consulta` DISABLE KEYS */;
INSERT INTO `Consulta` VALUES (1,2,1,1,'2022-11-15 00:00:00'),(2,2,1,1,'2022-11-10 10:00:00'),(3,2,4,1,'2022-11-15 12:00:00'),(4,5,1,5,'2022-11-25 16:30:00');
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
INSERT INTO `Med_Pac` VALUES (1,2),(4,2);
/*!40000 ALTER TABLE `Med_Pac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `Med_User_View`
--

DROP TABLE IF EXISTS `Med_User_View`;
/*!50001 DROP VIEW IF EXISTS `Med_User_View`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Med_User_View` AS SELECT 
 1 AS `ID`,
 1 AS `Nome`,
 1 AS `Email`,
 1 AS `Tel`,
 1 AS `Password`,
 1 AS `Idade`,
 1 AS `Morada`,
 1 AS `NIF`,
 1 AS `Num_Medico`,
 1 AS `Cod_Esp`*/;
SET character_set_client = @saved_cs_client;

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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medico`
--

LOCK TABLES `Medico` WRITE;
/*!40000 ALTER TABLE `Medico` DISABLE KEYS */;
INSERT INTO `Medico` VALUES (2,'0001',1),(5,'0002',5);
/*!40000 ALTER TABLE `Medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `Pac_User_View`
--

DROP TABLE IF EXISTS `Pac_User_View`;
/*!50001 DROP VIEW IF EXISTS `Pac_User_View`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `Pac_User_View` AS SELECT 
 1 AS `ID`,
 1 AS `Nome`,
 1 AS `Email`,
 1 AS `Tel`,
 1 AS `Password`,
 1 AS `Idade`,
 1 AS `Morada`,
 1 AS `NIF`,
 1 AS `Num_Utente`*/;
SET character_set_client = @saved_cs_client;

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
INSERT INTO `Paciente` VALUES (1,'273134778'),(3,'240496930'),(4,'444883959');
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
  `Code` char(5) NOT NULL,
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
INSERT INTO `Prescricao` VALUES (1,1,2,'AXF03'),(2,1,2,'AXF03'),(3,1,2,'AXF05'),(6,3,2,'0QAT8');
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
  `Cod_Anal` char(5) NOT NULL,
  `Procedimento` varchar(100) NOT NULL,
  `Valor_Min` float NOT NULL,
  `Valor_Max` float NOT NULL,
  `Unidades` varchar(10) NOT NULL,
  `Resultado` float NOT NULL,
  PRIMARY KEY (`Id`),
  KEY `Teste_Analise_null_fk` (`Cod_Anal`),
  CONSTRAINT `Teste_Analise_null_fk` FOREIGN KEY (`Cod_Anal`) REFERENCES `Analise` (`Codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Teste`
--

LOCK TABLES `Teste` WRITE;
/*!40000 ALTER TABLE `Teste` DISABLE KEYS */;
INSERT INTO `Teste` VALUES (2,'HGK10','TSH w/reflex to T4 Free',0.45,4.5,'mIU/L',4.3512),(3,'HGK10','T3 Total',1.155,3.388,'mmol/L',3.4734),(4,'HGK10','T4 Total',0.069,0.185,'mmol/L',0.30157),(5,'HGK10','WBC',4,10,'10e9/L',86.216),(6,'HGK10','Hemoglobin',13.7,17.5,'g/dL',645.8);
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Utilizador`
--

LOCK TABLES `Utilizador` WRITE;
/*!40000 ALTER TABLE `Utilizador` DISABLE KEYS */;
INSERT INTO `Utilizador` VALUES (1,'Artur Correia','art.afo@ua.pt','930577403','1904',20,'Quinta do Bosque, Lote 110, 2ºEsq','262190185'),(2,'Ana Filipa Gomes','afgomes@mail.pt',NULL,'1234',NULL,NULL,'112773456'),(3,'Daniel Carvalho','dl.carvalho@ua.pt','962368016','0000',25,'Sever do Vouga','222222222'),(4,'Andreia Soares','andreia@mail.pt','234555039','0000',27,'Porto','294953959'),(5,'Antero Lobo','lobao@mail.pt','934683895','1234',67,'Leiria','847294990');
/*!40000 ALTER TABLE `Utilizador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `Med_User_View`
--

/*!50001 DROP VIEW IF EXISTS `Med_User_View`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `Med_User_View` AS select `U`.`ID` AS `ID`,`U`.`Nome` AS `Nome`,`U`.`Email` AS `Email`,`U`.`Tel` AS `Tel`,`U`.`Password` AS `Password`,`U`.`Idade` AS `Idade`,`U`.`Morada` AS `Morada`,`U`.`NIF` AS `NIF`,`M`.`Num_Medico` AS `Num_Medico`,`M`.`Cod_Esp` AS `Cod_Esp` from (`Medico` `M` join `Utilizador` `U` on((`M`.`ID` = `U`.`ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `Pac_User_View`
--

/*!50001 DROP VIEW IF EXISTS `Pac_User_View`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`%` SQL SECURITY DEFINER */
/*!50001 VIEW `Pac_User_View` AS select `U`.`ID` AS `ID`,`U`.`Nome` AS `Nome`,`U`.`Email` AS `Email`,`U`.`Tel` AS `Tel`,`U`.`Password` AS `Password`,`U`.`Idade` AS `Idade`,`U`.`Morada` AS `Morada`,`U`.`NIF` AS `NIF`,`P`.`Num_Utente` AS `Num_Utente` from (`Paciente` `P` join `Utilizador` `U` on((`P`.`ID` = `U`.`ID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-15  0:48:14
