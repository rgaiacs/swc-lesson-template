#!/usr/bin/env python
"""Pandoc filter to convert add ids to glossary entries.

Usage:

    pandoc source.md --filter=id4glossary.py --output=output.html
"""
import pandocfilters as pf

import common

def keyword2html(keyword_node):
    """Return HTML version of keyword with id."""
    keyword = pf.stringify(keyword_node)
    id = common.text2fragment_identifier(keyword)
    return [{"t": "Span",
             "c": [[id, [],[]],
                 keyword_node]}]

def id4glossary(key, value, format, meta):
    """Add id to keywords at glossary."""
    if key == "DefinitionList":
        for definition in value:
            definition[0] = keyword2html(definition[0])
        return {"t": key,
                "c": value}

if __name__ == '__main__':
    pf.toJSONFilter(id4glossary)
