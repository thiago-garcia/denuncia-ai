'''
Módulo para expor as funções assertions do TestCase
'''
from django.test import TestCase


_dj_test_case = TestCase()

dj_assert_contains = _dj_test_case.assertContains
dj_assert_not_contains = _dj_test_case.assertNotContains
