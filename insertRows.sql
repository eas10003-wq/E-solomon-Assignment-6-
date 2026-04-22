
PRAGMA foreign_keys = ON;

INSERT INTO movie (movieId, categoryId, title, director, imdbId, price, image, watchNow) VALUES
(1, 1, 'The Notebook', 'Nick Cassavetes', 'tt0332280', 14.99, 'the-notebook.jpg', 1),
(2, 1, 'A Walk to Remember', 'Adam Shankman', 'tt0281358', 12.99, 'a-walk-to-remember.jpg', 0),
(3, 1, 'Crazy Rich Asians', 'Jon M. Chu', 'tt3104988', 16.50, 'crazy-rich-asians.jpg', 1),
(4, 1, '50 First Dates', 'Peter Segal', 'tt0343660', 13.99, '50-first-dates.jpg', 0),
(5, 1, 'Love Actually', 'Richard Curtis', 'tt0314331', 15.99, 'love-actually.jpg', 1),

(6, 2, 'The Bourne Identity', 'Doug Liman', 'tt0258463', 17.99, 'bourne-identity.jpg', 1),
(7, 2, 'The Bourne Supremacy', 'Paul Greengrass', 'tt0372183', 18.99, 'bourne-supremacy.jpg', 0),
(8, 2, 'Black Hawk Down', 'Ridley Scott', 'tt0265086', 16.99, 'black-hawk-down.jpg', 1),
(9, 2, 'Spider-Man', 'Sam Raimi', 'tt0145487', 15.50, 'spiderman-2002.jpg', 0),
(10, 2, 'The Fast and the Furious', 'Rob Cohen', 'tt0232500', 14.50, 'fast-and-furious-2001.jpg', 1);
