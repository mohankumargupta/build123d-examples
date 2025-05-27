set shell := ["sh", "-c"]
set windows-shell := ["powershell", "-c"]

all arg:
	just to_jupyter {{ arg }}
	just to_ocpvscode {{ arg }}

to_jupyter arg:
	python scripts/to_jupyter.py {{arg}}

to_ocpvscode arg:
	just

from_ocpvscode arg:
	just

from_jupyter arg:
	just






