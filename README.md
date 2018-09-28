# trigram-counter

Counts three-word phrases across STDIN or multiple text files

## Requirements

Python 3.x installed

## Usage

### Run the tests

    python -m unittest discover

### Get input from STDIN

    cat file.txt | python counter.py

### Get input from files

    python counter.py file1.txt file2.txt
    
## Design decisions 

Natural language processing can get complicated and I made some simplifying assumptions, such as:

1. Words like "Python's" will render as "pythons". You might think simply stripping the
single quote is logical, but what if we were processing, say, a fantasy novel with character names like "Rah'orth"?
In that case, the punctuation is meaningful and intended by the author and arguably should be preserved. But on balance 
users probably will see and care about the more common cases of possessive nouns, etc.
