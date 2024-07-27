/*

| product_id (P.K)   |   low_fats    |   recyclable  |
------------------------------------------------------
|   0                |      Y        |      N         |
|   1                |      Y        |      Y        |
|   2                |      N        |      Y         |
|   3                |      Y        |      Y         |
|   4                |      Y        |      N         |
-------------------------------------------------------

Find ids of product both low_fats & recycable
*/

SELECT 
    product_id
FROM 
    Products
WHERE
    low_fats = 'Y' AND recycable = 'Y'