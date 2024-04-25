## DAY 3
Exercise 1 — Tasks
1.Find the title of each film
    ```sql
    SELECT title FROM movies
    ```
2.Find the director of each film
    ```sql
    SELECT director FROM movies
    ```
3.Find the title and director of each film
    ```sql
    SELECT title,director FROM movies
    ```
4.Find the title and year of each film
    ```sql
    SELECT title,year
    FROM movies 
    ```
5.Find all the information about each film
    ```sql
    SELECT * FROM movies
    ```
Exercise 2 — Tasks
1.Find the movie with a row id of 6
    ```sql
    SELECT *
    FROM movies
    WHERE id=6
    ```

2.Find the movies released in the years between 2000 and 2010
    ```sql
    SELECT *
    FROM movies
    WHERE year BETWEEN 2000 
    AND 2010
    ```

3.Find the movies not released in the years between 2000 and 2010
    ```sql
    SELECT *
    FROM movies
    WHERE year NOT BETWEEN 2000 
    AND 2010
    ```

4.Find the first 5 Pixar movies and their release year
    ```sql
    SELECT *
    FROM movies
    WHERE id BETWEEN 1
    AND 5
    ```
5.Find the movies released in years 1999,2007,2010
    ```sql
    SELECT *
    FROM movies
    WHERE id BETWEEN 1
    AND 5
    ```

Exercise 3 — Tasks
1.Find all the Toy Story movies
    ```sql
    SELECT *
    FROM movies
    WHERE title LIKE "%toy story%";
    ``` 

2.Find all the movies directed by John Lasseter
    ```sql
    SELECT *
    FROM movies
    WHERE director LIKE "john lasseter";
    ```
    ```sql
    SELECT title FROM movies where director="John Lasseter";
    ```
3.Find all the movies (and director) not directed by John Lasseter
    ```sql
    SELECT *
    FROM movies
    WHERE director NOT LIKE "john lasseter";
    ```
    ```sql
    SELECT title FROM movies where director!="John Lasseter";
    ```
4.Find all the WALL-* movies
    ```sql
    SELECT *
    FROM movies
    WHERE title LIKE "%wall%";
    ```
    ```sql
    SELECT *
    FROM movies
    WHERE title LIKE "wall-";
    ```

Exercise 4 — Tasks
1.List all directors of Pixar movies (alphabetically), without duplicates 
    ```sql
    SELECT DISTINCT director FROM movies
    ORDER BY director ASC;
    ```
2.List the last four Pixar movies released (ordered from most recent to least)
    ```sql
    SELECT title FROM movies
    ORDER BY year DESC
    LIMIT 4
    ```
3.List the first five Pixar movies sorted alphabetically
    ```sql
    SELECT * FROM movies
    ORDER BY title ASC 
    LIMIT 5 
    ```
4.List the next five Pixar movies sorted alphabetically
    ```sql
    SELECT * FROM movies
    ORDER BY title ASC
    LIMIT 5 OFFSET 5
    ```

Review 1 — Tasks
1.List all the Canadian cities and their populations 
    ```sql
    SELECT * FROM north_american_cities where country = "Canada"
    ```
2.Order all the cities in the United States by their latitude from north to south
    ```sql
    SELECT * FROM North_american_cities
    WHERE Country="United States" ORDER BY Latitude DESC;
    ```
3.List all the cities west of Chicago, ordered from west to east
    ```sql
    SELECT * 
    FROM North_american_cities
    WHERE longitude <"-87.629798" 
    ORDER BY longitude ASC;
    ```
4.List the two largest cities in Mexico (by population)
    ```sql
    SELECT * 
    FROM North_american_cities
    WHERE country = "mexico" 
    order by population desc
    limit 2;
    ```
5.List the third and fourth largest cities (by population) in the United States and their population
    ```sql
    SELECT * 
    FROM North_american_cities
    WHERE country like "united states" 
    order by population desc 
    limit 2 offset 2;
    ```

Exercise 6 — Tasks

1.Find the domestic and international sales for each movie 
    ```sql
    SELECT title,domestic_sales,international_sales 
    FROM movies
    INNER JOIN Boxoffice
        ON movies.id= Boxoffice.movie_id
    ```
2.Show the sales numbers for each movie that did better internationally rather than domestically
    ```sql
    SELECT title,domestic_sales,international_sales 
    FROM movies
    INNER JOIN Boxoffice
        ON movies.id= Boxoffice.movie_id
    WHERE domestic_sales < international_sales
    ```
3.List all the movies by their ratings in descending order
    ```sql
    SELECT title,rating
    FROM movies
    NNER JOIN Boxoffice
        ON movies.id= Boxoffice.movie_id
    ORDER BY rating DESC
    ```

Exercise 7 — Tasks
1.Find the list of all buildings that have employees
    ```sql
    SELECT distinct building FROM employees;
    ```

2.Find the list of all buildings and their capacity
    ```sql
    SELECT * FROM buildings;
    ```
3.List all buildings and the distinct employee roles in each building (including empty buildings)
    ```sql
    SELECT DISTINCT bilding_name
    FROM buildings
      LEFT JOIN employees
        ON building_name=building
    WHERE role IS NULL;
    ```
Exercise 8 — Tasks
1.Find the name and role of all employees who have not been assigned to a building
    ```sql
    SELECT name, role FROM employees
    WHERE building IS NULL;
    ```
2.Find the names of the buildings that hold no employees
    ```sql
    SELECT DISTINCT building_name
    FROM buildings 
    LEFT JOIN employees
        ON building_name = building
    WHERE role IS NULL;
    ```

Exercise 9 — Tasks
1.List all movies and their combined sales in millions of dollars
    ```sql
    SELECT title, (domestic_sales + international_sales) / 1000000 AS gross_sales_millions
    FROM movies
    JOIN boxoffice
      ON movies.id = boxoffice.movie_id;
    ```
2.List all movies and their ratings in percent
    ```sql
    SELECT title, rating * 10 AS rating_percent
    FROM movies
    JOIN boxoffice
     ON movies.id = boxoffice.movie_id;
    ```
3.List all movies that were released on even number years
    ```sql
    SELECT title, year
    FROM movies
    WHERE year % 2 = 0;
    ```