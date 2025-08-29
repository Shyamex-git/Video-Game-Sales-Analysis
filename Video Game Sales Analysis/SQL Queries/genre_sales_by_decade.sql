SELECT
  -- Group years into decades for clear trend analysis
  CASE
    WHEN Year_of_Release BETWEEN '1980' AND '1989' THEN '1980s'
    WHEN Year_of_Release BETWEEN '1990' AND '1999' THEN '1990s'
    WHEN Year_of_Release BETWEEN '2000' AND '2009' THEN '2000s'
    WHEN Year_of_Release >= '2010' THEN '2010s'
    ELSE 'Other'
  END AS Decade,
  Genre,
  printf("%.2fM", SUM(Global_Sales)) AS Total_Sales_in_Decade
FROM vgsales
-- Filter for a few top genres to keep the output focused and readable
WHERE Genre IN ('Action', 'Sports', 'Shooter', 'Role-Playing', 'Platform', 'Misc')
  AND Decade != 'Other'
GROUP BY
  Decade,
  Genre
ORDER BY
  Decade,
  Total_Sales_in_Decade DESC;