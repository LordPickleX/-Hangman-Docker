-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: hangmandatabase
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `words_dictionary`
--

DROP TABLE IF EXISTS `words_dictionary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `words_dictionary` (
  `id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `words_dictionary`
--

LOCK TABLES `words_dictionary` WRITE;
/*!40000 ALTER TABLE `words_dictionary` DISABLE KEYS */;
INSERT INTO `words_dictionary` VALUES (1,'cat','animals'),(2,'elephant','animals'),(3,'encyclopedia','books'),(4,'forest','nature'),(5,'river','nature'),(6,'mountain','nature'),(7,'computer','technology'),(8,'internet','technology'),(9,'smartphone','technology'),(10,'pasta','cuisine'),(11,'sushi','cuisine'),(12,'taco','cuisine'),(13,'painting','art'),(14,'sculpture','art'),(15,'music','art'),(16,'soccer','sports'),(17,'basketball','sports'),(18,'tennis','sports'),(19,'guitar','music'),(20,'violin','music'),(21,'drums','music'),(22,'empire','history'),(23,'war','history'),(24,'revolution','history'),(25,'beach','travel'),(26,'mountain','travel'),(27,'city','travel'),(28,'atom','science'),(29,'biology','science'),(30,'physics','science'),(31,'novel','literature'),(32,'poetry','literature'),(33,'drama','literature'),(34,'school','education'),(35,'teacher','education'),(36,'student','education'),(37,'chess','games'),(38,'puzzle','games'),(39,'board game','games'),(40,'dress','fashion'),(41,'shirt','fashion'),(42,'jeans','fashion'),(43,'recycle','environment'),(44,'nature','environment'),(45,'sustainability','environment'),(46,'doctor','health'),(47,'hospital','health'),(48,'medicine','health');
/*!40000 ALTER TABLE `words_dictionary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-13  9:58:48
