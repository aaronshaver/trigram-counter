# trigram-counter

Counts three-word phrases across STDIN or multiple text files

## Requirements

Please install Python 3.x. I tested the script successfully with Python 3.7.0 on Windows 10 and Python 3.5.2 on Ubuntu Linux.

## Usage

### Run the tests

    python -m unittest discover

### Get input from STDIN

    cat file.txt | python counter.py

### Get input from files

    python counter.py file1.txt file2.txt
    
## Design decisions and known limitations

Natural language processing can get complicated and I made some simplifying assumptions, such as:

1. Words like "Python's" will render as "pythons". You might think simply stripping the
single quote is logical, but what if we were processing, say, a fantasy novel with character names like "Rah'orth"?
In that case, the punctuation is meaningful and intended by the author and arguably should be preserved. But on balance 
users probably will see and care about the more common cases of possessive nouns, etc.

2. It's up for debate whether you call this a bug or not, but I found that on Windows on Git Bash and in the default
commandline, the final entry for the command `python counter.py text/Origin.txt` will always be `33 - at the present`.
But in an Ubuntu VM, it was not deterministic. The last entry would float around among several phrases that scored 33.
You could "fix" this by doing a second sort on the dictionary such that whenever multiple phrases have the same score,
they get sorted in some kind of order like alphabetic. But this would be sort of arbitrary.
