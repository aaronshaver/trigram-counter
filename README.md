# trigram-counter

Counts three-word phrases across STDIN or multiple text files

## Usage

### Requirements

Python 3.x installed

### Run the tests

    python -m unittest discover

### Run the app

...

## Design decisions 

Natural language processing can get complicated and I made some simplifying assumptions, such as:

1. Words like "Python's" will render as "pythons". You might think simply striping the
single quote is logical, but what if we were processing, say, a fantasy novel with character names like "Rah'olrth"?
In that case the punctuation is meaningful and intended by the author and arguably should be preserved. But on balance 
users probably will see and care about the more common cases of possessive nouns, etc.
