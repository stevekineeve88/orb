from modules.Util.db_connection import DBConnection
from modules.Util.result import Result


class DictionaryRepo:
    def __init__(self, **kwargs):
        self.db_connection: DBConnection = kwargs.get("db_connection") or DBConnection()

    def insert_word(self, word: str) -> Result:
        result = Result()
        cursor = self.db_connection.get_cursor()
        try:
            cursor.execute(
                'INSERT INTO "Word_Words" '
                '(word, category) '
                'VALUES (%(word)s, %(category)s) RETURNING id',
                {
                    "word": word,
                    "category": word[0]
                }
            )
            word_id = cursor.fetchone()["id"]
            self.db_connection.get_connection().commit()
            result.set_insert_id(word_id)
        except Exception as e:
            result.set_message(str(e))
            result.set_status(False)
        finally:
            self.db_connection.get_connection().rollback()
            cursor.close()
        return result

    def load_word(self, word: str) -> Result:
        result = Result()
        cursor = self.db_connection.get_cursor()
        try:
            cursor.execute(
                'SELECT '
                '"Word_Words".id, '
                '"Word_Words".word, '
                '"Word_Words".category '
                'FROM "Word_Words"'
                'WHERE "Word_Words".word = %(word)s',
                {
                    "word": word
                }
            )
            data = cursor.fetchall()
            result.set_data(data)
        except Exception as e:
            result.set_message(str(e))
            result.set_status(False)
        finally:
            cursor.close()
        return result

    def load_words(self, characters: str, word_length: int, limit: int, offset: int, **kwargs):
        character_search = {}
        for character in characters:
            if character not in character_search.keys():
                character_search[character] = f'%{character}%'
                continue
            character_search[character] += f'%{character}%'
        result = Result()
        cursor = self.db_connection.get_cursor()
        values = {
            word_length: word_length
        }
        try:
            cursor.execute(
                f"""
                    SELECT
                        "Word_Words".id,
                        "Word_Words".word,
                        "Word_Words".category
                    FROM "Word_Words"
                    WHERE LENGTH("Word_Words".word) = %(word_length)s
                    AND {self.__build_character_search()}
                """
            )
            data = cursor.fetchall()
            result.set_data(data)
        except Exception as e:
            result.set_message(str(e))
            result.set_status(False)
        finally:
            cursor.close()
        return result

    @classmethod
    def __build_character_search(cls, characters: str) -> str:
        character_search = {}
        for character in characters:
            if character not in character_search.keys():
                character_search[character] = f'%{character}%'
                continue
            character_search[character] += f'%{character}%'
        character_like_conditions = []
        for key, value in character_search.items():
            character_like_conditions.append(f'"Word_Words".word LIKE {value}')
        return " OR ".join(character_like_conditions)
