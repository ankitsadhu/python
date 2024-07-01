```
Datalemur (Easy) - https://www.youtube.com/playlist?list=PLtfxzVLWb-B-F6Ds1p85wLYxPGq1lAsfk

Datalemur (Medium) - https://www.youtube.com/watch?v=EInziDxCoz0&list=PLtfxzVLWb-B-WGRZGsl3SFlHxl49MOfKP

DetaLemur (hard) - https://www.youtube.com/watch?v=osGSIQMJM_w&list=PLtfxzVLWb-B-4zEHGsxoCacaY4QfSVqh8


https://www.interviewquery.com/p/data-science-sql-interview-questions

https://www.youtube.com/playlist?list=PLVD3APpfd1tuXrXBWAntLx4tNaONro5dA

https://www.youtube.com/@iqjayfeng


SQL Interview topics 1.window functions case when self join union shoul use left join rank (over clause) LEAD LAG Group By SUM/COUNT MAX/MIN MOVING AVERAGE/SUM SUBQUERY INDEXING HAVING VS WHERE CTE 1. CASE WHEN. So many great use cases!

Self joins. Common in product user behavior.

DISTINCT and GROUP BY

Left vs outer joins. Need I say more?

UNION. Rarely discussed but frequent.

SUM and COUNT. Nail the foundations!

Date-time manipulation. This will set you apart.

String formatting, substring.

Window functions like rank and row. Absolute gold!

Subqueries. Because they always show up...

HAVING vs WHERE. Do you know why?

LAG and LEAD. What do you use these for?

Understanding indexing. More intermediate.

Running totals. A fun use case to learn.

MAX and MIN. More common than anyone says!


stratascratchSQL (22) ~ 7.3 hours | nariSQL

DATA MODELLING :

1. What is data modeling?
2. What are the objectives of data modeling?
3. What are the three levels of data modeling?
4. What is conceptual data model?
5. What is logical data model?
6. What is physical data model?
7. What is entity relationship diagram (ERD)?
8. What are the components of ERD?
9. What is normalization? What are the normal forms?
10. What is denormalization? When is it used?

SQL :

11. What is SQL?
12. What are the types of SQL commands?
13. What is the difference between WHERE and HAVING clause?
14. What is the difference between UNION and UNION ALL?
15. What is the difference between DELETE and TRUNCATE statements?
16. What is the difference between primary key and unique constraint?
17. What is a view? What are the benefits of views?
18. How to create a view?
19. What is a stored procedure? What are the benefits of stored procedures?
20. How to create a stored procedure?

TRANSACTION :

21. What is a transaction in DBMS?
22. What are the ACID properties of transactions?
23. What is a commit operation?
24. What is a rollback operation?
25. What is a deadlock in transactions?
26. What is a transaction log?
27. What is a savepoint in transactions?
28. What is concurrency control?
29. What are the types of transaction isolation levels?
30. What is two-phase locking (2PL) protocol?

KEYS AND CONSTRAINTS :

31. What is a key in DBMS?
32. What is a primary key?
33. What is a foreign key?
34. What is a composite key?
35. What is a candidate key?
36. What is a unique key?
37. What is a constraint in DBMS?
38. What is a NOT NULL constraint?
39. What is a CHECK constraint?
40. What is a referential integrity constraint?

Database Normalization:

41. What is database normalization?
42. What are the main objectives of normalization?
43. What is the First Normal Form (1NF)?
44. What is the Second Normal Form (2NF)?
45. What is the Third Normal Form (3NF)?
46. What is the Boyce-Codd Normal Form (BCNF)?
47. What is the Fourth Normal Form (4NF)?
48. What is the Fifth Normal Form (5NF)?
49. What is denormalization, and when is it used?
50. What are the advantages and disadvantages of normalization?
```

## *** Technical Assessment ****

* [ ]

## order_id | customer_id | order_datetime | item_id | order_quantity

A-001 | 32483 | 2018-12-15 09:15:22 | B000 | 3
A-005 | 21456 | 2019-01-12 09:28:35 | B001 | 1
A-005 | 21456 | 2019-01-12 09:28:35 | B005 | 1
A-006 | 42491 | 2019-01-16 02:52:07 | B008 | 2

