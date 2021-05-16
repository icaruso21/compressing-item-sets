# compressing-item-sets

A suite of algorithms for finding interesting item sets in large databases by considering the item sets that *compress* the data best. Python implementations of the algorithms described in ["Item Sets That Compress"](http://www.cs.uu.nl/groups/ADA/pubs/2006/item_sets_that_compress-siebes,vreeken,vanleeuwen.pdf).

## Usage

`python main.py version filepath`

## Environment Setup

To create a new environment:

- `python3 -m venv env`
- `source env/bin/activate`

To install packages in an active environment:

- `pip install <package name>`

To save an environment:

- `pip freeze > requirements.txt`

To restore an environment:

- `pip install -r ./requirements.txt`

### Datasets used for testing
All datasets were taken from http://fimi.uantwerpen.be/data/. They can be found under the `data` folder of this repository (with the exception of `kosarak`, which is too large to add to the repository)

- `chess`
- `connect`
- `kosarak`
