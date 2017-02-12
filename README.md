# Romaji-to-Japanese-Converter
A Python script that converts Romaji to Hiragana and/or Katakana

## Usage

Import convert.py into a Python file and call the function `romajiToJapanese()` with your Romaji string as the input. The default character set is the Hiragana. Use asterisks to switch between the Hiragana and Katakana.

## Example usage

Input:
```python3
print(convert.romajiToJapanese("Watashi wa *amerika*jin desu."))
```
Output:
```
わたし は アメリカじん です。
```

## Shell playground

Run `python3 input_convert.py` to manually input Romaji strings for instant conversion.

## Features

1. A solo `wa` is converted to the character associated with `ha` (`は` in Hiragana or `ハ` in Katakana)
2. Punctuation marks of `.`, `!`, and `?` are converted to the Japanese punctuation mark of `。`
3. The second `o` of `oo` is converted to the character associated with `u` for Hiragana (`う`)
4. The second `e` of `ee` is converted to the character associated with `i` for Hiragana (`い`)
5. The first consonant of two consecutive same consonants (except for `n`) is converted to the sakuon character for Hiragana and Katakana (`っ` in Hiragana or `ッ` in Katakana)
6. The second of consecutive same vowels is converted to the long-sound character for Katakana (`ー`)
