def read_embeddings_from_docx(filename):
    from itertools import count
    from zipfile import ZipFile
    with ZipFile(filename) as myzip:
        names = myzip.namelist()
        for n in count(1):
            embpath = f"word/embeddings/oleObject{n}.bin"
            if embpath not in names:
                return
            with myzip.open(embpath) as myfile:
                emb = myfile.read()
                yield emb


def get_embedding_format(compobj):
    from struct import unpack
    b = bytes(compobj)
    start = 28
    ret = []
    for i in range(3):
        try:
            strl, = unpack('<I', b[start:start + 4])
            s, = unpack(f'{strl}s', b[start + 4:start + 4 + strl])
            start = start + 4 + strl
            ret.append(s[:-1])
        except:
            break
    return ret

def read_embedding_contents(emb, paths=None):
    if paths is None:
        paths = [['CONTENTS'], ['\x03PRINT']]
    import olefile
    def try_default(func, *args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            # print(e)
            pass
        return None

    def read(ole, fn):
        return ole.openstream(fn).read()

    ole, data, form = None, None, None
    try:
        ole = olefile.OleFileIO(emb)
        try:
            _form = get_embedding_format(read(ole, ['\x01CompObj']))
            form = _form[2]
        except:
            pass
        # print(ole.listdir())
        for p in paths:
            data = try_default(read, ole, p)
            if data is not None: break
        return (form, data)
    except Exception as e:
        import sys
        print('failed to unpack ole:', e, file=sys.stderr)
    finally:
        if ole: ole.close()
    return (None, None)


def read_objs_from_doc(filename, paths=None, mapper=None):
    if mapper is None:
        mapper = lambda form, obj: (form, obj)
    for ole in read_embeddings_from_docx(filename):
        if ole is None: continue
        form, obj = read_embedding_contents(ole, paths=paths)
        if obj is None:
            # print('empty', filename, form)
            continue
        # print(form, filename)
        try:
            _form, _obj = mapper(form, obj)
            if _obj is not None:
                yield (_form, _obj)
        except Exception as e:
            import sys
            print(filename, e, file=sys.stderr)
    return

