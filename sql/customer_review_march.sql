-- Customer Revenue in March

/*
|   id    |   cust_id   |   order_date    | order_details |   order_cost  |
---------------------------------------------------------------------------
|   4     |     7       |    2019-02-01  |     Coat        |       25     |
|   5     |     7       |    2019-03-10  |     Shoes       |       80     |
|   6     |     7       |    2019-03-15  |     Boats       |       100    |
|   13    |     12      |    2019-03-11  |     Slipper     |       20     |
------------------------------------------------------------
Calculate the total revenue from each customer in March 2019 include only customers who were active in March 2019

Problem 1: Extract Month 
order_date: YYYY-MM-DD 
Solution: BUILTIN FUNC "Extract"
    SELECT 
    FROM orders
    WHETE Extract('MONTH' FROM order_date) = 3
    AND Extract('YEAR' FROM order_date) = 2019
*/

SELECT cust_id, SUM(total_order_cost)
FROM orders
WHERE Extract('MONTH' FROM order_date) = 3
AND Extract('YEAR' FROM order_date) = 2019
GROUP BY cust_id
ORDER BY SUM(total_order_cost) DESC

