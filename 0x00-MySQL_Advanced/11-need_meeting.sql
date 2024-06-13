-- script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.

DELIMITER $$
DROP FUNCTION IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
BEGIN
    RETURN (IF (b = 0, 0, a / b));
END
$$
DELIMITER ;