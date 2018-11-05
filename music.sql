CREATE TABLE Artist 

(

    Artist_Id int PRIMARY KEY,

    Artist_Name  varchar NOT NULL

);

   

        

CREATE TABLE Albums

(

    album_id int PRIMARY KEY,

    artist_id int NOT NULL REFERENCES Artist(artist_id),

    album_name varchar NOT NULL

);

    



CREATE TABLE Songs

(

    song_id int PRIMARY KEY,

    song_name varchar NOT NULL,

    album_id int NOT NULL REFERENCES Albums(album_id),

    track_number int, 

    Duration int 

    );
