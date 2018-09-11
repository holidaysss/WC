from unittest import TestCase
from wc import main

__author__ = 'MacRae'
__project__ = 'WcTest'


class TestWc(TestCase):
    def test(self):
        opts = [('-l', 'xt')]
        main(opts)