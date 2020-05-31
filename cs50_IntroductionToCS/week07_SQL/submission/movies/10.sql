SELECT p.name FROM people p
JOIN directors d ON d.person_id = p.id
JOIN ratings r ON r.movie_id = d.movie_id
WHERE r.rating >= "9.0";