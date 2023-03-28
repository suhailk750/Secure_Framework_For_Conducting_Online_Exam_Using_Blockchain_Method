/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - online_exam
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_exam` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `online_exam`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add department',7,'add_department'),
(26,'Can change department',7,'change_department'),
(27,'Can delete department',7,'delete_department'),
(28,'Can view department',7,'view_department'),
(29,'Can add feedback',8,'add_feedback'),
(30,'Can change feedback',8,'change_feedback'),
(31,'Can delete feedback',8,'delete_feedback'),
(32,'Can view feedback',8,'view_feedback'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add notification',10,'add_notification'),
(38,'Can change notification',10,'change_notification'),
(39,'Can delete notification',10,'delete_notification'),
(40,'Can view notification',10,'view_notification'),
(41,'Can add subject',11,'add_subject'),
(42,'Can change subject',11,'change_subject'),
(43,'Can delete subject',11,'delete_subject'),
(44,'Can view subject',11,'view_subject'),
(45,'Can add study_material',12,'add_study_material'),
(46,'Can change study_material',12,'change_study_material'),
(47,'Can delete study_material',12,'delete_study_material'),
(48,'Can view study_material',12,'view_study_material'),
(49,'Can add student',13,'add_student'),
(50,'Can change student',13,'change_student'),
(51,'Can delete student',13,'delete_student'),
(52,'Can view student',13,'view_student'),
(53,'Can add staff',14,'add_staff'),
(54,'Can change staff',14,'change_staff'),
(55,'Can delete staff',14,'delete_staff'),
(56,'Can view staff',14,'view_staff'),
(57,'Can add result',15,'add_result'),
(58,'Can change result',15,'change_result'),
(59,'Can delete result',15,'delete_result'),
(60,'Can view result',15,'view_result'),
(61,'Can add exam',16,'add_exam'),
(62,'Can change exam',16,'change_exam'),
(63,'Can delete exam',16,'delete_exam'),
(64,'Can view exam',16,'view_exam'),
(65,'Can add doubt',17,'add_doubt'),
(66,'Can change doubt',17,'change_doubt'),
(67,'Can delete doubt',17,'delete_doubt'),
(68,'Can view doubt',17,'view_doubt'),
(69,'Can add complaints',18,'add_complaints'),
(70,'Can change complaints',18,'change_complaints'),
(71,'Can delete complaints',18,'delete_complaints'),
(72,'Can view complaints',18,'view_complaints'),
(73,'Can add allocated_sub',19,'add_allocated_sub'),
(74,'Can change allocated_sub',19,'change_allocated_sub'),
(75,'Can delete allocated_sub',19,'delete_allocated_sub'),
(76,'Can view allocated_sub',19,'view_allocated_sub');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(19,'online_exam','allocated_sub'),
(18,'online_exam','complaints'),
(7,'online_exam','department'),
(17,'online_exam','doubt'),
(16,'online_exam','exam'),
(8,'online_exam','feedback'),
(9,'online_exam','login'),
(10,'online_exam','notification'),
(15,'online_exam','result'),
(14,'online_exam','staff'),
(13,'online_exam','student'),
(12,'online_exam','study_material'),
(11,'online_exam','subject'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-03-17 11:32:37.767522'),
(2,'auth','0001_initial','2023-03-17 11:32:38.917351'),
(3,'admin','0001_initial','2023-03-17 11:32:39.187334'),
(4,'admin','0002_logentry_remove_auto_add','2023-03-17 11:32:39.207561'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-03-17 11:32:39.227476'),
(6,'contenttypes','0002_remove_content_type_name','2023-03-17 11:32:39.479729'),
(7,'auth','0002_alter_permission_name_max_length','2023-03-17 11:32:39.727138'),
(8,'auth','0003_alter_user_email_max_length','2023-03-17 11:32:39.787557'),
(9,'auth','0004_alter_user_username_opts','2023-03-17 11:32:39.817546'),
(10,'auth','0005_alter_user_last_login_null','2023-03-17 11:32:39.927173'),
(11,'auth','0006_require_contenttypes_0002','2023-03-17 11:32:39.927173'),
(12,'auth','0007_alter_validators_add_error_messages','2023-03-17 11:32:39.952114'),
(13,'auth','0008_alter_user_username_max_length','2023-03-17 11:32:40.067438'),
(14,'auth','0009_alter_user_last_name_max_length','2023-03-17 11:32:40.197501'),
(15,'auth','0010_alter_group_name_max_length','2023-03-17 11:32:40.227345'),
(16,'auth','0011_update_proxy_permissions','2023-03-17 11:32:40.247168'),
(17,'auth','0012_alter_user_first_name_max_length','2023-03-17 11:32:40.380081'),
(18,'online_exam','0001_initial','2023-03-17 11:32:42.857319'),
(19,'sessions','0001_initial','2023-03-17 11:32:42.928854');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

/*Table structure for table `online_exam_allocated_sub` */

DROP TABLE IF EXISTS `online_exam_allocated_sub`;

CREATE TABLE `online_exam_allocated_sub` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `staf_id_id` bigint NOT NULL,
  `sub_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_allocate_staf_id_id_25e665d3_fk_online_ex` (`staf_id_id`),
  KEY `online_exam_allocate_sub_id_id_c3d68f09_fk_online_ex` (`sub_id_id`),
  CONSTRAINT `online_exam_allocate_staf_id_id_25e665d3_fk_online_ex` FOREIGN KEY (`staf_id_id`) REFERENCES `online_exam_staff` (`id`),
  CONSTRAINT `online_exam_allocate_sub_id_id_c3d68f09_fk_online_ex` FOREIGN KEY (`sub_id_id`) REFERENCES `online_exam_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_allocated_sub` */

/*Table structure for table `online_exam_complaints` */

DROP TABLE IF EXISTS `online_exam_complaints`;

CREATE TABLE `online_exam_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_complaints_lid_id_3c84814b_fk_online_exam_login_id` (`lid_id`),
  CONSTRAINT `online_exam_complaints_lid_id_3c84814b_fk_online_exam_login_id` FOREIGN KEY (`lid_id`) REFERENCES `online_exam_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_complaints` */

/*Table structure for table `online_exam_department` */

DROP TABLE IF EXISTS `online_exam_department`;

CREATE TABLE `online_exam_department` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `department` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_department` */

