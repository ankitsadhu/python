/*
Table 1: Worker
| worker_id  | first_name |  salary  |
--------------------------------------
|   1        |  Monika    | 100 000  |
|   2        |  Niharika  |  80 000  |
|   3        |  Vishal    | 300 000  |
|   4        |  Amitah    | 500 000  |
|   5        |  Vivek     | 500 000  |
--------------------------------------

Table 2: Title
| worker_id  | worker_title   | 
-------------------------------  
|   1        |  Manager       |
|   2        |  Executive     | 
|   3        |  Lead          |
|   4        |  Asst. Manager |
|   5        |  Manager       |

MAX SALAY WORKER TITLE
*/

SELECT title.worker_title
FROM worker
JOIN title
ON worker.worker_id = title.worker_id
WHERE worker.salary = (SELECT MAX(salary) FROM worker)
