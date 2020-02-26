"""
@Question

Write a function to flatten a nested dictionary.
Namespace the keys with a period.
For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, 
i.e. no clobbering will occur.
"""

def flatten(nested_dict):
    # empty dictionary
    flat_dict = {}

    for key, value in nested_dict.items():
        if(type(value) != dict):
            flat_dict[key] = value
        # if value is not dictionary
        else:
            # applying recursive operation
            for key2, value2 in flatten(value).items():
                flat_dict[key+'.'+key2] = value2
    
    return flat_dict
    
print flatten(
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
)

