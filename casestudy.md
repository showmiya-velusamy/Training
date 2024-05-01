```sql
    CREATE TABLE User (
    UserID int Primary key,
    Username varchar,
    Password varchar,
    Email varchar,
    FirstName varchar,
    LastName varchar,
    Date of birth date,
    Profile picture varchar,
    Favourite artworks text,
    );
```
```sql
    CREATE TABLE Artist(
    ArtistID int primary key,
    Name varchar,
    Biography text,
    Birthdate date,
    Nationality text,
    website varchar,
    Contact Information varchar,
    
    );
```
```sql
    CREATE TABLE Artwork(
    ArtworkID int primary key,
    Description text,
    Title varchar,
    CreationDate date,
    Medium text,
    ImageURL varchar,
    ArtistID int,
    FOREIGN KEY (artistID) REFERENCES artist(artistID), 
    );
```

```sql
    CREATE TABLE User_Favourite_Artwork(
    UserID int,
    ArtworkID int,
    FOREIGN KEY (userID) REFERENCES user(userID), 
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID));
    );
```

```sql
    CREATE TABLE Gallery (
    GalleryID int primary key,
    name varchar,
    Description text,
    location varchar,
    curator varchar,
    openingHours decimal,
    ArtistID int,
    FOREIGN KEY (artistID) REFERENCES artist(artistID), 
    );
```

```sql
    CREATE TABLE Artwork_Gallery (
    ArtworkID int,
    GalleryID int,
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID));
    );
```



