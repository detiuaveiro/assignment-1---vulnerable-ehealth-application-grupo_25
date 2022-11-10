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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Paciente` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Num_Utente` char(9) NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `Paciente_Utilizador_null_fk` FOREIGN KEY (`ID`) REFERENCES `Utilizador` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Especialidade` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Médico` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Num_Medico` char(4) NOT NULL,
  `Cod_Esp` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Médico_Especialidade_null_fk` (`Cod_Esp`),
  CONSTRAINT `Médico_Especialidade_null_fk` FOREIGN KEY (`Cod_Esp`) REFERENCES `Especialidade` (`Codigo`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `Médico_Utilizador_null_fk` FOREIGN KEY (`ID`) REFERENCES `Utilizador` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Med_Pac` (
  `ID_Pac` int NOT NULL,
  `ID_Med` int NOT NULL,
  PRIMARY KEY (`ID_Med`,`ID_Pac`),
  KEY `Med_Pac_Paciente_null_fk` (`ID_Pac`),
  CONSTRAINT `Med_Pac_Médico_null_fk` FOREIGN KEY (`ID_Med`) REFERENCES `Medico` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Med_Pac_Paciente_null_fk` FOREIGN KEY (`ID_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



CREATE TABLE `Medicamento` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  PRIMARY KEY (`Codigo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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


CREATE TABLE `Doenca` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Nome` varchar(100) NOT NULL,
  `Cod_Esp` int NOT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Doenca_Especialidade_null_fk` (`Cod_Esp`),
  CONSTRAINT `Doenca_Especialidade_null_fk` FOREIGN KEY (`Cod_Esp`) REFERENCES `Especialidade` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Diagnostico` (
  `Cod_Doenca` int NOT NULL,
  `Id_Pac` int NOT NULL,
  PRIMARY KEY (`Cod_Doenca`,`Id_Pac`),
  CONSTRAINT `Diagnostico_Doenca_null_fk` FOREIGN KEY (`Cod_Doenca`) REFERENCES `Doenca` (`Codigo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Diagnostico_Paciente_null_fk` FOREIGN KEY (`Cod_Doenca`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `Analise` (
  `Codigo` int NOT NULL AUTO_INCREMENT,
  `Id_Pac` int NOT NULL,
  `Data_Emi` date NOT NULL,
  `Data_Val` date DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Analise_Paciente_null_fk` (`Id_Pac`),
  CONSTRAINT `Analise_Paciente_null_fk` FOREIGN KEY (`Id_Pac`) REFERENCES `Paciente` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;