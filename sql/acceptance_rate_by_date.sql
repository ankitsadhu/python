-- Acceptance Rate By Date

/*
| user_id_sender | user_id_reciever |  date    |  action  |
-----------------------------------------------------------
|     Tim        |  Rob             |  March 1 | sent     |
|     Tim        |  Rob             |  March 2 | accepted | 
|     Rob        |  Fred            |  March 1 | sent     |
|     Rob        |  Jen             |  March 3 | sent     |
|     Rob        |  Jen             |  March 5 | sent     |   
-----------------------------------------------------------       
Expected Output
March 1 (Tim sent to Rob on 1 & accepted on 2, Rob sent to Fred not accepted)
March 1 = 50%

Solution:
Step 1: Split into two table
Step 2: Left Join
*/

WITH
    sent as (SELECT * FROM fb_friend_requests WHERE action = 'sent'),
    accepted as (SELECT * FROM fb_friend_requests WHERE action = 'accepted'

SELECT sent.date, 1.0 * COUNT(accepted.user_id_sender) / COUNT(send.user_id_sender) AS acceptance_rate
FROM sent
LEFT JOIN accepted
ON sent.user_id_sender = accepted.user_id_sender
AND sent.user_id_reciever = accepted.user_id_reciever
GROUP BY sent.date
ORDER BY sent.date