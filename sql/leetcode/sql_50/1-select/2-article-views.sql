/*
|  article_id    |   author_id    |   viewer_id   |    view_date    | 
---------------------------------------------------------------------
|   1            |      3          |    5         |     2019-08-01  |
|   1            |      3          |    6         |     2019-08-02  |

author_id & viewer_id indicates the same person
Find all the authors that view at least one of their own articles
Sort the result by id in asc order
*/

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id