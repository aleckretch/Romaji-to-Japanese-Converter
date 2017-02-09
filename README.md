# Romaji-to-Japanese-Converter
A Python script that converts Romaji to Hiragana and/or Katakana

## How to run

Download the convert.py file and run in shell using `python3 convert.py`. The default character set is the Hiragana. Use asterisks to switch between the Hiragana and Katakana, such as `watashi wa *amerikajin* desu`.

## Features

1. A solo `wa` is converted to the character associated with `ha` (`は` in Hiragana or `ハ` in Katakana)
2. Punctuation marks of `.`, `!`, and `?` are converted to the Japanese punctuation mark of `。`
3. The second `o` of `oo` is converted to the character associated with `u` (`う` in Hiragana or `ウ` in Katakana)
4. The second `e` of `ee` is converted to the character associated with `i` (`い` in Hiragana or `イ` in Katakana)
5. The first consonant of two consecutive same consonants (except for `n`) is converted to the long-sound character (`っ` in Hiragana or `ー` in Katakana)
