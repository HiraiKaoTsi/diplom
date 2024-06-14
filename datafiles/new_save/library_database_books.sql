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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_book` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `ISBN` varchar(20) NOT NULL,
  `year_publication` year DEFAULT NULL,
  `quantity` int DEFAULT '1',
  `price` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (10,'Покоя больше нет.','Ачебе Ч','978-5-04-767492-6',1965,1,0.49),(11,'Свидетель.','Адалян Н','978-5-04-818897-2',1987,2,1.9),(12,'П. Жизнь прожить.','Астафьев В','978-5-04-138558-3',1986,1,1.6),(13,'Не забывай меня, солнце.','Абдулин А','978-5-04-128932-4',1988,1,1),(14,'Олешина изба.','Абрамов Ф','978-5-04-649511-9',1976,1,0.99),(15,'Избранное.','Андреев Л','978-5-04-858170-4',1988,1,2),(16,'В городе в 70-х годах.','Афанасьев А','978-5-04-358328-4',1976,1,0.67),(17,'Повести гор и степей.','Айтматов Ч','978-5-04-310001-6',1980,1,0.35),(18,'Пламя родного очега.','Абубакар А','978-5-04-060363-3',1976,1,0.74),(19,'Махмудов.','Агим С','978-5-04-311395-5',1966,1,0.38),(20,'Последний поклон.','Астафьев В','978-5-04-915042-8',1983,1,0.65),(21,'Родники рождаются в горах.','Алиева Ф','978-5-04-089512-0',1971,1,0.46),(22,'Победители.','Адамов Г','978-5-04-752123-7',1990,1,3.6),(23,'Урок жестокости.','Абашидзе Г','978-5-04-670727-4',1971,1,0.46),(24,'Запах земли.','Атаров Н','978-5-04-898269-3',1965,1,0.63),(25,'Два долгих дня.','Андреев В','978-5-04-746909-6',1970,1,0.14),(26,'И день настал.','Аксов В','978-5-04-785256-0',1971,1,0.67),(27,'Образы и судьбы.','Апушкин Я','978-5-04-554281-4',1966,1,0.4),(28,'Расказы о суворове.','Алексеев С','978-5-04-705013-3',1990,1,0.5),(29,'Вэтой неброской сторонке.','Арцибашев А','978-5-04-286375-2',1988,1,0.7),(30,'Свет в затемненом мире.','Асанов Н','978-5-04-730222-5',1964,1,0.6),(31,'Угол чужой стены.','Асанов Н','978-5-04-740157-7',1962,1,0.55),(32,'Унас во дворе.','Авдеев В','978-5-04-508916-6',1980,1,0.9),(33,'Деревянные кони.','Абрамов Ф','978-5-04-065943-2',1978,1,1.8),(34,'Скромный контотьер.','Алексеев В','978-5-04-742406-4',1991,1,4.1),(35,'Хлебозоры.','Алексеев С','978-5-04-195629-5',1990,1,1.4),(36,'Наследники.','Алексеев М','978-5-04-420590-1',1961,1,0.49),(37,'Вишневый омут.','Алексеев М','978-5-04-827152-0',1980,1,1.2),(38,'Синие горы.','Алимжанов А','978-5-04-785791-6',1967,1,0.84),(39,'Вгорах туман.','Айсли А','978-5-04-709893-7',1966,1,0.2),(40,'Над куров теплых лесах.','Айсли А','978-5-04-328726-7',1976,1,0.4),(41,'Сказка о хрустальной пепелдьнице.','Айлисли А','978-5-04-369489-8',1977,1,0.75),(42,'Братья и сестра.','Абрамов Ф','978-5-04-829287-7',1980,1,2),(43,'Вам письмо.','Арлазоровой М','978-5-04-941515-2',1966,1,1.04),(44,'Увеликих истоков.','Азарх Р','978-5-04-823487-7',1967,1,0.42),(45,'Далеко от Москвы.','Ажаев В','978-5-04-740539-1',1966,1,1.54),(46,'Дата Татушхия.','Амирэджеби Ч','978-5-04-700000-8',1990,1,4),(47,'Гонец.','Алимжанова А','978-5-04-934662-3',1978,1,0.9),(48,'Залпы ноевого ковчега.','Абрагам П','978-5-04-298742-7',1975,1,1.03),(49,'Две зимы и три лета','Абрамов Ф','978-5-04-366119-7',1986,1,0.8),(50,'Правда оправде.','Артемов В','978-5-04-165801-4',1979,1,0.5),(51,'Избранное','Аргези Т','978-5-04-528809-5',1976,1,1.83),(52,'Очерки, статьи.','Айтматов Ч','978-5-04-011832-8',1975,1,0.71),(53,'Избранное. Т.1.','Атаров Н','978-5-04-008838-6',1971,1,0.83),(54,'Избранное произведения.','Анненский И','978-5-04-636051-6',1988,1,3.3),(55,'Долг.','Арясов И','978-5-04-357595-1',1980,1,1.1),(56,'Собрание сочинений в 3-х т. Т.1.','Аксаков С','978-5-04-612448-4',1986,1,3),(57,'Собрание сочинений в 3-х т. Т.2.','Аксаков С','978-5-04-215771-4',1986,1,2.8),(58,'Собрание сочинений в 3-х т. Т.3.','Аксаков С','978-5-04-173004-8',1986,1,2.5),(59,'Собрание сочинений в 5-х т. Т.2.','Аксаков С','978-5-04-003656-1',1966,1,0.9),(60,'Затежной выстрел.','Азольский А','978-5-04-511052-5',1989,1,1.8),(61,'Преревал. Кража.','Астафьев В','978-5-04-751919-7',1988,1,0.9),(62,'Где-то гремит война.','Астафьев В','978-5-04-875186-2',1990,1,1.2),(63,'Стрела Маханбета.','Алимжанов А','978-5-04-052772-4',1972,1,0.67),(64,'Деревенские расказы.','Ауэрбах Б','978-5-04-811070-6',1967,1,0.84),(65,'Око бюрокана.','Арзуманян А','978-5-04-020329-1',1976,1,1.11),(66,'Царь-рыба.','Астафьев В','978-5-04-688365-7',1986,1,0.9),(67,'Повести.','Абрамов Ф','978-5-04-296848-8',1988,1,0.75),(68,'Открыватели дорог.','Асанов Н','978-5-04-290945-0',1979,1,1.6),(69,'Так онол и бывает.','Ардов В','978-5-04-813954-7',1976,1,0.3),(70,'Т. Записки ружейного охотника.','Аксаков С','978-5-04-542359-5',1987,1,1.9),(71,'П. Разорваный рубль.','Антонов С','978-5-04-777136-6',1989,1,0.7),(72,'Повести и расказвы.','Ахтанов Т','978-5-04-666840-7',1966,1,0.54),(73,'Багрянная летопись.','Андреев Ю','978-5-04-969083-2',1988,1,2.2),(74,'Покоябольше нет.','Ачебе Ч','978-5-04-503936-9',1965,1,0.49),(75,'Всадник переходит бурную реку','Ашинов Х','978-5-04-118955-6',1966,1,0.49),(76,'Мост на дрине.','Андрич И','978-5-04-757993-1',1985,1,2.7),(77,'Сын Эрзянский.','Абрамов К','978-5-04-816716-8',1976,1,0.77),(78,'Повесть','Абрамов Ф','978-5-04-324797-1',1988,1,0.75),(79,'Берестянная грамота.','Алфимов Е','978-5-04-295982-0',1980,1,1.2),(80,'Ветер с моря.','Асанов Н','978-5-04-924878-1',1965,1,0.88),(81,'Волшебный камень.','Асанов Н','978-5-04-219749-9',1961,1,0.8),(82,'Повести ирасказы.','Астафьев В','978-5-04-795438-7',1984,1,2.6),(83,'Повести и расказы.','Андреев Л','978-5-04-666946-6',1979,1,2),(84,'Жизнь прожить.','Астафьев В','978-5-04-481755-5',1986,1,1.5),(85,'Красная роса.','Абдулин А','978-5-04-268259-9',1985,1,0.75),(86,'Информация из будущего.','Ахметов С','978-5-04-047904-7',1986,1,0.6),(87,'Земляки.','Абдулин Х','978-5-04-548777-1',1968,1,0.43),(88,'И помни обо мне.','Афанасьев А','978-5-04-574410-2',1985,1,1.2),(89,'Красноя роса.','Абдулин А','978-5-04-929608-9',1985,1,1.2),(90,'Победители недр.','Адамов Г','978-5-04-015522-4',1990,1,3.6),(91,'213','312','321',2000,1,1231),(92,'test','test','132',2000,1,345);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-14  7:56:02