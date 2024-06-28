/*
Table1: sf_transactions
|   ID  |   created_ad  |   value   |   purchase_ID |
-----------------------------------------------------
|   1   |   2019-01-0   |   172692  |       43      |
|   3   |   2019-01-09  |   109513  |       30      |
|   6   |   2019-01-21  |   184853  |       31      |
|   10  |   2019-02-06  |   116948  |       43      |
|   15  |   2019-02-26  |   100074  |       49      |
|   21  |   2019-03-22  |   250388  |       47      |
-----------------------------------------------------


|   year_month      |   value                            |
---------------------------------------------------------
|   2019-01 (Jan)   | 172692 + 109513 + 184853  = 467058 |
|   2019-02 (FEB)   | 116948 +  100074 =  217022         | 
|   2019-03 (MARCH) | 250388                             |
----------------------------------------------------------

Monthly % Change = (cur - prev) / prev
 [Jan - Feb] - (217022 - 467058/ 467058) * 100

Step1: SUM(value) GROUP BY year_month
Step2: Use LAG Fun to compare Previous value, LAG & LEAD BUILT IN FUNCTION  = value - LAG(value, 1) OVER (ORDER BY year_month) / LAG(value) OVER (ORDER BY year_month)
*/

WITH
monthly_value AS (
    SELECT TO_CHAR(created_at, 'YYYY-MM') AS year_month,  SUM(Value) AS value
    FROM sf_transactions
    GROUP BY year_month
    ORDER BY year_month
)
SELECT 
    year_month,
    ((value - LAG(value, 1) OVER (ORDER BY year_month)) / LAG(value, 1) OVER (ORDER BY year_month)) * 100
    AS percentage_change
FROM monthly_value 