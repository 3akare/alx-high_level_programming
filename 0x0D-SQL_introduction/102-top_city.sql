-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT `city`, AVG(`value`) as `avg_temp`
FROM `temperatures`
WHERE `month`=6 OR `month`=7
GROUP BY `city`
LIMIT 3;