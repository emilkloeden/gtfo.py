# gtfo.py

GTFOBins is a curated list of Unix binaries that can be exploited by an attacker to bypass local sec$

gtfo.py provides a command line interface over the top of the raw data.

Find the original project at https://gtfobins.github.io

## Installation
Let's be honest. I'm never going to jump through the hoops to get this on PyPI. Just git clone it.

## Usage

```sh
python3 --function limited-suid {name}
```

List all functions for a binary:

![alt text](https://github.com/emilkloeden/gtfo.py/raw/master/resources/basic.gif "python3 /path/to/gtfo.py cat")

Filter for a specific function:

![alt text](https://github.com/emilkloeden/gtfo.py/raw/master/resources/suid.gif "python3 /path/to/gtfo.py -f suid cat")

It is also recommended to add the following aliases:
```sh
alias gtfo="python3 /path/to/gtfo.py"
alias suid="python3 /path/to/gtfo.py -f suid"
```