## ITEMS

item_id varchar(10) primary key
item_category varchar(20)
Sample extract from ITEMS

## item_id | item_category

B000 | Outdoors
B001 | Outdoors
B002 | Outdoors
B003 | Kitchen
B004 | Kitchen

/* Questions */
-- Q1: How many UNITS have been ordered yesterday? UNITS is the total quantity ordered.
-- Output as: Units

-- Q2: How many UNITS have been ordered in the last 7 days (including today) in EACH and EVERY category? Please consider SEVEN calendar days in total, including today.
-- Please consider ALL categories, even those which have zero orders.
-- Output as: Category | Units

-- Q3: How many UNITS in EACH and EVERY category have been ordered on each day of the week in the last 7 days (including today)?
-- Output as: Category | Sunday_units | Monday_units | Tuesday_units | Wednesday_units | Thursday_units | Friday_units | Saturday_units

-- Q4: It is possible for customers to place multiple orders on a single date.
-- For ALL customers, write a query to get the earliest ORDER_ID for each customer for each date they placed an order.
-- Output as: Customer_id | Order_date | First_order_id

-- Q5: Write a query to get the second earliest ORDER_ID for each customer for each date they placed AT LEAST two orders.
-- Output as: Customer_id | Order_date | Second_order_id

MSSQL:

```
Q1: 
SELECT COUNT(order_quantity) AS Units
FROM Orders 
WHERE CAST(order_datetime AS DATE) = CAST(DATEADD(DD, -1 GETDATE()) AS DATE)
```

```
Q2: /*(not sure if they need to see 7 calendar days in this query as well, if yes, just add {FORMAT(order_datetime, 'dddd')} in select and group by clause)*/
SELECT item_category, COUNT(CASE WHEN order_quantity IS NULL THEN 0 ELSE order_quantity END) AS Units
FROM Items i
LEFT JOIN Orders o
  ON o.item_id = i.item_id
WHERE CAST(order_datetime AS DATE) >= CAST(DATEADD(DD, -7, GETDATE()) AS DATE)
GROUP BY item_category
```

```
Q3:
/** CREATE CTE OR TEMP TABLE USING Q2 ABOVE AND ADD WeekDay***/
; WITH orders_per_category AS(
    SELECT FORMAT(order_datetime, 'dddd') + '_units' AS WeekDay,
        item_category, 
        CASE WHEN order_quantity IS NULL THEN 0 ELSE order_quantity END AS Units
    FROM Items i
    LEFT JOIN Orders o
       ON o.item_id = i.item_id
    WHERE CAST(order_datetime AS DATE) >= CAST(DATEADD(DD, -7, GETDATE()) AS DATE)
)

SELECT *
FROM orders_per_category
PIVOT (
  SUM(Units)
  FOR WeekDay IN ([Sunday_units], [Monday_units], [Tuesday_units], [Wednesday_units], [Thursday_units], [Friday_units], [Saturday_units])
)B

```

```
Q4: 
SELECT o.Customer_Id, s.Order_Date, MIN(o.Order_id) as First_order_id
FROM Orders o
JOIN(
     SELECT Customer_Id, MIN(Order_Date)
     FROM Orders
    GROUP BY Customer_Id
)S
  ON o.Customer_Id = s.Customer_Id
  AND o.Order_Date = s.Order_Date
GROUP BY o.Customer_Id, s.Order_Date
```

```
Q5:
SELECT Customer_Id, Order_Date, Order_Id AS Second_Order_Id
FROM(
   SELECT Customer_Id, Order_Date, Order_Id, ROW_NUMBER() OVER(PARTITION BY Customer_Id ORDER BY Order_Id ASC) AS rn
   FROM Orders
   WHERE EXISTS(
     SELECT Customer_Id, COUNT(Order_Id) AS cnt
     FROM Orders
     GROUP BY Customer_Id
     HAVING COUNT(Order_Id) >= 2
   )S
WHERE S.rn = 2
```

---
