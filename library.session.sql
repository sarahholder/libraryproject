INSERT INTO libraryapp_library
(title, address)
VALUES
('Bellview Library', '500 Main Street');

INSERT INTO libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
VALUES
('Lamb', '59359409490', 2004, 1, 'Christopher Moore', 1);

INSERT INTO libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
VALUES
('Taiko', '04275747474873', 2001, 1, 'Eiji Yoshikawa', 1);

INSERT INTO libraryapp_book
(title, isbn, year_published, location_id, author, librarian_id)
VALUES
('Outlander', '8582475822', 2013, 1, 'Diana Gabaldon', 2);

SELECT * FROM auth_user;

SELECT
	li.id,
	li.title,
	li.address,
	b.id book_id,
	b.title book_title,
	b.author,
	b.year_published,
	b.isbn,
	b.location_id
FROM libraryapp_library li
JOIN libraryapp_book b ON li.id = b.location_id


