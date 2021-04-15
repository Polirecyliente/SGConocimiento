# Variables
m=markdown_file
b=SGConocimiento/1_Auxiliaries/Doc_gen/bibliography.yaml
c=SGConocimiento/1_Auxiliaries/Doc_gen/style.css
f=SGConocimiento/1_Auxiliaries/Doc_gen/filter.lua
t=SGConocimiento/1_Auxiliaries/Doc_gen/template.markdown
k=/usr/lib/nodejs/katex/dist/

# Generate Markdown
pandoc $m -o $m -s --toc --number-sections --template $t

# Generate HTML from Markdown
pandoc $m -o file1.html -s -c $c --lua-filter $f --citeproc --bibliography $b --katex=$k

# Generate PDF from HTML
google-chrome --headless --print-to-pdf-no-header --print-to-pdf="file1.pdf" file1.html --user-data-dir=~/.config/google-chrome/ --disable-gpu

# About using Chrome to generate PDF from HTML
# I was trying to use Weasyprint as the PDF engine in Pandoc, but I get these warnings, which make Katex to be rendered badly
# INFO: Step 2 - Fetching and parsing CSS - file:///usr/lib/nodejs/katex/dist/katex.min.css
# WARNING: Ignored `text-rendering:auto` at 1:4793, unknown property.
# WARNING: Ignored `width:-webkit-min-content` at 1:5147, invalid value.
# WARNING: Ignored `width:-moz-min-content` at 1:5173, invalid value.
# WARNING: Ignored `width:min-content` at 1:5196, invalid value.
# WARNING: Ignored `fill:currentColor` at 1:20781, unknown property.
# WARNING: Ignored `stroke:currentColor` at 1:20799, unknown property.
# WARNING: Ignored `fill-rule:nonzero` at 1:20819, unknown property.
# WARNING: Ignored `fill-opacity:1` at 1:20837, unknown property.
# WARNING: Ignored `stroke-width:1` at 1:20852, unknown property.
# WARNING: Ignored `stroke-linecap:butt` at 1:20867, unknown property.
# WARNING: Ignored `stroke-linejoin:miter` at 1:20887, unknown property.
# WARNING: Ignored `stroke-miterlimit:4` at 1:20909, unknown property.
# WARNING: Ignored `stroke-dasharray:none` at 1:20929, unknown property.
# WARNING: Ignored `stroke-dashoffset:0` at 1:20951, unknown property.
# WARNING: Ignored `stroke-opacity:1` at 1:20971, unknown property.
# WARNING: Ignored `stroke:none` at 1:21004, unknown property.
# WARNING: Ignored `box-sizing:border-content` at 1:22091, invalid value.
# WARNING: Ignored `right:calc(50% + .3em)` at 1:22549, invalid value.
# WARNING: Ignored `left:calc(50% + .3em)` at 1:22650, invalid value.

# Because Weasyprint does not support those CSS properties, I will keep using Chrome to convert HTML into PDF