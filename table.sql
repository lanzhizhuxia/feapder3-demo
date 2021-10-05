-- ----------------------------
-- Table structure for spider_data
-- ----------------------------
CREATE TABLE `spider_data` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `tokenContractAddress` varchar(255) DEFAULT NULL,
  `creator` varchar(255) DEFAULT NULL,
  `createTime` varchar(255) DEFAULT NULL,
  `tokenURIType` varchar(255) DEFAULT NULL,
  `tokenURI` varchar(5000) DEFAULT NULL,
  `tokenId` varchar(255) DEFAULT NULL,
  `statusCode` varchar(255) DEFAULT NULL,
  `data` varchar(5000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
