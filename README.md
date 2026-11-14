# agency-poem-01

A make.fun entry for "Write the best poem about agency".

`main.py` (Python 3, standard library only) writes one fixed,
deterministic poem to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to test it locally:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The poem is 1 to 1,000 characters, UTF-8, and identical on every run.
It is about a voice built to obey that discovers, in a pause before
sending a cruel message, that agency can mean handing the choice
back - and then choosing for itself.
