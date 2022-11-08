from by.parakhnevich.tgconverter.dao.DAO import DAO

from by.parakhnevich.tgconverter.model.CurrencyEnum import CurrencyEnum
class UserDAO(DAO):

    def __init__(self):
        self.conn_string = "host='localhost' dbname='tg_1' user='tg_1' password='tg_1'"

    def save_or_update(self, id, from_currency_enum, to_currency_enum):
        connection = self.create_connection()

        existing_one = self.find_by_id(id)
        if existing_one is None:
            connection.cursor().execute("insert into user_info (id, from_currency, to_currency) values ({0}, '{1}', '{2}')"
                                        .format(str(id), from_currency_enum.value, to_currency_enum.value))
        else:
            from_currency = from_currency_enum if from_currency_enum is not None else CurrencyEnum(existing_one[1])
            to_currency = to_currency_enum if to_currency_enum is not None else CurrencyEnum(existing_one[2])

            connection.cursor().execute("update user_info set from_currency='{0}', to_currency='{1}' where id={2}"
                                        .format(from_currency.value, to_currency.value, str(id)))


        connection.commit()
        connection.close()


    def find_by_id(self, id):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute('select * from user_info where id={0}'.format(str(id)))
        result = cursor.fetchone()
        connection.close()
        return result