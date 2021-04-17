<!--
#   Mermaid and SMILES
-->

<!-- #T# Table of contents -->

<!-- #C# Mermaid -->
<!-- #C# - Styling -->
<!-- #C# SMILES -->

<!-- #T# Beginning of content -->

<!-- #C# Mermaid -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# Mermaid is used in Markdown to create diagrams such as graphs, pie charts, Gantt diagram, flowcharts, class diagrams, entity relationship diagrams, etcetera -->

<!-- #T# Pandoc can be used to render Mermaid diagrams in HTML and PDF files, this needs the use of an external Pandoc filter, such as the `mermaid-filter` filter -->

<!-- #T# to use Mermaid in Markdown, the code block is used, using the word 'mermaid' as the language of the code block -->
``` mermaid
graph LR
    A---B
    A-->C
    B-->D
    C-->D
```
<!-- #T# the first word after mermaid is , this word determines the type of diagram, 'graph' is to make flowcharts, it can also be 'pie' for a pie chart, 'gantt' for a Gantt diagram, 'stateDiagram' for a state diagram, 'classDiagram' for a class diagram, 'erDiagram' for an entity relationship diagram, 'sequenceDiagram' for a sequence diagram, each with its own syntax -->

<!-- #T# Mermaid code can be written in its own file, and it can be compiled into SVG using the `mmdc` command, which is the Mermaid CLI -->

<!-- #T# the `mmdc` command has the following basic syntax -->
<!-- # SYNTAX `mmdc -i input_file1.mmd -o output_file1.svg`{.bash} -->
<!-- #T# the file output_file1.svg contains the image form of the Mermaid diagram in input_file1.mmd -->

<!-- #T# to put a caption to the image, the `caption` attribute can be used. The format attribute sets the format of the image, it can be 'svg', 'png' -->
``` {.mermaid caption="image_caption1" format="svg"}
graph TB
    A-->B
```

<!-- #T# in a 'graph' diagram, LR stands for left to right, but it can be replaced with TB which stands for top to bottom, these letters can be reversed, RL stands for right to left, and BT stands for bottom to top. TD is a synonym for TB, but there is no DT counterpart -->
``` mermaid
graph BT
    A-->B
```

<!-- #T# in the syntax `A---B`, A and B are nodes, nodes can have any name but not the name 'end' -->

<!-- #T# the general syntax for nodes is -->

<!-- # SYNTAX identifier1open_delimiter1 string1 close_delimiter1 -->

<!-- #T# identifier1 is a string that identifies the node. string1 is a string with the contents that are displayed in the diagram, string1 is optional, if left out then identifier1 is displayed in the diagram -->

<!-- #T# the pair open_delimiter1 and close_delimiter1 is a pair of corresponding delimiters, they can be '[string1]' for a rectangle, '(string1)' for a rectangle with rounded corners, '([string1])' for a rectangle with rounded horizontal edges, '[[string1]]' for a flowchart subroutine shape, '[(string1)]' for a flowchart database shape, '((string1))' for a circle, '>string1]' for a five side shape, '{string1}' for a square rhombus, '{{string1}}' for a hexagon, '[/string1/]' for a slanted right parallelogram, '[\string1\]' for a slanted left parallelogram, '[/string1\]' for an upwards trapezoid, '[\string1/]' for a downwards trapezoid -->

<!-- #T# note that identifier1open_delimiter1 has no space between identifier1 and open_delimiter1 -->

<!-- #T# string1 can be placed inside double quoted, to be able to used delimiters as characters that are part of the string, for example "text (text) text" -->

<!-- #T# node1 abbreviates identifier1open_delimiter1string1close_delimiter1 -->

<!-- #T# nodes can be connected in different ways with this syntax -->

<!-- # SYNTAX node1 connector1 node2 -->

<!-- #T# node1 and node2 are nodes as shown before. connector1 can be, '-->' for an arrow from node1 to node2, '---' for a line from node1 to node2, '-.-' for a dotted line, '-.->' for a dotted arrow, '==>' for a thick arrow -->

<!-- #T# connector1 can have text inside, it can be '-- string1 -->' for an arrow with text, '-- string1 ---' for a line with text, '-. string1 .-' for a dotted line with text, '-. string1 .->' for a dotted arrow with text, '== string1 ==>' for a thick arrow with text -->

<!-- #T# several nodes can be connected in chain -->
<!-- # SYNTAX node1 connector1 node2 connector2 node3 -->
<!-- #T# more nodes and connectors can be placed like this -->
graph TB
  A --> B --> C[End node]

<!-- #T# the & operator means 'and', it's used to put nodes on the same hierarchical level -->
graph TB
  A & B --> C
<!-- #T# A and B are placed on the same hierarchical level, above C -->

<!-- #T# two nodes are separated by a single hierarchical level by default. To separate two nodes further, the arrow length is increased. Each character that the arrow length is increased corresponds to one additional hierarchical level separating the nodes. In arrows with text, the arrow length is increased in the end side of the arrow -->
graph TB
  A --> D
  B ====> D
  C -. text ....-> D
<!-- #T# B is plus two hierarchical levels above D, C is plus three hierarchical levels above D -->

<!-- #T# nested graphs can be created with this syntax -->

<!-- # SYNTAX nested graphs    -->
<!-- # subgraph subgraph_id1   -->
<!-- #   nodes_and_connectors1 -->
<!-- # end                     -->

graph TB
  A --> B
  A --> C
    subgraph sub1
      C --> D
      subgraph sub_sub1
        D --> E
      end
    end

<!-- #C# - Styling -->

<!-- # |----- -->
<!-- #T# connectors and nodes can be styled, using SVG property value pairs -->

<!-- #T# to style connectors, their number of creation is used, which is the sequential number in which they appear in the graph definition -->

<!-- #T# the following syntax is used to style connectors -->
<!-- # SYNTAX linkStyle int1 property1 : value1, propertyN : valueN -->
<!-- #T# int1 is the number of creation of the link being styled, counting from 0, property1 and value1 are an SVG property value pair -->

graph TB
  A -- link 0 --> B -- link 1 --> C
  B -- link 2 --> D

linkStyle 2 stroke : green,  stroke-width : 6px

<!-- #T# to style nodes, their id is used, with the following syntax -->
<!-- # SYNTAX style id1 property1 : value1, propertyN : valueN -->

graph TB
  A[text] --> B[text]

style A fill : magenta, stroke-dasharray : 10 5

<!-- #T# classes can be created to apply style to all nodes of that class, with the following syntax -->
<!-- # SYNTAX classDef class1 property1 : value1, propertyN : valueN -->

<!-- #T# a class is assigned to a set of nodes with the following syntaxes -->
<!-- # SYNTAX class node_id1, node_id2 class1 -->
<!-- # SYNTAX node_id1:::class1 connector1 node2 -->

<!-- #T# the second syntax allows the assignment of class1 to node1 as part of the graph definition -->

graph TB
  A:::class1 --> B

classDef class1 fill : green
<!-- # |----- -->

<!-- # |------------------------------------------------------------- -->

<!-- #C# SMILES -->

<!-- # |------------------------------------------------------------- -->
<!-- #T# SMILES stands for Simplified Molecular Input Line Entry System, it is used in Markdown to convert plain text into 2D molecular diagrams -->

<!-- #T# to use SMILES in Markdown, a code block is used, using the word 'smiles' as the language of the code block (it may require a Mathpix SMILES extension or compiler to see the molecule) -->
```smiles
O=C=O
```
<!-- #T# this shows a carbon dioxide molecule -->
<!-- # |------------------------------------------------------------- -->