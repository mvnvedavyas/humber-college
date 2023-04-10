/********************************************************
* This script creates the database named my_guitar_shop 
*********************************************************/

-- create the tables for the database
CREATE TABLE categories_copy (
  category_id        INT            PRIMARY KEY   AUTO_INCREMENT,
  category_name      VARCHAR(255)   NOT NULL      UNIQUE
);

CREATE TABLE products_copy (
  product_id         INT            PRIMARY KEY   AUTO_INCREMENT,
  category_id        INT            NOT NULL,
  product_code       VARCHAR(10)    NOT NULL      UNIQUE,
  product_name       VARCHAR(255)   NOT NULL,
  description        TEXT           NOT NULL,
  list_price         DECIMAL(10,2)  NOT NULL,
  discount_percent   DECIMAL(10,2)  NOT NULL      DEFAULT 0.00,
  date_added         DATETIME                     DEFAULT NULL,
  CONSTRAINT products_fk_categories_copy
    FOREIGN KEY (category_id)
    REFERENCES categories_copy (category_id)
);

CREATE TABLE customers_copy (
  customer_id           INT            PRIMARY KEY   AUTO_INCREMENT,
  email_address         VARCHAR(255)   NOT NULL      UNIQUE,
  password              VARCHAR(60)    NOT NULL,
  first_name            VARCHAR(60)    NOT NULL,
  last_name             VARCHAR(60)    NOT NULL,
  shipping_address_id   INT                          DEFAULT NULL,
  billing_address_id    INT                          DEFAULT NULL
);

-- Insert data into the tables
INSERT INTO categories_copy (category_id, category_name) VALUES
(1, 'Guitars'),
(2, 'Basses'),
(3, 'Drums'), 
(4, 'Keyboards');

