PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Romance', 'romance.jpg'),
(2, 'Action', 'action.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'The Notebook', 'Nicholas Sparks', '9780446605236', 14.99, 'the-notebook.jpg', 1),
(2, 1, 'A Walk to Remember', 'Nicholas Sparks', '9780446693806', 12.99, 'a-walk-to-remember.jpg', 0),
(3, 1, 'Crazy Rich Asians', 'Kevin Kwan', '9780307588371', 16.50, 'crazy-rich-asians.jpg', 1),
(4, 1, '50 First Dates', 'Unknown Author', '9780000000001', 13.99, '50-first-dates.jpg', 0),
(5, 1, 'Love Actually', 'Richard Curtis', '9780000000002', 15.99, 'love-actually.jpg', 1),

(6, 2, 'The Bourne Identity', 'Robert Ludlum', '9780553593549', 17.99, 'bourne-identity.jpg', 1),
(7, 2, 'The Bourne Supremacy', 'Robert Ludlum', '9780553579253', 18.99, 'bourne-supremacy.jpg', 0),
(8, 2, 'Black Hawk Down', 'Mark Bowden', '9780802143389', 16.99, 'black-hawk-down.jpg', 1),
(9, 2, 'Spider-Man', 'Stan Lee', '9780785131799', 15.50, 'spiderman-2002.jpg', 0),
(10, 2, 'The Fast and the Furious', 'Ken Li', '9780000000003', 14.50, 'fast-and-furious-2001.jpg', 1);
