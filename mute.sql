CREATE TABLE `muted_players` (
 `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
 `client_id` int(11) NOT NULL,
 `admin_id` int(11) NOT NULL DEFAULT '0',
 `muted` tinyint(4) NOT NULL,
 PRIMARY KEY (`id`),
 KEY `client_id` (`client_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8