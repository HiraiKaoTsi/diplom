-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: library_database
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `history_message`
--

DROP TABLE IF EXISTS `history_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `date_emit` date NOT NULL,
  `main_text` longtext NOT NULL,
  `social_network` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_users_id_idx` (`user_id`),
  CONSTRAINT `FK_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_message`
--

LOCK TABLES `history_message` WRITE;
/*!40000 ALTER TABLE `history_message` DISABLE KEYS */;
INSERT INTO `history_message` VALUES (1,8,'2024-05-14','13333','email'),(2,8,'2024-05-14','1312323','email'),(3,8,'2024-05-14','Первое проверочное сообщение!','email'),(4,8,'2024-05-14','zxc!1','email'),(5,8,'2024-05-14','qqqq','email'),(6,8,'2024-05-14','3333','sms'),(7,8,'2024-05-14','жИЗНЬ','email'),(8,8,'2024-05-15','Здравствуйте Максим вы задолжали книгу 2 пожалуйста верните её','sms'),(9,8,'2024-05-15','szxf','sms'),(10,8,'2024-05-15','Здравствуйте максим вы задолжали книгу 2 верните её в течение недели','sms'),(11,8,'2024-05-15','Здравствуйте максим вы задолжали книгу 2 верните её в течение недели','sms'),(12,8,'2024-05-15','Вы задолжали книгу!','sms'),(13,8,'2024-05-15','Тест сообщение!','sms'),(14,8,'2024-05-15','Тест сообщение!231','sms'),(15,8,'2024-05-15','Вы задолжали книгу!','sms'),(16,8,'2024-05-15','Задолжник!','sms'),(17,8,'2024-05-15','Задолжник ТТТ библиотека!','sms'),(18,8,'2024-05-15','Test','email'),(19,8,'2024-05-15','zxc','email'),(20,8,'2024-05-15','qwe','email'),(21,8,'2024-05-15','1111','email'),(22,7,'2024-05-18','test','email'),(23,7,'2024-05-18','Здравствуйте это Библиотека ТТТ вы задолжали книгу пожалуйста придите и продлите ёё либо верните.','email'),(24,7,'2024-05-18','Здравствуйте это Библиотека ТТТ вы задолжали книгу пожалуйста придите и продлите ёё либо верните.','email'),(25,7,'2024-05-18','     book.id, \n        book.name_book, \n        book.author, \n        book.ISBN, \n        book.year_publication, \n        book.quantity, \n        COUNT(take_book.id) AS count_take_book\n    FROM \n        take_book\n    INNER JOIN\n        books ON take_book.book_id = books.id\n    WHERE \n        take_book.date_return IS NULL \n    GROUP BY\n        books.id\n    HAVING\n        (books.quantity - COUNT(take_book.id)) = 0;','email');
/*!40000 ALTER TABLE `history_message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-24 14:45:38
