/*
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

*/

SELECT 
FROM Weather w1
INNER JOIN Weather w2 --common part of both table
WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 -- SUBDATE(w1.recordDate,1) = w1.recordDate
AND w1.temperature > w2.temperature


