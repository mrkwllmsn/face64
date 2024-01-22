#!/usr/bin/env python3
# -*- coding: utf-8 -*-
### face64 will base64 encode data as emojis. It's bigger and friendlier, but also dumber
### By MarkW2024

import base64

class face64encoder:
    def __init__(self, theMagicOffset=129333):
        self.TheMagicOffset = theMagicOffset
        self.base64_to_emoji_mapping = {
            'A': '🥺', 'B': '😊', 'C': '😂', 'D': '😍', 'E': '😎', 'F': '🥳', 'G': '🤩', 'H': '😜', 'I': '😇', 'J': '😏',
            'K': '😌', 'L': '😀', 'M': '😃', 'N': '😄', 'O': '😅', 'P': '😆', 'Q': '😉', 'R': '😋', 'S': '😎', 'T': '😍',
            'U': '😘', 'V': '😗', 'W': '😙', 'X': '😚', 'Y': '☺️', 'Z': '🙂',
            '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣',
        }

    def encode(self, *args):
        data = ' '.join(args)
        encoded_bytes = base64.b64encode(data.encode('utf-8'))
        b64 = encoded_bytes.decode('utf-8')
        faced = ''
        for x in b64:
          for char in x:
              unicode_code_point = ord(char)
              finalord = unicode_code_point + self.TheMagicOffset
              character = chr(finalord)
              faced = faced + character
        return faced

    def decode(self, *args):
        data = ' '.join(args)
        decoded = ''
        for x in data:
          for char in x:
              unicode_code_point = ord(char)
              decoded_char = unicode_code_point - self.TheMagicOffset
              decoded = decoded + chr(decoded_char)
        decoded_bytes = base64.b64decode(decoded)
        face_decoded_string = decoded_bytes.decode('utf-8')
        return face_decoded_string

    def base64_to_emoji(self, *args):
        input_string = ' '.join(args)
        translated_string = ''.join(self.base64_to_emoji_mapping.get(char, char) for char in input_string)
        return translated_string

    def emoji_to_base64(self, *args):
        input_string = ''.join(args)
        emoji_to_base64_mapping = {v: k for k, v in self.base64_to_emoji_mapping.items()}
        translated_string = ''.join(emoji_to_base64_mapping.get(char, char) for char in input_string)
        return translated_string


