WITH PublisherGenreSales AS (
  -- First, calculate total sales for each publisher within each genre
  SELECT
    Genre,
    Publisher,
    SUM(Global_Sales) as Total_Sales
  FROM vgsales
  GROUP BY Genre, Publisher
),
RankedPublishers AS (
  -- Now, rank publishers within each genre based on their sales
  SELECT
    Genre,
    Publisher,
    Total_Sales,
    RANK() OVER(PARTITION BY Genre ORDER BY Total_Sales DESC) as Rank
  FROM PublisherGenreSales
)
-- Finally, select the #1 ranked publisher for each genre
SELECT
  Genre,
  Publisher AS Top_Publisher,
  printf("%.2fM", Total_Sales) AS Sales_in_Genre
FROM RankedPublishers
WHERE Rank = 1
ORDER BY Total_Sales DESC;