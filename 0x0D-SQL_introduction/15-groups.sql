-- lists all the number of records withe the same score
SELECT score,COUNT(*) FROM second_table GROUP BY score;