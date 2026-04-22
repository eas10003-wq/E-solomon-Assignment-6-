
PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Fantasy', 'fantasy-category.jpg'),
(2, 'Classics', 'classics-category.jpg'),
(3, 'Science Fiction', 'science-fiction-category.jpg'),
(4, 'Modern Bestsellers', 'modern-bestsellers-category.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Harry Potter and the Sorcerer''s Stone', 'J. K. Rowling', '9780590353427', 19.99, 'harry-potter-1.jpg', 1),
(2, 1, 'Harry Potter and the Chamber of Secrets', 'J. K. Rowling', '9780439064873', 20.99, 'harry-potter-2.jpg', 0),
(3, 1, 'The Hobbit', 'J. R. R. Tolkien', '9780547928227', 18.50, 'the-hobbit.jpg', 1),
(4, 2, 'Dream of the Red Chamber', 'Cao Xueqin', '9780140442939', 17.99, 'dream-of-the-red-chamber.jpg', 0),
(5, 2, 'Journey to the West', 'Wu Cheng''en', '9787119016634', 21.99, 'journey-to-the-west.jpg', 1),
(6, 2, 'Pride and Prejudice', 'Jane Austen', '9780141439518', 12.99, 'pride-and-prejudice.jpg', 0),
(7, 3, 'The Three-Body Problem', 'Liu Cixin', '9780765377067', 18.99, 'three-body-problem.jpg', 1),
(8, 3, 'The Dark Forest', 'Liu Cixin', '9780765386694', 19.99, 'the-dark-forest.jpg', 0),
(9, 4, 'The Little Prince', 'Antoine de Saint-Exupery', '9780156012195', 11.99, 'the-little-prince.jpg', 1),
(10, 4, 'To Live', 'Yu Hua', '9781400031863', 15.99, 'to-live.jpg', 1);