INSERT INTO products_copy (product_id, category_id, product_code, product_name, description, list_price, discount_percent, date_added) VALUES
(1, 1, 'strat', 'Fender Stratocaster', 'The Fender Stratocaster is the electric guitar design that changed the world. New features include a tinted neck, parchment pickguard and control knobs, and a ''70s-style logo. Includes select alder body, 21-fret maple neck with your choice of a rosewood or maple fretboard, 3 single-coil pickups, vintage-style tremolo, and die-cast tuning keys. This guitar features a thicker bridge block for increased sustain and a more stable point of contact with the strings. At this low price, why play anything but the real thing?\r\n\r\nFeatures:\r\n\r\n* New features:\r\n* Thicker bridge block\r\n* 3-ply parchment pick guard\r\n* Tinted neck', '699.00', '30.00', '2017-10-30 09:32:40'),
(2, 1, 'les_paul', 'Gibson Les Paul', 'This Les Paul guitar offers a carved top and humbucking pickups. It has a simple yet elegant design. Cutting-yet-rich tone?the hallmark of the Les Paul?pours out of the 490R and 498T Alnico II magnet humbucker pickups, which are mounted on a carved maple top with a mahogany back. The faded finish models are equipped with BurstBucker Pro pickups and a mahogany top. This guitar includes a Gibson hardshell case (Faded and satin finish models come with a gig bag) and a limited lifetime warranty.\r\n\r\nFeatures:\r\n\r\n* Carved maple top and mahogany back (Mahogany top on faded finish models)\r\n* Mahogany neck, ''59 Rounded Les Paul\r\n* Rosewood fingerboard (Ebony on Alpine white)\r\n* Tune-O-Matic bridge with stopbar\r\n* Chrome or gold hardware\r\n* 490R and 498T Alnico 2 magnet humbucker pickups (BurstBucker Pro on faded finish models)\r\n* 2 volume and 2 tone knobs, 3-way switch', '1199.00', '30.00', '2017-12-05 16:33:13'),
(3, 1, 'sg', 'Gibson SG', 'This Gibson SG electric guitar takes the best of the ''62 original and adds the longer and sturdier neck joint of the late ''60s models. All the classic features you''d expect from a historic guitar. Hot humbuckers go from rich, sweet lightning to warm, tingling waves of sustain. A silky-fast rosewood fretboard plays like a dream. The original-style beveled mahogany body looks like a million bucks. Plus, Tune-O-Matic bridge and chrome hardware. Limited lifetime warranty. Includes hardshell case.\r\n\r\nFeatures:\r\n\r\n* Double-cutaway beveled mahogany body\r\n* Set mahogany neck with rounded ''50s profile\r\n* Bound rosewood fingerboard with trapezoid inlays\r\n* Tune-O-Matic bridge with stopbar tailpiece\r\n* Chrome hardware\r\n* 490R humbucker in the neck position\r\n* 498T humbucker in the bridge position\r\n* 2 volume knobs, 2 tone knobs, 3-way switch\r\n* 24-3/4" scale', '2517.00', '52.00', '2018-02-04 11:04:31'),
(4, 1, 'fg700s', 'Yamaha FG700S', 'The Yamaha FG700S solid top acoustic guitar has the ultimate combo for projection and pure tone. The expertly braced spruce top speaks clearly atop the rosewood body. It has a rosewood fingerboard, rosewood bridge, die-cast tuners, body and neck binding, and a tortoise pickguard.\r\n\r\nFeatures:\r\n\r\n* Solid Sitka spruce top\r\n* Rosewood back and sides\r\n* Rosewood fingerboard\r\n* Rosewood bridge\r\n* White/black body and neck binding\r\n* Die-cast tuners\r\n* Tortoise pickguard\r\n* Limited lifetime warranty', '489.99', '38.00', '2018-06-01 11:12:59'),
(5, 1, 'washburn', 'Washburn D10S', 'The Washburn D10S acoustic guitar is superbly crafted with a solid spruce top and mahogany back and sides for exceptional tone. A mahogany neck and rosewood fingerboard make fretwork a breeze, while chrome Grover-style machines keep you perfectly tuned. The Washburn D10S comes with a limited lifetime warranty.\r\n\r\nFeatures:\r\n\r\n    * Spruce top\r\n    * Mahogany back, sides\r\n    * Mahogany neck Rosewood fingerboard\r\n    * Chrome Grover-style machines', '299.00', '0.00', '2018-07-30 13:58:35'),
(6, 1, 'rodriguez', 'Rodriguez Caballero 11', 'Featuring a carefully chosen, solid Canadian cedar top and laminated bubinga back and sides, the Caballero 11 classical guitar is a beauty to behold and play. The headstock and fretboard are of Indian rosewood. Nickel-plated tuners and Silver-plated frets are installed to last a lifetime. The body binding and wood rosette are exquisite.\r\n\r\nThe Rodriguez Guitar is hand crafted and glued to create precise balances. From the invisible careful sanding, even inside the body, that ensures the finished instrument''s purity of tone, to the beautifully unique rosette inlays around the soundhole and on the back of the neck, each guitar is a credit to its luthier and worthy of being handed down from one generation to another.\r\n\r\nThe tone, resonance and beauty of fine guitars are all dependent upon the wood from which they are made. The wood used in the construction of Rodriguez guitars is carefully chosen and aged to guarantee the highest quality. No wood is purchased before the tree has been cut down, and at least 2 years must elapse before the tree is turned into lumber. The wood has to be well cut from the log. The grain must be close and absolutely vertical. The shop is totally free from humidity.', '415.00', '39.00', '2018-07-30 14:12:41'),
(7, 2, 'precision', 'Fender Precision', 'The Fender Precision bass guitar delivers the sound, look, and feel today''s bass players demand. This bass features that classic P-Bass old-school design. Each Precision bass boasts contemporary features and refinements that make it an excellent value. Featuring an alder body and a split single-coil pickup, this classic electric bass guitar lives up to its Fender legacy.\r\n\r\nFeatures:\r\n\r\n* Body: Alder\r\n* Neck: Maple, modern C shape, tinted satin urethane finish\r\n* Fingerboard: Rosewood or maple (depending on color)\r\n* 9-1/2" Radius (241 mm)\r\n* Frets: 20 Medium-jumbo frets\r\n* Pickups: 1 Standard Precision Bass split single-coil pickup (Mid)\r\n* Controls: Volume, Tone\r\n* Bridge: Standard vintage style with single groove saddles\r\n* Machine heads: Standard\r\n* Hardware: Chrome\r\n* Pickguard: 3-Ply Parchment\r\n* Scale Length: 34" (864 mm)\r\n* Width at Nut: 1-5/8" (41.3 mm)\r\n* Unique features: Knurled chrome P Bass knobs, Fender transition logo', '799.99', '30.00', '2018-06-01 11:29:35'),
(8, 2, 'hofner', 'Hofner Icon', 'With authentic details inspired by the original, the Hofner Icon makes the legendary violin bass available to the rest of us. Don''t get the idea that this a just a "nowhere man" look-alike. This quality instrument features a real spruce top and beautiful flamed maple back and sides. The semi-hollow body and set neck will give you the warm, round tone you expect from the violin bass.\r\n\r\nFeatures:\r\n\r\n* Authentic details inspired by the original\r\n* Spruce top\r\n* Flamed maple back and sides\r\n* Set neck\r\n* Rosewood fretboard\r\n* 30" scale\r\n* 22 frets\r\n* Dot inlay', '499.99', '25.00', '2018-07-30 14:18:33'),
(9, 3, 'ludwig', 'Ludwig 5-piece Drum Set with Cymbals', 'This product includes a Ludwig 5-piece drum set and a Zildjian starter cymbal pack.\r\n\r\nWith the Ludwig drum set, you get famous Ludwig quality. This set features a bass drum, two toms, a floor tom, and a snare?each with a wrapped finish. Drum hardware includes LA214FP bass pedal, snare stand, cymbal stand, hi-hat stand, and a throne.\r\n\r\nWith the Zildjian cymbal pack, you get a 14" crash, 18" crash/ride, and a pair of 13" hi-hats. Sound grooves and round hammer strikes in a simple circular pattern on the top surface of these cymbals magnify the basic sound of the distinctive alloy.\r\n\r\nFeatures:\r\n\r\n* Famous Ludwig quality\r\n* Wrapped finishes\r\n* 22" x 16" kick drum\r\n* 12" x 10" and 13" x 11" toms\r\n* 16" x 16" floor tom\r\n* 14" x 6-1/2" snare drum kick pedal\r\n* Snare stand\r\n* Straight cymbal stand hi-hat stand\r\n* FREE throne', '699.99', '30.00', '2018-07-30 12:46:40'),
(10, 3, 'tama', 'Tama 5-Piece Drum Set with Cymbals', 'The Tama 5-piece Drum Set is the most affordable Tama drum kit ever to incorporate so many high-end features.\r\n\r\nWith over 40 years of experience, Tama knows what drummers really want. Which is why, no matter how long you''ve been playing the drums, no matter what budget you have to work with, Tama has the set you need, want, and can afford. Every aspect of the modern drum kit was exhaustively examined and reexamined and then improved before it was accepted as part of the Tama design. Which is why, if you start playing Tama now as a beginner, you''ll still enjoy playing it when you''ve achieved pro-status. That''s how good these groundbreaking new drums are.\r\n\r\nOnly Tama comes with a complete set of genuine Meinl HCS cymbals. These high-quality brass cymbals are made in Germany and are sonically matched so they sound great together. They are even lathed for a more refined tonal character. The set includes 14" hi-hats, 16" crash cymbal, and a 20" ride cymbal.\r\n\r\nFeatures:\r\n\r\n* 100% poplar 6-ply/7.5mm shells\r\n* Precise bearing edges\r\n* 100% glued finishes\r\n* Original small lugs\r\n* Drum heads\r\n* Accu-tune bass drum hoops\r\n* Spur brackets\r\n* Tom holder\r\n* Tom brackets', '799.99', '15.00', '2018-07-30 13:14:15');

