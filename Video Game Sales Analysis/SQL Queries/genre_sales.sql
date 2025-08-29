SELECT
  Genre,
  SUM(Global_Sales) AS Total_Sales_in_Millions
FROM
  vgsales
GROUP BY
  Genre
ORDER BY
  Total_Sales_in_Millions DESC;