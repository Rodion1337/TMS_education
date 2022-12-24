-- DELETE FROM users WHERE user_id = 2;

"""Попытался удалить юзера, но почему-то не получается ни как"""


ALTER TABLE posts ADD CONSTRAINT post_author_id FOREIGN KEY(post_author_id) REFERENCES users(user_id) ON DELETE CASCADE;
DELETE FROM users WHERE user_id = 2;

FOREIGN KEY(post_author_id) REFERENCES users(user_id) ON DELETE SET NULL;
DELETE FROM users WHERE user_id = 2;
