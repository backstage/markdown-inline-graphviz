Markdown Inline Graphviz (for Python 3)
=======================================

This is just a continuation of the great job of Steffen Prince in [sprin/markdown-inline-graphviz](https://github.com/sprin/markdown-inline-graphviz), 
in order to get it work with pip3. If you use python 2, please use the original extension instead.

A Python Markdown extension that replaces inline Graphviz definitions with
inline SVGs or PNGs!

Why render the graphs inline? No configuration! Works with any
Python-Markdown-based static site generator, suche originas
[MkDocs](http://www.mkdocs.org/), [Pelican](http://blog.getpelican.com/), and
[Nikola](https://getnikola.com/) out of the box without configuring an output
directory.

# Installation

    $ pip3 install markdown_inline_graphviz_extension --user

# Usage

Activate the `markdown_inline_graphviz` extension. For example, with Mkdocs, you add a
stanza to mkdocs.yml:

```yaml
markdown_extensions:
    - markdown_inline_graphviz
```

To use it in your Markdown doc, with SVG output:

    ```graphviz dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
    ```

or with PNG:

    ```graphviz dot attack_plan.png
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
    ```

Alternatively you can still using `{%` legacy notation but its not recommended.

```
{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}
```

Supported graphviz commands: dot, neato, fdp, sfdp, twopi, circo.

# Credits

Inspired by [jawher/markdown-dot](https://github.com/jawher/markdown-dot),
which renders the dot graph to a file instead of inline.

Forked from [cesaremorel/markdown-inline-graphviz](https://github.com/cesaremorel/markdown-inline-graphviz), which itself is a fork from [sprin/markdown-inline-graphviz](https://github.com/sprin/markdown-inline-graphviz).

# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
