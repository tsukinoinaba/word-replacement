# Word Replacement

This is a simple Python program to replace an arbitrary set of words in a body of text.

## Usage

Run the program using

```python
python regex.py
```

First, the program will prompt you to enter the text passage. Enter or paste the text into the terminal.

Then, the program will prompt you to supply a JSON file. This JSON file should contain a list of pairs, where the key is the word in the original text to be replaced, and the value is the new word to take its place. For example, see `pronouns.json` as an example, which is used to replace masculine pronouns (he/him/his) with feminine pronouns (she/her/hers). Note that the words are case-sensitive.

Words will only be replaced in whole, and not if they are a part of another word. For instance, `the` will not be converted to `tshe` using `pronouns.json`.
