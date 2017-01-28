'''
Functions to reflect over SQLAlchemy models
'''
from sqlalchemy.orm import class_mapper


class KeyNotFoundException(Exception):
    """Primary key not found exception"""


def public_vars(cls):
    return {k: v for k, v in vars(cls).items() if not k.startswith('_')}


def class_keys(cls):
    """This is a utility function to get the attribute names for
    the primary keys of a class

    # >>> class_keys(Deal)
    # >>> ('dealer_code', 'deal_jacket_id', 'deal_id')
    """
    primary_keys = []
    for name, attr in public_vars(cls).items():
        try:
            if len(attr) and attr[0].primary_key is True:
                primary_keys.append(name)
        except Exception, e:
            pass
    return tuple(primary_keys)


def primary_key(cls):
    """
    Utility function to get the primary key
    of the class. In case of multiple primary keys,
    use the <classname>_id convention
    """
    keys = class_keys(cls)

    if len(keys) > 1:
        # guess the pk
        pk = cls.__name__.lower() + '_id'
    else:
        pk = next(iter(keys), None)

    if pk not in cls.__dict__:
        # could not find pk field in class, now check
        # whether it has been explicitly specified
        if 'pk_field' in cls.__dict__:
            pk = cls.__dict__['pk_field']
        else:
            raise KeyNotFoundException("Could not figure out primary key field"
                                       "for %s model. Tried to first use %s as"
                                       " field name,and then looked for"
                                       " pk_field attr which was also missing"
                                       % (cls.__name__, pk))

    return pk
