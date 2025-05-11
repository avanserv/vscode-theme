Comprehensive reStructuredText Features
========================================

Titles and Sections
-------------------

reStructuredText supports hierarchical section titles using underlines and overlines.

Lists
-----

- Bullet lists are created using `-`, `*`, or `+`.
- Nested lists are indented.

1. Enumerated lists use numbers followed by a period.
2. They can also be nested.

Definition Lists
~~~~~~~~~~~~~~~~

Term 1
    Definition for term 1.

Term 2
    Definition for term 2.

Tables
------

Simple Table::

    +------------+------------+
    | Header 1   | Header 2   |
    +============+============+
    | Row 1 Col 1| Row 1 Col 2|
    +------------+------------+
    | Row 2 Col 1| Row 2 Col 2|
    +------------+------------+

Grid Table::

    +------------+------------+
    | Header 1   | Header 2   |
    +============+============+
    | Row 1 Col 1| Row 1 Col 2|
    +------------+------------+
    | Row 2 Col 1| Row 2 Col 2|
    +------------+------------+

Inline Markup
-------------

*Emphasis* (italic), **Strong** (bold), ``Inline Code``, and `Hyperlink <https://example.com>`_.

Images
------

.. image:: https://via.placeholder.com/150
    :alt: Placeholder Image
    :align: center

Directives
----------

.. note::

    This is a note directive.

.. warning::

    This is a warning directive.

.. code-block:: python

    # Code block directive
    print("Hello, World!")

Admonitions
-----------

.. admonition:: Custom Admonition

    This is a custom admonition.

References
----------

- `Internal Reference <#lists>`_
- `External Reference <https://example.com>`_

Footnotes
---------

This is a sentence with a footnote reference [#]_.

.. [#] This is the footnote text.

Substitutions
-------------

|substitution_example|

.. |substitution_example| replace:: This is a substitution.

Math
----

Inline math: :math:`E = mc^2`

Block math::

    .. math::

        E = mc^2

Comments
--------

.. This is a comment and will not appear in the output.

