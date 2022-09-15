from unittest import TestCase, main

import password_verify.passw
from password_verify.passw import password_check


class PasswordCheckTest(TestCase):
    def test_len(self):
        self.assertEqual(password_check('sdffdff'), 'пароль слишком короткий')
        self.assertEqual(password_check('1234567'), 'пароль слишком короткий')
        self.assertEqual(password_check('ораjk-1'), 'пароль слишком короткий')

    def test_allowed_sign(self):
        self.assertEqual(password_check('jhjhshjh'),
                         f'пароль должен содержать хотя бы один из символов {password_verify.passw.allowed_sign}')
        self.assertEqual(password_check('123456788'),
                         f'пароль должен содержать хотя бы один из символов {password_verify.passw.allowed_sign}')

    def test_ukrokirilica(self):
        self.assertEqual(password_check('sdfK-JH1ор'),
                         f'пароль должен содержать только латиницу, цифры и символы {password_verify.passw.allowed_sign}')

    def test_lower(self):
        self.assertEqual(password_check('KJHJH-JHJH'), 'пароль должен содержать хотя бы одну строчную букву')

    def test_upper(self):
        self.assertEqual(password_check('iuiou-kjhjh'), 'пароль должен содержать хотя бы одну загланую букву')

    def test_digit(self):
        self.assertEqual(password_check('iuiou-kjJHHF'), 'пароль должен содержать хотя бы одну цифру')

    def test_godno(self):
        self.assertEqual(password_check('iuid12ou-kjJHHF'),
                         'поздравляем! пароль соответствует всем требованиям безопасности')


if __name__ == '__main__':
    main()
