#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from face64.face64encoder import face64encoder 

class TestFace64(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestFace64, self).__init__(*args, **kwargs)

        #Some known values we can test with.
        self.TheMagicOffset = 129333
        self.decodedString = 'this is a test'
        self.encodedString = '🦙🥼🦝🦥🦘🦮🥷🦥🦘🦮🥷🦝🥾🥽🦇🦡🦘🥨🦆🥲'

    def test_encode(self):
        face64 = face64encoder(self.TheMagicOffset)
        result = face64.encode(self.decodedString)
        self.assertEqual(result, self.encodedString, "Encoding did not match the expected result")

    def test_decode(self):
        face64 = face64encoder(self.TheMagicOffset)
        result = face64.decode(self.encodedString)
        self.assertEqual(result, self.decodedString, "Decoding did not match the expected result")

    def test_encode_decode(self):
        #Test full encoding/decoding process with a different offset 
        face64 = face64encoder(self.TheMagicOffset+10)
        start = self.decodedString
        result = face64.encode(start)
        end = face64.decode(result)
        self.assertEqual(start, end, "Encode and Decode test did not match the expected result")

    def test_encode_decode_emoji(self):
        #Test full encoding/decoding process with a different offset 
        face64 = face64encoder(self.TheMagicOffset+10)
        start = self.decodedString
        print(start)
        result = face64.base64_to_emoji(start)
        print(result)
        end = face64.emoji_to_base64(result)
        self.assertEqual(start, end, "Encode and Decode test did not match the expected result")
        print(end)


if __name__ == '__main__':
    unittest.main()
