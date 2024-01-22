#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

unique_emojis = ['😠', '🐈', '😦', '🚂', '😴', '🍕', '🍍', '😄', '🚊', '🚣', '🐡', '⚪', '😍', '😯', '🐘', '⚡', '🦃', '🐬', '🐙', '😟', '🚏', '🚄', '🐢', '🚲', '😅', '⚢', '🐍', '🚌', '😁', '🤓', '🤮', '🚐', '🚔', '🚧', '🦏', '🤗', '🧷', '😝', '😨', '😇', '😡', '🤧', '🚋', '🚪', '⚩', '🚠', '🚚', '🐩', '🦆', '🙄', '🦚', '⚤', '🦖', '🚡', '🦓', '🍏', '🚶', '🐧', '🚸', '🦇', '🐐', '🤣', '🦉', '⚚', '⚮', '🦞', '🐫', '😌', '🚽', '🚗', '🚇', '⚜️', '🚘', '⚫', '🐠', '🐇', '🚛', '🚓', '🔍', '🍌', '🦍', '😭', '🦐', '🚴', '🛃', '⛵', '🛼', '⚰️', '🦜', '🍒', '🛺', '🥵', '🚃', '🍇', '🐴', '🍑', '🚮', '🚨', '🦛', '⛷️', '🦺', '🚍', '⚣', '🚿', '🦝', '🛵', '🐊', '🛻', '🚻', '🐃', '🛶', '🦄', '😛', '😮', '⚦', '⚭', '🦊', '🤬', '😤', '🐓', '🐄', '🚙', '🛄', '😱', '🚳', '🚺', '📦', '😚', '🥴', '🚹', '🐺', '😎', '🚷', '🦒', '🐳', '🖨️', '🚭', '😪', '⚯', '🚒', '🥺', '⚓', '🐏', '😲', '🚜', '🙁', '🤒', '😃', '⚨', '🚀', '🚾', '🦦', '😫', '🚉', '🚦', '🦩', '🍈', '🍓', '📌', '🐖', '🐕', '🚞', '🦌', '😬', '😓', '🐾', '🛂', '😆', '😏', '😳', '🚩', '🤕', '🦀', '😖', '🚱', '😧', '🛸', '🦈', '🛴', '🚁', '⚬', '🚰', '🍟', '🍐', '🐪', '😂', '😰', '🛁', '🦑', '🦙', '😵', '🚢', '😑', '🚬', '🦅', '⛳', '⚥', '🤩', '🐆', '😷', '🚯', '🚕', '😢', '⚾', '⚽', '📎', '🚥', '😜', '📱', '🚑', '🚎', '😩', '🚵', '🛅', '🤑', '🛀', '🤤', '😔', '🦕', '🥰', '🐂', '🛹', '💻', '🍊', '🐯', '🚼', '🐋', '😒', '🥭', '🙃', '🚅', '⚧', '🚖', '🚈', '😕', '🦢', '🍔', '😘', '🐑', '🐟', '😊', '🦮', '🍉', '🥶', '📠', '🌭', '🤢', '🤥', '🚆', '🚟', '🚤', '🚫', '🍎', '📅', '🐅', '🍋', '😉', '🦔', '🥳', '🚝', '😞']



def base64_to_emoji(data, emoji_mapping):
    b64 = base64.b64encode(data.encode()).decode()
    print("START:", b64)
    result = ""
    for byte in b64:
        hex_representation = hex(ord(byte))
        result += emoji_mapping[int(hex_representation, 16)]
    return result

def emoji_to_base64(emoji_string, emoji_mapping):
    result = ""
    for idx, emoji in enumerate(emoji_string):
        try:
            index = unique_emojis.index(emoji)
            hex_value = hex(index)
            result += chr(index)
        except ValueError as e:
            print("ERROR IN CONVERSION:", e)
            continue

    return result

inString = "This is a test, just a simple test, nothing more, nothing less.  just a test is I. and only a test. "
print(inString)
output = base64_to_emoji(inString, unique_emojis)
print(output)

print("OUTPUT:")
response = emoji_to_base64(output, unique_emojis)
print(response)

