/*
|   id  |   user_id    |    item    |   created_at  |  revenue  |
-----------------------------------------------------
|   1   |   Rob        |    apple   |   2023-01-01  |  1.00     |
|   2   |   Rob        |    orange  |   2023-01-12  |  1.50     |
|   3   |   Jen        |    banana  |   2023-01-02  |  2.00     |
|   4   |   Rob        |    orange  |   2023-01-09  |  1.50     |
|   5   |   Jen        |    pear    |   2023-01-07  |  1.50     |
-----------------------------------------------------------------
Q. Find user who have bought within 7 days
*/

SELECT DISTINCT(t1.user_id)
FROM amazon_transaction t1
JOIN amazon_transaction t2
ON t1.user_id = t2.user_id
AND t2.created - t1.created_at BETWEEN 0 and 7
AND t1.id != t2.id