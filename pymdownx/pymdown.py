"""
pymdownx.pymdown
Import all of the pymdown plugins
(except for those that shouldn't regularly be used)

MIT license.

Copyright (c) 2014 Isaac Muse <isaacmuse@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from __future__ import unicode_literals
from markdown import Extension

extensions = [
    'pymdownx.magiclink',
    'pymdownx.betterem',
    'pymdownx.tilde',
    'pymdownx.caret',
    'pymdownx.mark',
    'pymdownx.smartsymbols',
    'pymdownx.githubemoji',
    'pymdownx.tasklist',
    'pymdownx.progressbar',
    'pymdownx.headeranchor',
    'pymdownx.superfences',
    'pymdownx.math'
]


class PyMdownExtension(Extension):
    """Add various extensions to Markdown class"""

    def extendMarkdown(self, md, md_globals):
        """Register extension instances"""
        md.registerExtensions(extensions, self.config)


def makeExtension(*args, **kwargs):
    return PyMdownExtension(*args, **kwargs)