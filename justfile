set shell := ["sh", "-c"]
set windows-shell := ["powershell", "-c"]

@_default:
	just --list

to_jupyter arg:
	python scripts/to_jupyter.py {{arg}}

to_ocpvscode arg:
	just

from_ocpvscode arg:
	just

from_jupyter arg:
	just






