DELIMITER ;;
CREATE DEFINER=`hw4app`@`%` PROCEDURE `usp_createlogin`(
   in `@username` varchar(30),
   in `@email` varchar(50),
   in `@pwd` varchar(60)
)
begin
insert into `logins` (`username`, `password`, `email`) values (`@username`, `@pwd`, `@email`);
commit;
end ;;
DELIMITER ;

DELIMITER ;;
CREATE DEFINER=`hw4app`@`%` PROCEDURE `usp_getcount`()
select count(*) as `cnt` From   `logins` ;;
DELIMITER ;
