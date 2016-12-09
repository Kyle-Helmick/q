-- MySQL dump 10.13  Distrib 5.7.16, for Linux (armv7l)
--
-- Host: localhost    Database: qdata
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `id` int(11) NOT NULL,
  `firstname` tinytext,
  `lastname` tinytext,
  `lastlogin` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sessions`
--

DROP TABLE IF EXISTS `sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sessions` (
  `sessionid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `username` tinytext,
  `logindate` datetime DEFAULT NULL,
  `ipaddr` tinytext,
  PRIMARY KEY (`sessionid`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` VALUES (37,3,'abc123@gmail.com','2016-12-07 14:57:03','10.200.155.178'),(38,3,'abc123@gmail.com','2016-12-07 14:59:03','10.200.155.178'),(39,3,'abc123@gmail.com','2016-12-07 14:59:17','10.200.155.178'),(40,3,'abc123@gmail.com','2016-12-07 14:59:27','10.200.155.178'),(41,3,'abc123@gmail.com','2016-12-07 15:00:31','10.200.155.178'),(42,3,'abc123@gmail.com','2016-12-07 15:04:53','10.200.155.178'),(43,3,'abc123@gmail.com','2016-12-07 15:07:26','10.200.155.178'),(44,3,'abc123@gmail.com','2016-12-07 15:20:58','10.200.155.178'),(47,6,'michael.gohde@colorado.edu','2016-12-07 16:57:15','128.138.20.165'),(48,3,'abc123@gmail.com','2016-12-07 17:02:12','10.201.24.206'),(49,3,'abc123@gmail.com','2016-12-07 17:03:03','10.201.24.206'),(50,3,'abc123@gmail.com','2016-12-07 17:12:50','10.201.24.206'),(51,3,'abc123@gmail.com','2016-12-07 17:44:49','10.201.24.206'),(52,3,'abc123@gmail.com','2016-12-07 18:07:51','172.21.64.46'),(54,9,'j864188@mvrht.com','2016-12-07 21:23:51','10.202.195.61'),(55,3,'abc123@gmail.com','2016-12-08 13:10:13','10.200.155.178');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlookup`
--

DROP TABLE IF EXISTS `userlookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlookup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` tinytext NOT NULL,
  `passhash` tinytext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlookup`
--

LOCK TABLES `userlookup` WRITE;
/*!40000 ALTER TABLE `userlookup` DISABLE KEYS */;
INSERT INTO `userlookup` VALUES (1,'a','e9d71f5ee7c92d6dc9e92ffdad17b8bd49418f98'),(3,'abc123@gmail.com','5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'),(6,'michael.gohde@colorado.edu','5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'),(7,'abc123@gmail.com','5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'),(8,'hello@gmail.com','6367c48dd193d56ea7b0baad25b19455e529f5ee'),(9,'j864188@mvrht.com','7963c814a12223db8fe40d021546327bd004c1fd'),(10,'diana','5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'),(11,'diana','5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8');
/*!40000 ALTER TABLE `userlookup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usrentries`
--

DROP TABLE IF EXISTS `usrentries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usrentries` (
  `entryid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `description` text,
  `class` tinytext,
  `duedate` datetime DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  `title` tinytext,
  PRIMARY KEY (`entryid`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usrentries`
--

LOCK TABLES `usrentries` WRITE;
/*!40000 ALTER TABLE `usrentries` DISABLE KEYS */;
INSERT INTO `usrentries` VALUES (11,6,'Do a presentation for CSCI 3308','none','2016-12-07 00:00:00',2,'Presentation'),(18,3,'Example for the presentation','none','2016-12-07 00:00:00',1,'Somethings here already!'),(19,3,'Buy some Apples','none','2016-12-12 00:00:00',3,'Apples'),(20,8,'b','none','2016-09-12 00:00:00',1,'a'),(21,9,'df','none','2016-10-20 00:00:00',3,'remind ');
/*!40000 ALTER TABLE `usrentries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-09 15:34:36
