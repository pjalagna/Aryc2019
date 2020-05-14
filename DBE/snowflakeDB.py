"""
file snowflakeDB.py
pja 05/12/2020

crud flag    + aux flag               + CVFlag
====================================================
help /''     +                        +
create       + table                  + <known>
capture      + rid                    +
read / seek  + structure/table/
               record/col/keys        + name/[{limits}[c=v]]
update       + dups/not/add breaker   + [{limits}[c=v]]
delete       + table/record/col       + name/[{limits}[c=v]]
DONE
"""
import genn
def Do(crudFlag,auxFlag='',CVFlag=''):
    #crudFlag fan
    CF = crudFlag.upper()
    if (CF == 'HELP'):
        doHelp()
    elif (CF == 'CREATE'):
        createTable()
    else:
        doHelp()
    #endif cf fan

#
def createTable():
    sq1 = """
create table snowflake (
  rid string not null,
  v1 string null,
  v2 string null,
  v3 string null,
  v4 string null,
  v5 string null,
  v6 string null,
  primary_key(rid)
) ;
"""
    #if db  not open then open
    # do create
    # say ok
#
