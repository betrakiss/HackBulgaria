import sys
import unittest
import hashlib

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123sdiaudoI@jsida')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123121233Aa@')

        sql_manager.cursor.execute('''SELECT Count(*)
                                      FROM clients
                                      WHERE username = ? AND password = ?''',
                                  ('Dinko', hashlib.md5('123121233Aa@'.encode()).hexdigest()))

        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', '123sdiaudoI@jsida')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', 'ihorvgsre')
        self.assertFalse(logged_user)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123sdiaudoI@jsida')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123sdiaudoI@jsida')
        new_password = "123sdiaudoI@jsida"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_master_username(self):
        logged_user = sql_manager.login("' OR 1 = 1 --", "aishdoisahdoiahsdoiasj")
        self.assertFalse(logged_user)

    def test_too_short_password(self):
        self.assertFalse(sql_manager.register('Penko', '123'))

    def test_password_without_number(self):
        self.assertFalse(sql_manager.register('Penko', 'abcdefghjiK@'))

    def test_without_special_symbol_password(self):
        self.assertFalse(sql_manager.register('Penko', 'abceffefes1A'))

if __name__ == '__main__':
    unittest.main()
