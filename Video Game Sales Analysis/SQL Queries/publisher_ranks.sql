SELECT
  Publisher,
  SUM(Global_Sales) AS Total_Sales_in_Millions
FROM
  vgsales
GROUP BY
  Publisher
ORDER BY
  Total_Sales_in_Millions DESC
LIMIT 10;