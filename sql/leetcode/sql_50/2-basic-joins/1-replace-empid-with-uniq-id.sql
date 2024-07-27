/*
Table1: Employees
| id  | name     |
------------------
| 1   | Alice    |
| 7   | Bob      |
| 11  | Meir     |
| 90  | Winston  |
| 3   | Jonathan |
------------------

Table2: EmployeeUNI
| id  |  uniq_id  |
------------------
| 3   | 1         |
| 11  | 2         |
| 90  | 3         |
-------------------

Why Choosing Left Join?
As we need to all rows of left table, & only pick matching id's with right table

*/

SELECT eu.uniq_id,
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id



