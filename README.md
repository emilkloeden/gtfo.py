# gtfo.py

GTFOBins is a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions.

gtfo.py provides a command line interface over the top of the raw data.

Find the original project at https://gtfobins.github.io

## Usage

```sh
python3 --function limited-suid {name}
```

It is also recommended to add the following aliases:
```sh
alias gtfo="python3 /path/to/gtfo.py"
alias suid="python3 /path/to/gtfo.py -f suid"
```
