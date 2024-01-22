# Face64

## Bigger and Friendlier than base64.

This script encodes data/text as face64, which is base64 that is then shifted up into the utf-8 smiley face range.
It's bigger than base64, which is already bigger than source, so you're not going to want to you use this for anything but fun.
But it is quote a site to behold.

It converts the base64, and then replaces the characters with emojis by using the ordinals and adding an offset up into the smiley category.

## Installation:
clone the repo, cd into the directory, run the python setup.py install script. It's set up for pip but isn't there yet, 

```shell
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

or you could...
```shell
$ echo "Well isn't this a silly thing." | face64 | face64 -d
Well isn't this a silly thing.
```

## Options

 -d decode

     Decode an encoded string

-f offset <optional> (number)

     Change the offset used by the encoder, this changes the pictures that appear.


## Uninstall:
 Why tho? haha, ok fair enough.

```shell
pip uninstall face64
```

## TODO / LIMITATIONS
 You can't encode binary data with it yet, I intend to handle that soon. 