INSERT INTO customers_copy (customer_id, email_address, password, first_name, last_name, shipping_address_id, billing_address_id) VALUES
(1, 'allan.sherwood@yahoo.com', '650215acec746f0e32bdfff387439eefc1358737', 'Allan', 'Sherwood', 1, 2),
(2, 'barryz@gmail.com', '3f563468d42a448cb1e56924529f6e7bbe529cc7', 'Barry', 'Zimmer', 3, 3),
(3, 'christineb@solarone.com', 'ed19f5c0833094026a2f1e9e6f08a35d26037066', 'Christine', 'Brown', 4, 4),
(4, 'david.goldstein@hotmail.com', 'b444ac06613fc8d63795be9ad0beaf55011936ac', 'David', 'Goldstein', 5, 6),
(5, 'erinv@gmail.com', '109f4b3c50d7b0df729d299bc6f8e9ef9066971f', 'Erin', 'Valentino', 7, 7),
(6, 'frankwilson@sbcglobal.net', '3ebfa301dc59196f18593c45e519287a23297589', 'Frank Lee', 'Wilson', 8, 8),
(7, 'gary_hernandez@yahoo.com', '1ff2b3704aede04eecb51e50ca698efd50a1379b', 'Gary', 'Hernandez', 9, 10),
(8, 'heatheresway@mac.com', '911ddc3b8f9a13b5499b6bc4638a2b4f3f68bf23', 'Heather', 'Esway', 11, 12);

