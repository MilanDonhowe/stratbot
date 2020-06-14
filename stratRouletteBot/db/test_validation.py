# Unit Tests for input validation

import unittest
import asyncio
from stratsAPI import valid_map, valid_side
from discord.ext.commands import BadArgument

class TestCommandValidation(unittest.TestCase):


    def get_async_result(self, func, arg, loop):
        result = loop.run_until_complete(func(arg))
        return result

    def test_valid_side(self):
        loop = asyncio.get_event_loop()
        self.assertEqual(self.get_async_result(valid_side, 't', loop), "T")
        self.assertEqual(self.get_async_result(valid_side, 'ct', loop), "CT")
        self.assertRaises(BadArgument, self.get_async_result, valid_side, 'god guys', loop)
        loop.close()

    def test_valid_map(self):
        pass


if __name__ == "__main__":
    unittest.main()