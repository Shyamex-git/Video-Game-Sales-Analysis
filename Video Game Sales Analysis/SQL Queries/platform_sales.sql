SELECT
  Platform,
  SUM(Global_Sales) AS Total_Sales_in_Millions
FROM
  vgsales
GROUP BY
  Platform
ORDER BY
  Total_Sales_in_Millions DESC
LIMIT 10;