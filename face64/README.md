#Face64

##Bigger and Friendlier than base64.

This script encodes data/text as face64, which is base64 that is then shifted up into the utf-8 smiley face range.
It's bigger than base64, which is already bigger than source, so you're not going to want to you use this for anything but fun.
But it is quote a site to behold.

It converts the base64, and then replaces the characters with emojis by using the ordinals and adding an offset up into the smiley category.

## Installation:
```shell
clone the repo, cd into the directory
git clone https://github.com/mrkwllmsn/face64
cd face64
python3 setup.py install
```

You should then get face64 available to you.

## Usage
You can pass your message to it as an argument, you send it to stdin.

```shell
$ face64 "Well isn't this a silly thing."
🦋🥧🦋🦨🦗🥸🥷🦥🦘🥧🥩🦣🦙🥸🥷🥥🦖🥼🦡🦯🥾🥼🥺🦜🦘🥧🦡🦨🦗🥽🦠🦜🦙🥼🦝🦥🦗🦢🦘🦪
```

```shell
$ echo "🦋🥧🦋🦨🦗🥸🥷🦥🦘🥧🥩🦣🦙🥸🥷🥥🦖🥼🦡🦯🥾🥼🥺🦜🦘🥧🦡🦨🦗🥽🦠🦜🦙🥼🦝🦥🦗🦢🦘🦪" | face64 -d
Well isn't this a silly thing.
```

## Options 
```shell
    -d decode - Decode an encoded string
    -f offset <optional> (number) - change the offset used by the encoder, this changes the pictures that appear. 
```