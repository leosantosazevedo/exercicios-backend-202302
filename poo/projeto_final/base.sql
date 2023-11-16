CREATE DATABASE `loja`;

use `loja` ;

DROP TABLE IF EXISTS `Produto`;

CREATE TABLE `Produto` (
  `IdProduto` int(11) NOT NULL AUTO_INCREMENT,
  `NomeProduto` varchar(50) NOT NULL,
  `DescricaoProduto` varchar(50),
  PRIMARY KEY (`IdProduto`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `Produto` (`NomeProduto`,`DescricaoProduto`) values ('Banana Prata','Banana Prata');
INSERT INTO `Produto` (`NomeProduto`,`DescricaoProduto`) values ('Hershey's','Chocolate Hershey's Meio Amargo');