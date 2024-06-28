-- Premium Vs Freemium

/* Question
Table1: ms_user_dimension
--------------------
| user_id | acc_id |
--------------------
|   1     |  716   |
|   2     |  749   |
|   3     |  713   | (non paying customer 713)
|   4     |  716   |
--------------------

Table 2: ms_account_dimension
--------------------
| acc_id  | paying |
|         |customer|
--------------------
|   713   |  no    |
|   716   |  yes   |
|   723   |  yes   |
|   749   |  yes   |
--------------------

Table 3: ms_download_facts
| date   | user_id | downloads |
--------------------------------
| mar 1  |    1    |   5       |
| mar 1  |    2    |   3       |
| mar 2  |    3    |   7       |
| mar 2  |    4    |   6       |


Q. Find Each day when non paying users downloaded > Paying Customers
| date  | Paying Customer download | Non paying download |
----------------------------------------------------------
| Mar 1 |       5 + 3              |    0                |
| Mar 2 |       6                  |    7                | ✅

*/

/* Solution
Step 1: Joining all tables together select date, paying_customers, non_paying_customer
------------------------------------------------------------------------
| user_id | acc_id | acc_id  |  paying  | date   | user_id | downloads |
|         |        |         | customer |        
------------------------------------------------------------------------
|   1     |  716   |   716   |    yes   | mar 1  |    1    |   5       |
|   2     |  749   |   749   |    yes   | mar 1  |    2    |   3       |
|   3     |  713   |   713   |    no    | mar 2  |    3    |   7       |
|   4     |  716   |   716   |    yes   | mar 2  |    4    |   6       |
------------------------------------------------------------------------


STEP 1: Join all tables
Step 2: Add up downloads using CASE condition, GROUP BY date
Step 3: Only keep rows where non_paying > paying
*/


WITH 
    download_table as (
        SELECT date,
            SUM(CASE WHEN paying_customers = "yes" THEN downloads END) as paying,
            SUM(CASE WHEN paying_customers = "no" THEN downloads END) as non_paying,
        FROM ms_user_dimension table1
        JOIN ms_account_dimension table2
        ON table1.acc_id = table2.acc_id
        JOIN ms_download_facts table3
        ON t1.user_id = t3.user_id
        GROUP BY DATE
    )
SELECT * 
FROM download_table 
WHERE non_paying > paying
ORDER BY date




