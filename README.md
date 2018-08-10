# docx_cdx
Read ChemDraw CDX and other formats embedded in DOCX files  

**Don't use this CDX parser**, it's unreliable. I have reimplemented it for fun, this is a 'note to self' repo.
Launch `obabel -i cdx 'file.cdx' -o sdf` instead, for the time being CDX functionality does not work with Python bindings, only binary obabel does the job.

Requirements:
 - Python 3
 - kaitaistruct 0.8
 - olefile 0.45
 - openbabel 2.3

See [`setup.sh`](setup.sh) for install commands.

Example:

```python
from docx_cdx.parse_mols_from_docx import read_mols_from_docx
mols = read_mols_from_docx('/home/user/file.docx')

for mol in mols:
    # will print MDL MOL strings of all the molecules in the docx file
    print(mol)
```
