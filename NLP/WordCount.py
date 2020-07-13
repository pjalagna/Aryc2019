"""
file wordCount.py
pja 07/11/2020

"""
"""
main(doc)
init
till eof
-- get word from doc
--- wdi = clean(wd)
--- debWU(wd)
--

clean(wd)
-- replace !@?,:; with null
-- trim
-- ==> wd
;

debWU(wd)
-- writeUnique(wd,1) to wds
--- on error
---- read(wd->ctr)
------ writeUnique(wd,ctr+1)
;


init
fioClass(doc)
open wdsdb.db
if not exists wds((wd)ctr)

"""