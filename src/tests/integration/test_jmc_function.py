import unittest
import sys


sys.path.append('./src')  # noqa

from tests.utils import string_to_tree_dict
from jmc.test_compile import JMCPack


class TestVarOperation(unittest.TestCase):
    ...


class TestBoolFunction(unittest.TestCase):
    ...


class TestExecuteExcluded(unittest.TestCase):
    ...


class TestJMCCommand(unittest.TestCase):
    ...


class TestLoadOnce(unittest.TestCase):
    ...


class TestLoadOnly(unittest.TestCase):
    ...