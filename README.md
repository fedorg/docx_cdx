# docx_cdx
Read ChemDraw CDX and other formats embedded in DOCX files
Requirements:
 - Python 3
 - kaitaistruct 0.8
 - olefile 0.45
 - openbabel 2.3

Example:

```python
from docx_cdx.parse_mols_from_docx import read_mols_from_docx
mols = read_mols_from_docx('/home/user/file.docx')

for mol in mols:
    # will print MDL MOL strings of all the molecules in the docx file
    print(mol)
```
