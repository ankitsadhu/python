-- Most Profitable Companies

/*
-----------------------------------------------------------------------------
|   company     |   sector  |   country     |   market_value    |   profits |
-----------------------------------------------------------------------------
|   ICBC        |  Finance  |     China     |      215.6        |   42.7    |
|   Toyota      |  Cars     |     Japan     |      193.5        |   18.8    |
|   Apple       |  Tech     |     USA       |      483.1        |   37      |
|   BP          |  Energy   |     UK        |      148.8        |   23      |
|   Gzprom      |  Energy   |     Russia    |      88.8         |   39      |
-----------------------------------------------------------------------------
Find 3 most profitable company in the world
*/


SELECt company, profits
FROM forbes_global_2010
ORDER BY profits DESC 
LIMIT 3