/*Table structure for table `online_exam_doubt` */

DROP TABLE IF EXISTS `online_exam_doubt`;

CREATE TABLE `online_exam_doubt` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `staf_id_id` bigint NOT NULL,
  `stud_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_doubt_staf_id_id_a6d381b9_fk_online_exam_staff_id` (`staf_id_id`),
  KEY `online_exam_doubt_stud_id_id_e5fa17de_fk_online_exam_student_id` (`stud_id_id`),
  CONSTRAINT `online_exam_doubt_staf_id_id_a6d381b9_fk_online_exam_staff_id` FOREIGN KEY (`staf_id_id`) REFERENCES `online_exam_staff` (`id`),
  CONSTRAINT `online_exam_doubt_stud_id_id_e5fa17de_fk_online_exam_student_id` FOREIGN KEY (`stud_id_id`) REFERENCES `online_exam_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_doubt` */

/*Table structure for table `online_exam_exam` */

DROP TABLE IF EXISTS `online_exam_exam`;

CREATE TABLE `online_exam_exam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `sub_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_exam_sub_id_id_09827625_fk_online_exam_subject_id` (`sub_id_id`),
  CONSTRAINT `online_exam_exam_sub_id_id_09827625_fk_online_exam_subject_id` FOREIGN KEY (`sub_id_id`) REFERENCES `online_exam_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_exam` */

/*Table structure for table `online_exam_feedback` */

DROP TABLE IF EXISTS `online_exam_feedback`;

CREATE TABLE `online_exam_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_feedback` */

/*Table structure for table `online_exam_login` */

DROP TABLE IF EXISTS `online_exam_login`;

CREATE TABLE `online_exam_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_login` */

/*Table structure for table `online_exam_notification` */

DROP TABLE IF EXISTS `online_exam_notification`;

CREATE TABLE `online_exam_notification` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `notification` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_notification` */

/*Table structure for table `online_exam_result` */

DROP TABLE IF EXISTS `online_exam_result`;

CREATE TABLE `online_exam_result` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `stud_id_id` bigint NOT NULL,
  `sub_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_result_stud_id_id_d1f83826_fk_online_exam_student_id` (`stud_id_id`),
  KEY `online_exam_result_sub_id_id_bf1ad033_fk_online_exam_subject_id` (`sub_id_id`),
  CONSTRAINT `online_exam_result_stud_id_id_d1f83826_fk_online_exam_student_id` FOREIGN KEY (`stud_id_id`) REFERENCES `online_exam_student` (`id`),
  CONSTRAINT `online_exam_result_sub_id_id_bf1ad033_fk_online_exam_subject_id` FOREIGN KEY (`sub_id_id`) REFERENCES `online_exam_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_result` */

/*Table structure for table `online_exam_staff` */

DROP TABLE IF EXISTS `online_exam_staff`;

CREATE TABLE `online_exam_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lname` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_staff_lid_id_ca45b65b_fk_online_exam_login_id` (`lid_id`),
  CONSTRAINT `online_exam_staff_lid_id_ca45b65b_fk_online_exam_login_id` FOREIGN KEY (`lid_id`) REFERENCES `online_exam_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_staff` */

/*Table structure for table `online_exam_student` */

DROP TABLE IF EXISTS `online_exam_student`;

CREATE TABLE `online_exam_student` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `lname` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_student_lid_id_64968ff4_fk_online_exam_login_id` (`lid_id`),
  CONSTRAINT `online_exam_student_lid_id_64968ff4_fk_online_exam_login_id` FOREIGN KEY (`lid_id`) REFERENCES `online_exam_login` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_student` */

/*Table structure for table `online_exam_study_material` */

DROP TABLE IF EXISTS `online_exam_study_material`;

CREATE TABLE `online_exam_study_material` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `materials` varchar(100) NOT NULL,
  `sub_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_study_ma_sub_id_id_753f6622_fk_online_ex` (`sub_id_id`),
  CONSTRAINT `online_exam_study_ma_sub_id_id_753f6622_fk_online_ex` FOREIGN KEY (`sub_id_id`) REFERENCES `online_exam_subject` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_study_material` */

/*Table structure for table `online_exam_subject` */

DROP TABLE IF EXISTS `online_exam_subject`;

CREATE TABLE `online_exam_subject` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) NOT NULL,
  `d_id_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `online_exam_subject_d_id_id_bdff9ce7_fk_online_ex` (`d_id_id`),
  CONSTRAINT `online_exam_subject_d_id_id_bdff9ce7_fk_online_ex` FOREIGN KEY (`d_id_id`) REFERENCES `online_exam_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `online_exam_subject` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
