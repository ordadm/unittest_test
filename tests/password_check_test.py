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
        self.assertEqual(password_check('sdfK-JH1ор'), f'пароль должен содержать только латиницу, цифры и символы {password_verify.passw.allowed_sign}')




if __name__ == '__main__':
    main()
