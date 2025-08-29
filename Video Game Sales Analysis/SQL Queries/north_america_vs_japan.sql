SELECT
  Genre,
  printf("%.2fM", SUM(NA_Sales)) AS North_America_Sales,
  printf("%.2fM", SUM(JP_Sales)) AS Japan_Sales,
  CASE
    WHEN SUM(NA_Sales) > SUM(JP_Sales) THEN 'North America'
    ELSE 'Japan'
  END as Regional_Preference
FROM vgsales
GROUP BY Genre
ORDER BY SUM(Global_Sales) DESC;