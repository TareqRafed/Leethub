# Write your MySQL query statement below

SELECT score, dense_rank() OVER(ORDER BY SCORE DESC) as "rank" FROM Scores 