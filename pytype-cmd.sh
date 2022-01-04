error_list="import-error,attribute-error,module-attr,not-callable,duplicate-keyword-argument,unsupported-operands,wrong-arg-types,name-error,pyi-error,wrong-arg-count,bad-return-type,invalid-annotation,not-indexable,wrong-keyword-args,annotation-type-mismatch,missing-parameter,not-writable,not-supported-yet,not-callable"
# python lib version causes name error
libname=Flask
libname=Django
#libname=Jinja2
#libname=Numpy
#libname=pytz
#libname=MarkupSafe
#libname=Werkzeug
#libname=pytest
pytype top-10/$libname/tmp/ -d $error_list -o pytype-res
