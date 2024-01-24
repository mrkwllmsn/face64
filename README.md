# Face64

## Bigger and Friendlier than base64.


🦋🥼🦝🦡🥾🥼🦡🦩🦎🦌🦙🦡🥾🥽🦇🦮🦎🦌🥪🦯🦗🥼🥻🥥🦗🥨🥿🦯🥾🥽🦙🦫🦘🦢🦨🦜🦏🦢🥮🦮🥾🥽🦇🦤🦏🦈🥷🦟🦗🥧🥪🦯🦙🥽🥿🥦🦎🥨🦆🦜🦘🥽🥿🦫🦏🥨🥿🦝🦗🦈🥩🦜🦆🦣🦋🥥🥾🥽🦇🦤🦏🦍🥿🦡🥩🦤🥸🦏🦘🦮🥷🥨🦎🦍🦠🦜🦙🥼🥮🦫🥾🥼🥦🥦🦎🥧🦜🦜🦖🦌🥪🦢🦗🥨🥿🦩🦎🦍🦇🦥🦗🥧🥩🦜🦙🥼🥭🦜🦏🥼🦋🦟🦗🥧🦇🦡🥾🥽🦇🦤🦏🦈🥷🦃🦎🦍🦇🦮🦖🦍🦜🦪🥾🥻🦡🦫🦙🦈🥷🦣🦏🦍🦆🦜🦙🦍🦃🦡🦏🥸🥷🥥🦗🦮🥷🦥🦙🥸🥩🦜🦈🦚🦀🥶🦥🦠🦠🦜🦏🥼🥮🦪🥩🦤🥸🦏🦙🥸🥷🦡🦙🦢🦋🦪🥾🥽🦃🦡🦏🦈🥷🥥🦖🥼🦊🦜🦎🥧🥮🦠🦏🦈🥩🦜🦆🦌🦭🦨🥾🥺🦠🦜🦘🥧🦋🦡🥾🥼🦡🦯🥾🥼🥿🦨🦗🥧🥪🦠🦏🦈🦬🦜🦎🦣🥿🥦🦗🦢🦋🥥🦙🥼🦊🦨🥾🥽🥿🦡🦏🥸🥦🦤🦏🦌🥻🦠🦁🦞🥷🥾🦏🦍🦠🦨🥾🥽🦡🦫🦙🦈🥷🥦🦖🦄🦀🥶🦥🦞🥷🥨🦎🦌🥪🥥🥾🥼🥺🦜🦏🥽🥿🦥🦗🦢🦨🥤


This script encodes data/text as face64, which is base64 that is then shifted up into the utf-8 smiley face range.
It's bigger than base64, which is already bigger than source, so you're not going to want to you use this for anything but fun.
But it is quite a site to behold!

It converts the base64, and then replaces the characters with emojis by using the ordinals, converting to utf-8 and adding an offset up into the smiley category.
Yes, that does mean it's big, but not compared to GTAV so get over it.

## Installation:
clone the repo, cd into the directory, run the python setup.py install script. It's set up for pip but isn't there yet.

```shell
git clone https://github.com/mrkwllmsn/face64
cd face64
python3 setup.py install
```

You should then get face64 available to you.

## Usage
You can pass your message to it as an argument (You don't need to quote it if you don't want to), or you can send it to stdin.

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

 --decode -d
     Decode an encoded string

--offset -f offset (number value, eg -f -100)
     Change the offset used by the encoder, this changes the pictures that appear. Some work better than others.

--smiley -s Smileys
    Make all the output smiley faces instead of the default face64 emojis which is more of a mix.


## Uninstall:
 Why tho? haha, ok fair enough.

```shell
pip uninstall face64
```

## TODO / LIMITATIONS
 You can't encode binary data with it yet, I intend to handle that soon. 
