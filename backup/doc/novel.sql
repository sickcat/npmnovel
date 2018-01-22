CREATE TABLE `Book` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `cover` varchar(255),
  `title` varchar(255),
  `updated` varchar(255) DEFAULT NULL,
  `cat` varchar(255),
  `tags` varchar(255),
  `author` varchar(255),
  `read_count` int(11) DEFAULT 0,
  `word_count` int(11) DEFAULT 0,
  `longintro` text,
  `shortintro` text,
  `last_chapter` int,
  `click_count` int(11) DEFAULT 0,
  `other_info` text DEFAULT NULL,
  `deleted` int(8) DEFAULT 0,
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
  `deleted` int(8) DEFAULT 0,
  `click` int(8) DEFAULT 1,
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

CREATE TABLE `User` (
  `user_id` varchar(255) NOT NULL,
  `read_list` text DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

INSERT INTO `Book`(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, last_chapter, author) VALUES(1, "1/title.png", "测试书本", "2017-01-01", "", "", 15678, 500000, "一本关于测试是的户籍的书", 1, "德成广告");

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(1, "章节1", 1, "章节1", "1.txt", 150, 500000);

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(2, "章节2", 1, "章节2", "2.txt", 150, 500000);

INSERT INTO `Book`(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, last_chapter, author) VALUES(2, "2/title.jpg", "朝花夕拾", "2017-01-01", "", "", 15678, 500000, "《朝花夕拾》里作者鲁迅用夹叙夹议的方法，以青少年时代的生活经历为线索，真实生动地叙写了自己从农村到城镇，从家庭到社会，从国内到国外的一组生活经历，抒发了对往昔亲友和师长的怀念之情，同时也对旧势力、旧文化进行了嘲讽和抨击。", 1, "鲁迅");

INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(3, "狗·猫·鼠", 2, "狗·猫·鼠", "3.txt", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(4, "阿长与山海经", 2, "阿长与山海经", "4.txt", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(5, "二十四孝图", 2, "二十四孝图", "5.txt", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(6, "五猖会", 2, "五猖会", "6.txt", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(7, "无常", 2, "无常", "7.txt", 150, 500000);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(8, "从百草园到三味书屋", 2, "从百草园到三味书屋", "8.txt", 150, 500000);

INSERT INTO `Cat`(cat_id, name) VALUES(1, "全部");

INSERT INTO `Book`(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, last_chapter, author) VALUES(3, "3/title.jpeg", "改革创新大家谈", "2018-01-01", "", "", 0, 500000, "警员干部门对于全面深化改革的优秀看法建议", 9, "深圳市公安局全面深化改革创新领导小组");
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(9, "（报何展辉）接处警流程图_20171022", 3, "（报何展辉）接处警流程图_20171022", "9.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(10, "欧伟国_拴心留人的_20171101", 3, "欧伟国_拴心留人的_20171101", "10.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(11, "林长平_文海局长指示要通_20171106", 3, "林长平_文海局长指示要通_20171106", "11.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(12, "甘桂平_我心目中的_20171103", 3, "甘桂平_我心目中的_20171103", "12.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(13, "李鹏飞_市局召开全局政_20171110", 3, "李鹏飞_市局召开全局政_20171110", "13.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(14, "高一帆_执法服务管理监督_20171104", 3, "高一帆_执法服务管理监督_20171104", "14.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(15, "关于动态整理有关情况(王鸣泽）", 3, "关于动态整理有关情况(王鸣泽）", "15.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(16, "何贵莲_#攻坚行动#_20171107", 3, "何贵莲_#攻坚行动#_20171107", "16.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(17, "赖培勤_高端对话欣赏_20171101", 3, "赖培勤_高端对话欣赏_20171101", "17.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(18, "李冉_保护产权_20171105", 3, "李冉_保护产权_20171105", "18.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(19, "潘晓光_生活中唯一不变的是变化_20171012", 3, "潘晓光_生活中唯一不变的是变化_20171012", "19.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(20, "彭翔_警宝托管中心开放啦_20171021", 3, "彭翔_警宝托管中心开放啦_20171021", "20.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(21, "邵兵_晚上到执勤卡点检查_20171022", 3, "邵兵_晚上到执勤卡点检查_20171022", "21.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(22, "罗明_龙岗信息化建设_20171107", 3, "罗明_龙岗信息化建设_20171107", "22.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(23, "邹红玲_#攻坚行动#--执法闭环_20171022", 3, "邹红玲_#攻坚行动#--执法闭环_20171022", "23.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(24, "程爱民_云终端辛路历程_20171104", 3, "程爱民_云终端辛路历程_20171104", "24.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(25, "程文明_闭环攻坚团队到经侦支队交流工作_20171022", 3, "程文明_闭环攻坚团队到经侦支队交流工作_20171022", "25.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(26, "王莉娜_迎接十九大的每天_20171015", 3, "王莉娜_迎接十九大的每天_20171015", "26.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(27, "刘德炎_全市入室抢劫案件反弹迹象明显_20171021", 3, "刘德炎_全市入室抢劫案件反弹迹象明显_20171021", "27.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(28, "周立群_上周日下午_20171107", 3, "周立群_上周日下午_20171107", "28.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(29, "康凯_深入贯彻落实_20171107", 3, "康凯_深入贯彻落实_20171107", "29.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(30, "田晶莹_十九大安保的任务加重_20171010", 3, "田晶莹_十九大安保的任务加重_20171010", "30.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(31, "柴卫平_#攻坚行动#_20171105", 3, "柴卫平_#攻坚行动#_20171105", "31.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(32, "邵兵_枪库的一米黄线_20171010", 3, "邵兵_枪库的一米黄线_20171010", "32.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(33, "杨焕阳_从优待警20171101", 3, "杨焕阳_从优待警20171101", "33.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(34, "李壁_一直以来_20171101", 3, "李壁_一直以来_20171101", "34.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(35, "王永昌_写在运用警务云终端前_20171109", 3, "王永昌_写在运用警务云终端前_20171109", "35.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(36, "林长平_文海局长的国庆“假期”_20171001", 3, "林长平_文海局长的国庆“假期”_20171001", "36.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(37, "吴发明_塘所推广应用警_20171107", 3, "吴发明_塘所推广应用警_20171107", "37.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(38, "王嘉锐_积极响应落实_20171102", 3, "王嘉锐_积极响应落实_20171102", "38.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(39, "高一帆_#执法服务管理监督_20171101", 3, "高一帆_#执法服务管理监督_20171101", "39.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(40, "周立群_直面问题_20171108", 3, "周立群_直面问题_20171108", "40.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(41, "黄钦庆_接处警流程图_20171022", 3, "黄钦庆_接处警流程图_20171022", "41.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(42, "吴狄_改革在持续发力_20171108", 3, "吴狄_改革在持续发力_20171108", "42.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(43, "任俊元_不忘初心，砥砺前行_20171020", 3, "任俊元_不忘初心，砥砺前行_20171020", "43.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(44, "陈昊_少出去应酬_20171104", 3, "陈昊_少出去应酬_20171104", "44.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(45, "童晓军_党的十九大安保维稳_20171102", 3, "童晓军_党的十九大安保维稳_20171102", "45.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(46, "欧伟国_ 阳光管理的平台_20171101", 3, "欧伟国_ 阳光管理的平台_20171101", "46.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(47, "谢啸皎_我与你同在_20171010", 3, "谢啸皎_我与你同在_20171010", "47.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(48, "李鹏飞_市局政治部编发“双节”_20171009", 3, "李鹏飞_市局政治部编发“双节”_20171009", "48.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(49, "马鸿雁_布吉所涉稳重点人员管控_20171010", 3, "马鸿雁_布吉所涉稳重点人员管控_20171010", "49.html", 0, 0);
INSERT INTO `Chapter`(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES(50, "图片测试", 3, "CHJ", "dct12.html", 0, 0);
