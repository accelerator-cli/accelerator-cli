"""Tests for our `acc validate` subcommand."""


from subprocess import PIPE, Popen as popen
from unittest import TestCase


class TestHello(TestCase):
    def test_returns_descriptor_version(self):
        output = popen(['acc', 'validate'], stdout=PIPE).communicate()[0]
        self.assertTrue('1' in output)