UPDATE country_vaccination_stats
    SET daily_vaccination = 0
    WHERE avg(daily_vaccination) IS NaN
UPDATE country_vaccination_stats
    SET daily_vaccination = median(daily_vaccination)
    WHERE daily_vaccination IS NaN
