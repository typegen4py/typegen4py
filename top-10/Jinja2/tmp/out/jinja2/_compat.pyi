import collections as abc
import marshal
import sys
from io import BytesIO as BytesIO, StringIO
from os import fspath as fspath
from typing import Any, Optional

PY2: Any
PYPY: Any
unichr = chr
range_type = range
text_type = str
string_types: Any
integer_types: Any
iterkeys: Any
itervalues: Any
iteritems: Any
NativeStringIO = StringIO

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...
ifilter = filter
imap = map
izip = zip
intern = sys.intern
implements_iterator: Any
implements_to_string: Any
encode_filename: Any
marshal_dump = marshal.dump
marshal_load = marshal.load

def with_metaclass(meta: Any, *bases: Any): ...
