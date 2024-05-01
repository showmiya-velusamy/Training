Exercise 10 — Tasks

1.Find the longest time that an employee has been at the studio 
    ```sql
    SELECT name,max(years_employed) FROM employees;
    ```
2.For each role, find the average number of years employed by employees in that role
    ```sql
    select Role, avg(Years_employed) from Employees group by Role;
    ```
3.Find the total number of employee years worked in each building
    ```sql
    select Building, sum(Years_employed) as total number of employee years 
    from Employees group by Building;
    ```

Exercise 11 — Tasks
1.Find the number of Artists in the studio (without a HAVING clause)
    ```sql
    SELECT count(role) FROM employees
    WHERE role="Artist"
    ```
2.Find the number of Employees of each role in the studio
    ```sql
    SELECT role,count(role) 
    FROM employees AS number_of_employees
    GROUP BY role
    ```
3.Find the total number of years employed by all Engineers
    ```sql
    SELECT sum(years_employed) 
    FROM employees AS number_of_years
    WHERE Role="Engineer"
    GROUP BY role
    ```
    ```sql
    select sum(years_employed) as 
    [total number of years employed by all Engineers]
    from Employees 
    group by Role having Role = ‘Engineer’;

Exercise 12 — Tasks
1.Find the number of movies each director has directed 
    ```sql
    SELECT director,count(title) 
    FROM movies AS number_of_movies
    GROUP BY director
    ```
2.Find the total domestic and international sales that can be attributed to each director
    ```sql
    SELECT director,sum(domestic_sales+international_sales) 
    FROM movies  
    INNER JOIN boxoffice
        ON movies.id=boxoffice.movie_id
    GROUP BY director
    ```

Exercise 13 — Tasks
1.Add the studio's new production, Toy Story 4 to the list of movies (you can use any director)
    ```sql
    INSERT INTO movies 
    VALUES(16,'Toy Story 4','Woody Allen',2020,114);
    ```

2.Toy Story 4 has been released to critical acclaim! It had a rating of 8.7, and made 340 million domestically and 270 million internationally. Add the record to the BoxOffice table.
    ```sql
    INSERT INTO boxoffice
    VALUES(4,8.7,340000000,270000000)
    ```

Exercise 14 — Tasks
1.The director for A Bug's Life is incorrect, it was actually directed by John Lasseter
    ```sql
    Update Movies 
    set Director = "John Lasseter"
    where id=2;
    ```
2.The year that Toy Story 2 was released is incorrect, it was actually released in 1999
    ```sql
    update movies
    set year=1999
    where title="Toy Story 2";
    ```
3.Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich
    ```sql
    Update Movies 
    set Director = "Lee Unkrich",
    Title="Toy story 3"
    where id=11;
    ```
Exercise 15 — Tasks
1.This database is getting too big, lets remove all movies that were released before 2005. 
    ```sql
    Delete from movies
    where Year < 2005;
    ```
2.Andrew Stanton has also left the studio, so please remove all movies directed by him. 
    ```sql
    Delete from movies 
    where Director = ‘Andrew Stanton’;
    ``` 
 
Exercise 16 — Tasks

1.Create a new table named Database with the following columns:
– Name A string (text) describing the name of the database
– Version A number (floating point) of the latest version of this database
– Download_count An integer count of the number of times this database was downloaded
This table has no constraints.   

    ```sql
    CREATE TABLE database(
        name TEXT,
        version FLOAT,
        Download_count INTEGER,
    );
    ```

Exercise 17 — Tasks

1.Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in. 
    
    ```sql
    ALTER TABLE Movies 
    ADD Aspect_ratio float;
    ```
2.Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.
   
    ```sql
    ALTER TABLE movies
    ADD language TEXT
      DEFAULT English;
    ```

Exercise 18 — Tasks
1.We've sadly reached the end of our lessons, lets clean up by removing the Movies table.

    ```sql
    DROP TABLE IF EXISTS movies;
    ```
2.And drop the BoxOffice table as well.

    ```sql
    DROP TABLE IF EXISTS Boxoffice;
    ```