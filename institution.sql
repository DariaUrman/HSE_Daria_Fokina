-- MySQL dump 10.13  Distrib 8.1.0, for macos13 (arm64)
--
-- Host: localhost    Database: institution
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(100) NOT NULL,
  `head_department_fio` varchar(100) NOT NULL,
  `department_room_n` int NOT NULL,
  `faculty_id` int DEFAULT NULL,
  `department_phone` varchar(20) NOT NULL,
  `department_email` varchar(30) NOT NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE KEY `depp_index` (`department_phone`),
  UNIQUE KEY `depe_index` (`department_email`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `department_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Civil law','Denis Denisovich Denisov',103,1,'+74444444444','civil_law@institution.ru'),(2,'Constitutional and administrative law','Georgy Georgievich Georgiev',104,1,'+75555555555','con_adm_law@institution.ru'),(3,'Criminal law','Evgeny Evgenievich Evgeniev',105,1,'+76666666666','criminal_law@institution.ru'),(4,'Higher mathematics','Fedor Fedorivich Fedorov',457,2,'+78888888888','higher_maths@institution.ru'),(5,'Information technologies','Nikolay Nikolayevich Nikolaev',458,2,'+79999999999','info_tech@institution.ru'),(6,'Computational and experimental mechanics','Nadezhda Nikolaevna Nadezhdova',459,2,'+71010101010','ce_mechs@institution.ru'),(7,'Entrepreneurship and economic security','Anna Antonovna Antonova',790,3,'+71111111111','enecsec@institution.ru'),(8,'Accounting, audit and economic analysis','Olesya Olegovna Olegova',791,3,'+71212121212','aa_ecan@institution.ru'),(9,'Management, marketing and commerce','Aleksey Alekseevich Alekseev',792,3,'+71313131313','mm_com@institution.ru');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation_statement`
--

DROP TABLE IF EXISTS `evaluation_statement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evaluation_statement` (
  `evaluation_statement_id` int NOT NULL AUTO_INCREMENT,
  `mark` int NOT NULL,
  `sheet_id` int DEFAULT NULL,
  `student_id` int DEFAULT NULL,
  PRIMARY KEY (`evaluation_statement_id`),
  KEY `evaluation_statement_ibfk_1` (`sheet_id`),
  KEY `evaluation_statement_ibfk_2` (`student_id`),
  CONSTRAINT `evaluation_statement_ibfk_1` FOREIGN KEY (`sheet_id`) REFERENCES `sheet` (`sheet_id`) ON DELETE CASCADE,
  CONSTRAINT `evaluation_statement_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`) ON DELETE CASCADE,
  CONSTRAINT `evaluation_statement_chk_1` CHECK ((`mark` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation_statement`
--

LOCK TABLES `evaluation_statement` WRITE;
/*!40000 ALTER TABLE `evaluation_statement` DISABLE KEYS */;
INSERT INTO `evaluation_statement` VALUES (1,2,1,1),(2,3,2,1),(3,4,3,1),(4,5,1,2),(5,2,2,2),(6,3,3,2),(7,4,4,3),(8,5,5,3),(10,2,4,4),(11,3,5,4),(13,3,7,5),(14,4,8,5),(15,5,9,5),(16,5,7,6),(17,4,8,6),(18,3,9,6),(19,4,10,7),(20,3,11,7),(21,2,12,7),(22,5,10,8),(23,4,11,8),(24,3,12,8),(25,2,13,9),(26,3,14,9),(27,4,15,9),(28,5,13,10),(29,4,14,10),(30,3,15,10),(31,2,16,11),(32,3,17,11),(33,4,18,11),(34,4,16,12),(35,4,17,12),(36,4,18,12),(37,5,19,13),(38,5,20,13),(39,5,21,13),(40,3,19,14),(41,3,20,14),(42,3,21,14),(43,2,22,15),(44,2,23,15),(45,2,24,15),(46,4,22,16),(47,4,23,16),(48,4,24,16),(49,3,25,17),(50,4,26,17),(51,5,27,17),(52,4,25,18),(53,5,26,18),(54,3,27,18),(55,2,1,19),(56,3,2,19),(57,4,3,19),(58,5,1,20),(59,4,2,20),(60,4,3,20),(61,3,4,21),(62,3,5,21),(64,5,4,22),(65,4,5,22),(67,3,7,23),(68,3,8,23),(69,3,9,23),(70,4,7,24),(71,4,8,24),(72,4,9,24),(73,5,10,25),(74,5,11,25),(75,5,12,25),(76,2,10,26),(77,2,11,26),(78,2,12,26),(79,3,13,27),(80,3,14,27),(81,3,15,27),(82,4,13,28),(83,4,14,28),(84,4,15,28),(85,5,16,29),(86,5,17,29),(87,5,18,29),(88,2,16,30),(89,3,17,30),(90,4,18,30),(91,5,19,31),(92,4,20,31),(93,3,21,31),(94,4,19,32),(95,5,20,32),(96,4,21,32),(97,3,22,33),(98,2,23,33),(99,3,24,33),(100,4,22,34),(101,5,23,34),(102,4,24,34),(103,3,25,35),(104,3,26,35),(105,3,27,35),(106,4,25,36),(107,4,26,36),(108,4,27,36),(109,5,7,37),(110,4,8,37);
/*!40000 ALTER TABLE `evaluation_statement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `faculty_id` int NOT NULL AUTO_INCREMENT,
  `faculty_name` varchar(100) NOT NULL,
  `dean_fio` varchar(100) NOT NULL,
  `dean_room_n` int NOT NULL,
  `dean_phone` varchar(20) NOT NULL,
  `dean_email` varchar(30) NOT NULL,
  PRIMARY KEY (`faculty_id`),
  UNIQUE KEY `dp_index` (`dean_phone`),
  UNIQUE KEY `de_index` (`dean_email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES (1,'Law','Alexander Alexandrovich Aleksandrov',123,'+71111111111','aaa@institution.ru'),(2,'Mechanics and Mathematics','Boris Borisovich Borisov',456,'+72222222222','bbb@institution.ru'),(3,'Economics','Vladislav Vladislavovich Vladislavov',789,'+73333333333','vvv@institution.ru');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `professor_id` int NOT NULL AUTO_INCREMENT,
  `professor_fio` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `experience` varchar(100) NOT NULL,
  `professor_date_of_birth` date NOT NULL,
  `professor_address` varchar(100) NOT NULL,
  `professor_phone` varchar(20) NOT NULL,
  `professor_email` varchar(30) NOT NULL,
  `department_id` int DEFAULT NULL,
  PRIMARY KEY (`professor_id`),
  UNIQUE KEY `pp_index` (`professor_phone`),
  UNIQUE KEY `pe_index` (`professor_email`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `professor_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES (1,'Varvara Dmitrievna Dmitrieva','senior lecturer','none','15 years','1980-01-01','Moscow, Leninskiy prosperkt, 30','+79996677891','VD_Dmitrieva@institution.ru',1),(2,'Yaroslav Yaroslavovich Yaroslavov','assistant professor','assistant professor','18 years','1975-03-08','Moscow, prospekt Kosmonavtov, 12','+75675675657','Y_Yaroslavov@institution.ru',1),(3,'Olga Petrovna Petrova','assistant','none','5 years','1990-05-05','Moscow, prospekt Mira, 21','+79549879864','O_Petrova@institution.ru',2),(4,'Vasiliy Artemovich Ivanov','professor','professor','23 years','1960-06-09','Moscow, Letchika Babushkina street, 19','+74567389021','V_Ivanov@institution.ru',2),(5,'Yulia Andreevna Sokolova','assistant','none','7 years','1987-12-08','Moscow, Abelmanovckaya street, 27','+7961456987','Y_Sokolova@institution.ru',3),(6,'Anton Savelievich Smirnov','senior lecturer','none','18 years','1970-09-09','Moscow, Abramtsevskaya street, 15','+71177755431','A_Smirnov@institution.ru',3),(7,'Vasilisa Viktorovna Karpova','senior lecturer','none','8 years','1991-11-03','Moscow, Alabyan street, 4','+79099092233','V_Karpova@institution.ru',4),(8,'Petr Alekseevich Vasilchuk','assistant professor','assistant professor','13 years','1973-12-09','Moscow, Anuchina street, 8','+79098786556','P_Vasilchuk@institution.ru',4),(9,'Vladimir Viktorovich Uglov','senior lecturer','none','10 years','1962-02-26','Moscow, Artamonova street, 135','+79091113344','V_Uglov@institution.ru',5),(10,'Pavel Alekseevich Utov','assistant professor','assistant professor','14 years','1974-12-11','Moscow, Armavirskaya street, 10','+790829345698','P_Utov@institution.ru',5),(11,'Alexandra Fedorovna Kostrova','assistant','none','11 years','1980-07-06','Moscow, Aerodromnaya street, 78','+79047651020','A_Kostrova@institution.ru',6),(12,'Artem Igorevich Potapov','senior lecturer','none','12 years','1971-06-02','Moscow, Bakinskaya street, 3','+79013450986','A_Potapov@institution.ru',6),(13,'Ignat Vasilievich Kozlov','assistant professor','assistant professor','19 years','1976-04-15','Moscow, Bazhova street, 17','+79017650983','I_Kozlov@instituton.ru',7),(14,'Igor Viktorovich Eremin','assistant professor','assistant professor','20 years','1977-05-29','Moscow, Barklaya street, 20','+79017650233','I_Eremin@instituton.ru',7),(15,'Yuri Pavlovich Losev','senior lecturer','none','14 years','1978-06-03','Moscow, Barrikadnaya street, 135','+79026785493','Y_Losev@institution.ru',8),(16,'Alena Dmitrievna Kozakova','assistant professor','assistant professor','20 years','1977-10-18','Moscow, Bataiskaya street, 67','+79034567894','A_Kozakova@institution.ru',8),(17,'Dinara Arturovna Galimyanova','assistant','none','9 years','1983-08-01','Moscow, Borovskiy proezd, 6','+79039871236','D_Galimyanova@institution.ru',9),(18,'Kseniya Glebovna Pestova','assistant professor','assistant professor','16 years','1980-11-14','Moscow, Bahrushina street, 96','+79161881910','KG_Pestova@institution.ru',9);
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheet`
--

DROP TABLE IF EXISTS `sheet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sheet` (
  `sheet_id` int NOT NULL AUTO_INCREMENT,
  `study_year` enum('1','2','3','4','5') NOT NULL,
  `semester` enum('1','2','3','4','5','6','7','8','9','10') NOT NULL,
  `stgroup_id` int DEFAULT NULL,
  `subject_id` int DEFAULT NULL,
  `professor_id` int DEFAULT NULL,
  PRIMARY KEY (`sheet_id`),
  KEY `sheet_ibfk_1` (`stgroup_id`),
  KEY `sheet_ibfk_2` (`subject_id`),
  KEY `sheet_ibfk_3` (`professor_id`),
  CONSTRAINT `sheet_ibfk_1` FOREIGN KEY (`stgroup_id`) REFERENCES `stgroup` (`stgroup_id`) ON DELETE CASCADE,
  CONSTRAINT `sheet_ibfk_2` FOREIGN KEY (`subject_id`) REFERENCES `subject` (`subject_id`) ON DELETE CASCADE,
  CONSTRAINT `sheet_ibfk_3` FOREIGN KEY (`professor_id`) REFERENCES `professor` (`professor_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheet`
--

LOCK TABLES `sheet` WRITE;
/*!40000 ALTER TABLE `sheet` DISABLE KEYS */;
INSERT INTO `sheet` VALUES (1,'1','1',1,1,1),(2,'1','1',2,2,2),(3,'1','2',1,3,1),(4,'1','2',3,4,3),(5,'1','2',4,5,4),(7,'1','1',6,7,5),(8,'1','2',5,8,6),(9,'1','2',6,9,5),(10,'2','3',7,10,7),(11,'2','4',8,11,8),(12,'2','3',7,12,7),(13,'3','5',9,13,9),(14,'3','6',10,14,10),(15,'3','6',9,15,9),(16,'4','7',11,16,11),(17,'4','8',12,17,12),(18,'4','8',11,18,11),(19,'5','9',13,19,13),(20,'5','10',14,20,14),(21,'5','10',13,21,13),(22,'1','1',15,22,15),(23,'1','2',16,23,16),(24,'1','2',15,24,15),(25,'2','3',17,25,17),(26,'2','4',18,26,18),(27,'2','4',17,27,17);
/*!40000 ALTER TABLE `sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stgroup`
--

DROP TABLE IF EXISTS `stgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stgroup` (
  `stgroup_id` int NOT NULL AUTO_INCREMENT,
  `stgroup_n` int NOT NULL,
  `year_of_admission` year NOT NULL,
  `course` enum('1','2','3','4','5') NOT NULL,
  `department_id` int DEFAULT NULL,
  PRIMARY KEY (`stgroup_id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `stgroup_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stgroup`
--

LOCK TABLES `stgroup` WRITE;
/*!40000 ALTER TABLE `stgroup` DISABLE KEYS */;
INSERT INTO `stgroup` VALUES (1,1,2019,'1',1),(2,2,2019,'1',1),(3,3,2019,'1',2),(4,4,2019,'1',2),(5,5,2019,'1',3),(6,6,2019,'1',3),(7,7,2018,'2',4),(8,8,2018,'2',4),(9,9,2017,'3',5),(10,10,2017,'3',5),(11,11,2016,'4',6),(12,12,2016,'4',6),(13,13,2015,'5',7),(14,14,2015,'5',7),(15,15,2019,'1',8),(16,16,2019,'1',8),(17,17,2018,'2',9),(18,18,2018,'2',9);
/*!40000 ALTER TABLE `stgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `student_fio` varchar(100) NOT NULL,
  `student_date_of_birth` date NOT NULL,
  `student_address` varchar(100) NOT NULL,
  `student_phone` varchar(20) NOT NULL,
  `student_email` varchar(30) NOT NULL,
  `stgroup_id` int DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `stp_index` (`student_phone`),
  UNIQUE KEY `ste_index` (`student_email`),
  KEY `stgroup_id` (`stgroup_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`stgroup_id`) REFERENCES `stgroup` (`stgroup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (1,'Anastasia Andreevna Akopyan','2002-02-20','Moscow, Bobrov pereulok, 34','+79695556677','aaakop@example.ru',1),(2,'Vasiliy Petrovich Makarov','2001-01-23','Moscow, Bumazhniy proezd, 15','+79097659897','vpmakarov@example.ru',1),(3,'Marina Alexandrovna Martinova','2001-03-07','Moscow, Buzheninova street, 4','+79086549872','mamartinova@example.ru',2),(4,'Igor Vladimirovich Karpatov','2002-04-19','Moscow, Vavilova street, 98','+79065678764','ivkarpatov@example.ru',2),(5,'Maria Konstantinovna Komarova','2001-05-04','Moscow, Vilyuiskaya street, 6','+79012349876','mkkomarova@example.ru',3),(6,'Yulia Gennadievna Sidorova','2000-06-24','Moscow, Vishnevaya street, 76','+78980004433','ygsidorova@example.ru',3),(7,'Artem Alekseevich Turin','2001-07-03','Moscow, Verbnaya street, 98','+79893366771','aaturin@example.ru',4),(8,'Ariza Ruslanovna Badoeva','2002-08-12','Moscow, Visotskogo street, 65','+79890010203','arbadoeva@example.ru',4),(9,'Sergey Vitalievich Borunov','2000-08-20','Moscow, Veselaya street, 8','+79099091111','svborunov@example.ru',5),(10,'Sergey Evgenievich Gasanov','2001-01-07','Moscow, Gazetny pereulok, 78','+79076549988','segasanov@example.ru',5),(11,'Natalya Viktorovna Nesterova','2002-10-18','Moscow, Gagarina street, 9','+79095544336','nvnesterova@example.ru',6),(12,'Ivan Antonovich Minalev','2001-12-05','Moscow, Davydkovskaya street, 35','+79083345698','iaminalev@example.ru',6),(13,'Tatiana Andreevna Klimenko','1999-12-12','Moscow, Dvintsev street, 89','+79073467899','taklimenko@example.ru',7),(14,'Evgeny Yaroslavovich Petrenko','1999-01-21','Moscow, Dezhneva proezd, 12','+79098883366','eypetrenko@example.ru',7),(15,'Elena Ivanovna Romanova','1998-12-23','Moscow, Donskaya street, 6','+79097771122','eiromanova@example.ru',8),(16,'Petr Borisovich Vozhkov','1998-11-12','Moscow, Detskaya street, 11','+79109874568','pbvozhkov@example.ru',8),(17,'Lidiya Kirillovna Kuptsova','1999-10-10','Moscow, Domodedovskaya street, 67','+79054467898','lkkuptsova@example.ru',9),(18,'Vladimir Alexandrovich Shesteperov','1999-09-07','Moscow, Evstigneeva street, 8','+79034567888','vashesteperov@example.ru',9),(19,'Daria Mikhilovna Ostrova','1997-09-01','Moscow, Egorievskaya street, 101','+79098881111','dmostrova@example.ru',10),(20,'Mikhail Yaroslavovich Polkanov','1996-08-24','Moscow, Elokhovskiy proezd, 96','+79091118866','mypolkanov@example.ru',10),(21,'Fedor Konstantinovich Ushakov','1996-07-20','Moscow, Zhulebinskaya street, 22','+79092227676','fkushakov@example.ru',11),(22,'Zhanna Markovna Shpitz','1996-06-27','Moscow, Zhuzha street, 1','+79099992213','zm@example.ru',11),(23,'Yaroslav Petrovich Kislov','1995-05-30','Moscow, Zhivopisnaya street, 11','+79046758899','ypkislov@example.ru',12),(24,'Lyubov Alexandrovna Piskunova','1995-05-06','Moscow, Zabelina street, 10','+79034466699','lapiskunova@example.ru',12),(25,'Vitaly Alexandrovich Vedeev','1995-07-19','Moscow, Goncharova street, 15','+79086548765','vavedeev@example.ru',13),(26,'Mark Iosifovich Shmargun','1995-09-10','Moscow, Guriyanova street, 7','+79091236549','mishmargun@example.ru',13),(27,'Maria Alekseevna Sharapova','1995-10-18','Moscow, Dvornikova street, 6','+79093456282','masharapova@example.ru',14),(28,'Nikita Yurievich Kozhevnikov','1995-11-19','Moscow, Druzhbi street, 9','+79012348769','nykozhevnikov@example.ru',14),(29,'Makar Antonovich Yusupov','2001-12-03','Moscow, Domodedovskaya street, 18','+79062789541','mayusupov@example.ru',15),(30,'Alevtina Georgievna Glinka','2002-08-27','Moscow, Eletskaya street, 12','+79092345171','agglinka@example.ru',15),(31,'Ekaterina Yurievna Kolpakova','2001-08-13','Moscow, Zarayskaya street, 15','+79065677654','eykolpakova@example.ru',16),(32,'Sergey Alexandrovich Anchuk','2001-12-06','Moscow, Zelenogradskaya street, 2','+79056793254','asanchuk@example.ru',16),(33,'Yulia Nikolaevna Kalina','2000-12-05','Moscow, Zyuzinskaya street, 9','+79065679933','ynkalina@example.ru',17),(34,'Anton Leonidovich Myasnikov','2000-01-20','Moscow, Zarechie street, 7','+79043567172','almyasnikov@example.ru',17),(35,'Elizaveta Pavlovna Sidorchuk','2000-01-27','Moscow, Zuboxskaya street, 9','+79027865454','epsidorchuk@example.ru',18),(36,'Pavel Valentinovich Nesterov','2000-02-05','Moscow, Istrinskaya street, 9','+79056789090','pvnesterov@example.ru',18),(37,'Yana Yurievna Kosmos','1995-08-19','Moscow, Leninskiy prospekt, 30','+79967897766','yykosmos@example.ru',12);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subject`
--

DROP TABLE IF EXISTS `subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subject` (
  `subject_id` int NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  `subject_type` enum('humanities','mathematics') NOT NULL,
  `hours_quantity` smallint unsigned NOT NULL,
  `control_form` enum('exam','test') NOT NULL,
  `department_id` int DEFAULT NULL,
  PRIMARY KEY (`subject_id`),
  KEY `subject_ibfk_1` (`department_id`),
  CONSTRAINT `subject_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`department_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subject`
--

LOCK TABLES `subject` WRITE;
/*!40000 ALTER TABLE `subject` DISABLE KEYS */;
INSERT INTO `subject` VALUES (1,'Civil law (general part)','humanities',200,'exam',1),(2,'Civil law (special part)','humanities',400,'exam',1),(3,'Business law','humanities',150,'test',1),(4,'Constitutional law','humanities',300,'exam',2),(5,'Administrative law','humanities',500,'exam',2),(7,'Criminal law','humanities',500,'exam',3),(8,'Criminology','humanities',250,'test',3),(9,'Fundamentals of the theory of proof','humanities',500,'exam',3),(10,'Mathematic analysis','mathematics',350,'exam',4),(11,'Mathematical logic','mathematics',350,'exam',4),(12,'Mathematics','mathematics',300,'exam',4),(13,'Theory of Probability and Mathematical Statistics','mathematics',400,'exam',5),(14,'Mathematical programming','mathematics',400,'exam',5),(15,'Scripting languages','mathematics',600,'test',5),(16,'Modern experimental mechanics','mathematics',400,'exam',6),(17,'Experimental mechanics of materials','mathematics',300,'test',6),(18,'Experimental machine mechanics','mathematics',300,'exam',6),(19,'Management','humanities',450,'exam',7),(20,'Accounting','mathematics',500,'exam',7),(21,'Marketing','humanities',350,'test',7),(22,'Economic analysis','mathematics',500,'exam',8),(23,'Audit','mathematics',450,'exam',8),(24,'Risk assessment and management','mathematics',400,'test',8),(25,'Business planning','mathematics',400,'exam',9),(26,'Commercialization of innovations','mathematics',450,'exam',9),(27,'Research','humanities',350,'test',9);
/*!40000 ALTER TABLE `subject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-12 17:13:15
