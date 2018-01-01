CREATE TABLE `Book` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `cover` varchar(255),
  `title` varchar(255),
  `updated` varchar(255) DEFAULT NULL,
  `cat` varchar(255),
  `tags` varchar(255),
  `author` varchar(255),
  `read_count` int(11) NOT NULL,
  `word_count` int(11),
  `longintro` text,
  `shortintro` text,
  `last_chapter` int,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `Chapter` (
  `chapter_id` int(11) NOT NULL AUTO_INCREMENT,
  `chapter` varchar(255),
  `book_id` int(11),
  `title` varchar(255) DEFAULT NULL,
  `link` varchar(255),
  `read_count` int(11) NOT NULL,
  `word_count` int(11),
  `longintro` text,
  PRIMARY KEY (`chapter_id`),
  FOREIGN KEY (`book_id`) REFERENCES `Book` (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `Cat` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(11),
  PRIMARY KEY (`cat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

CREATE TABLE `Tag` (
  `tag_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(11),
  PRIMARY KEY (`tag_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;


INSERT INTO `Book`(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, last_chapter, author) VALUES(1, "1/title.png", "测试书本", "2017-01-01", "", "", 15678, 500000, "一本关于测试是的户籍的书", 1, "德成广告");

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(1, "章节1", 1, "章节1", "1", 150, 500000);

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(2, "章节2", 1, "章节2", "2", 150, 500000);

INSERT INTO `Book`(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, last_chapter, author) VALUES(2, "2/title.jpg", "朝花夕拾", "2017-01-01", "", "", 15678, 500000, "《朝花夕拾》里作者鲁迅用夹叙夹议的方法，以青少年时代的生活经历为线索，真实生动地叙写了自己从农村到城镇，从家庭到社会，从国内到国外的一组生活经历，抒发了对往昔亲友和师长的怀念之情，同时也对旧势力、旧文化进行了嘲讽和抨击。", 1, "鲁迅");

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(3, "狗·猫·鼠", 2, "狗·猫·鼠", "3", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(4, "阿长与山海经", 2, "阿长与山海经", "4", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(5, "二十四孝图", 2, "二十四孝图", "5", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(6, "五猖会", 2, "五猖会", "6", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(7, "无常", 2, "无常", "7", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(8, "从百草园到三味书屋", 2, "从百草园到三味书屋", "8", 150, 500000);
