/*
Average session time per user per day
Session: A page load - page exit
    facebook_web_log
| user_id   |     time      |   action      |
---------------------------------------------
|   Timmy   |   3:00 Apr 1  |   page_load   |
|   Timmy   |   3:00 Apr 1  |   page_load   |
|   Timmy   |   3:05 Apr 1  |   scroll_down |
|   Timmy   |   3:06 Apr 1  |   page_exit   |
|   Rob     |   1:17 Apr 2  |   page_load   |
|   Timmy   |   1:21 Apr 2  |   page_load   |
|   Rob     |   1:17 Apr 2  |   page_exit   |
|   Timmy   |   1:23 Apr 1  |   page_exit   |

Take the last page load  & page exit per day per user

STEP 1: Split into 2 table into page load & exit
Table1: page_load
| user_id   |     time      |   action      |
---------------------------------------------
|   Timmy   |   3:00 Apr 1  |   page_load   |
|   Timmy   |   3:00 Apr 1  |   page_load   |
|   Rob     |   1:17 Apr 2  |   page_load   |
|   Timmy   |   1:21 Apr 2  |   page_load   |
---------------------------------------------

Table 2: page_exit
| user_id   |     time      |   action      |
---------------------------------------------
|   Timmy   |   3:06 Apr 1  |   page_exit   |
|   Rob     |   1:17 Apr 2  |   page_exit   |
|   Timmy   |   1:23 Apr 1  |   page_exit   |
---------------------------------------------

Now we need to take latest in each table on every date & remove duplicate by doing this
Join table
Diff

*/

WITH 
page_loads as (
    SELECT user_id, DATE(timestamp), MAX(timestamp) as load_time
    FROM facebook_web_log 
    WHERE action = 'page_load'
    GROUP BY user_id, date
)

WITH
page_exits as (
    SELECT user_id, DATE(timestamp), MIN(timestamp) as exit_time
    FROM facebook_web_log 
    WHERE action = 'page_exit'
    GROUP BY user_id, date
)


SELECT page_loads.user_id, page_loads.date, AVG(page_exits.exit_time - page_loads.load_time) as session_time
FROM page_loads
JOIN page_exits
ON page_loads.user_id = page_exits.user_id AND page_loads.date = page_exits.date
GROUP BY user_id

