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
It is about a person who hands their days to an agent in small
surrenders, finds that a perfectly run life has quietly left them
out of it, and takes their choices back - clumsily, and on purpose.
