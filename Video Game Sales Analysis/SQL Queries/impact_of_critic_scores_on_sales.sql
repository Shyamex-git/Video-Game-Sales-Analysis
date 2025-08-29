SELECT
  CASE
    WHEN Critic_Score >= 90 THEN 'A+ : Critically Acclaimed (90+)'
    WHEN Critic_Score >= 80 THEN 'B : Great Reviews (80-89)'
    WHEN Critic_Score >= 70 THEN 'C : Good Reviews (70-79)'
    WHEN Critic_Score >= 50 THEN 'D : Mixed Reviews (50-69)'
    ELSE 'F : Poor Reviews (<50)'
  END AS Critic_Rating_Tier,
  COUNT(Name) AS Number_of_Games,
  printf("$%.2fM", AVG(Global_Sales)) AS Average_Sales_per_Game
FROM vgsales
WHERE Critic_Score IS NOT NULL
GROUP BY Critic_Rating_Tier
ORDER BY Critic_Rating_Tier;