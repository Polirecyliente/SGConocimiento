This directory contains auxiliary files, needed for different purposes in this project.

The `default_HTML.css` file is the stylesheet used to generate HTML files from Markdown files via Pandoc.

The `default_PDF.css` file is the stylesheet used to generate PDF files from Markdown files via Pandoc.

The `template.markdown` file is the Pandoc template used to generate Markdown files from Markdown files via Pandoc, needed because the default template does not include '$toc-title$' which places the title of the table of contents. If in a future version of Pandoc, the default Markdown template includes '$toc-title$', then this file `template.markdown` should be deleted.

The `Bibliography.yaml` file contains the bibliography of read sources that are the base of this project.

The `APIs` directory contains code created for different APIs. If in a future version of these APIs, this code is included, that code should be deleted from the `APIs` directory, or the whole directory should be deleted if all the code is included in those external APIs.