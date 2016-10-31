-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: qdata
-- ------------------------------------------------------
-- Server version	5.5.53-0ubuntu0.14.04.1

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
INSERT INTO `profiles` VALUES (1,'Test','User','2016-10-30 12:34:42'),(2,'a','b','2016-10-30 19:14:37'),(3,'c','d','2016-10-30 19:14:44'),(4,'e','f','2016-10-30 19:14:54'),(5,'puttest1','puttest2','2016-10-30 19:15:14');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sessions`
--

LOCK TABLES `sessions` WRITE;
/*!40000 ALTER TABLE `sessions` DISABLE KEYS */;
INSERT INTO `sessions` VALUES (1,1,'testuser','2016-10-30 12:41:30','127.0.0.1'),(2,2,'a','2016-10-30 19:24:37','127.0.0.1'),(3,3,'c','2016-10-30 19:25:04','127.0.0.1'),(4,4,'puttest1','2016-10-30 19:25:49','1.2.3.4'),(5,5,'puttest1','2016-10-30 19:26:11','1.2.3.4');
/*!40000 ALTER TABLE `sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlookup`
--

DROP TABLE IF EXISTS `userlookup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlookup` (
  `id` int(11) NOT NULL,
  `username` tinytext NOT NULL,
  `passhash` tinytext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlookup`
--

LOCK TABLES `userlookup` WRITE;
/*!40000 ALTER TABLE `userlookup` DISABLE KEYS */;
INSERT INTO `userlookup` VALUES (1,'testuser','testpassword'),(2,'a','b'),(3,'c','d'),(4,'e','f'),(5,'puttest1','puttest2'),(6,'puttest2','puttest3');
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
  PRIMARY KEY (`entryid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usrentries`
--

LOCK TABLES `usrentries` WRITE;
/*!40000 ALTER TABLE `usrentries` DISABLE KEYS */;
INSERT INTO `usrentries` VALUES (1,1,'Finish doing SQL database stuff','CSCI 3308','2016-10-31 08:00:00',1),(2,1,'Insert waaay more rows.','CSCI 3308','2016-10-31 08:00:00',2),(3,2,'moar stuff','CSCI 3308','2016-10-30 19:27:13',3),(4,2,'Do calc','Calc','2016-10-30 19:27:29',2),(5,2,'Concentrate science','Stuff','2016-10-30 19:27:50',1);
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

-- Dump completed on 2016-10-30 19:28:33
