SELECT
  Year_of_Release,
  SUM(Global_Sales) AS Total_Sales_in_Millions
FROM
  vgsales
WHERE
  Year_of_Release != 'N/A' -- This filters out any rows with missing year data
GROUP BY
  Year_of_Release
ORDER BY
  Year_of_Release;