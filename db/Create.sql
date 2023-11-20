CREATE TABLE IF NOT EXISTS items
             (
                          _id          INTEGER NOT NULL AUTO_INCREMENT,
                          description VARCHAR(240) NOT NULL,
                          name        VARCHAR(40) NOT NULL,
                          price       FLOAT NOT NULL,
                          PRIMARY KEY (_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
