CREATE DATABASE AnsibleTraining;
CREATE TABLE `AnsibleTraining`.`students` (
      `id` BIGINT NULL AUTO_INCREMENT,
      `name` VARCHAR(45) NULL,
      PRIMARY KEY (`id`));

USE AnsibleTraining;
INSERT INTO `students` VALUES (1,'Norbert');
INSERT INTO `students` VALUES (2,'Adrian');
INSERT INTO `students` VALUES (3,'Bengt');
INSERT INTO `students` VALUES (4,'Bastian');
INSERT INTO `students` VALUES (5,'Marcus');
GRANT ALL PRIVILEGES ON *.* TO 'flask'@'%' IDENTIFIED BY 'login';
