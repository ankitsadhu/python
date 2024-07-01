/*
| id | first_name | salary  | manager_id |
------------------------------------------
| 1  |  Allen     | 200 000 |     1      |
| 10 |  Jenifer   |   1 000 |     13     |            
| 11 |  Richard   | 250 000 |     1      |
| 13 |  Katty     | 150 000 |     1      |  

Solution: Self Join
*/

SELECT emp1.first_name, emp1.salary
FROM employee emp1
JOIN employee emp2
ON emp1.manager_id = emp2.id
WHERE emp1.salary > emp2.salary
