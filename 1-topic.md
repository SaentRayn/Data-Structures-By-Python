## Trees: Grow()ing The Future

The first data structure we aim to take a look at are Trees.

[Back to Home](0-welcome.md)

### What Are They:

<details>
<summary>How Do They Work:</summary>
<br>
A Tree is often used for analyzing a collection of data in a type of order that can show relativity. For example a family tree shows the relation of parent to child. The tree utilizes a range of basic functions that allow for efficiency in application. These functions include a getroot, insert/add, find, delete, and a print.

One might ask why is their a print function within the tree-based function when one already exists for Python. The answer is, "the same reason the find function is dynamic". When we possess a tree of data their will be a root with it's many existing nodes and leafs that make up the tree. Whenever we want to find something on the tree we need to determine the best type of search in order to more efficiently find the desired node. This could be a depth-first, breadth-first, or a simple traversel of the tree. The differences being do I search through each branch starting left or right side, or do I check each layer before moving to the next.

The best example of these is relative of an example below mentioning a family tree and a championship bracket. If I follow the champion as my root and want to find the path they took in each match to win the tournament, then I could do a breadth-first as I only need to find which of the two nodes is the champion and then move down that corresponding branch. In a family tree we usually will use a depth-first as we are moving or seeking out the leaf node's lineage through the family tree. There are more options for these searches but these will suffice for now in understanding.

The print function will follow a similar theme as do I want each branch to print out first, or just go from left-to-right (or vice-versa) printing every node along the way. We need to define or use the defined tree-based print to reference the node data and print off for us in the order we seek to see the data. If I want to print off my branch in geneology going from me to each of my grandparents, then I might need to define a reverse bread-first, or a breadth-last if you will, that would print me, then my mother/father, then my mother's mother/father, and father's mother/father. This can become tedious so often the tree is used in conjunction with another data structure for storing these values as they are found and then just printing off that structure.

*There is an axample of this beneficial conjunction in the conclusion*
</details>
<br>

<details>
<summary>Why Use Them:</summary>
<br>
Trees serve as a way of sorting information in order to anlayze factors relating to the data set. A few of these examples include a family tree in geneology or a championship bracket. Though a bracket is an inverted tree it could be analyzed from the winner down until each leaf is found representing every participant within the challenge. The family tree will show relation of node to leaf or parent to child through each generation until the eventual top is reached. This in most belief's goes to Adam and Eve as the first humans. More immediate however parents and grandparents direct lines show one branch of the tree leading to a leaf whether that be you or your posterity so forth.

Because of this straightforward lineage that occurs in a tree is it much easier to insert and delete from a tree. Though I hope you don't delete someone from your family tree whenever a new child is born they are immediately attached as a leaf to the respective parents node. Similarly, searching is considerably faster as if we want to see who the champion faced in the second or even first match we can simply trace down the branch following the champion until that layer or level in the tree we seek.

Finding a great-great-great-grandparent can be just as easy and fast, assuming the tree is completed in some of its glory. We start at the leaf/child we want to know the great-great-great-grandparent of and then walk up each edge or link from parents to the parents of the parents and so forth until the desired node is located.
</details>
<br>


<details>
<summary>Limitations:</summary>
<br>
Alright, I admit. A family tree and champion's bracket aren't always considered true trees in the definition of the data structure, they exhibit many of the core qualities and strengths of them. In inverse analization, however, a tree data structure can be limited by computing power or simply the way it is built in the program. Their may only be room for 2 children nodes on each parent node. The tree can be unbalanced if the wrong root is picked and the tree is left unbalanced. This causes extra unnecessary computing power to be consumed. Without babysitting of the tree it can fail just as swiftly as it can assist for good in a program.

Depending on the versality of the program and what is needed from a data structure it might be more beneficial to pick something like a map, linked list, or dictionary structure. However if the goal is to continue to build layer by layer forever such as the family tree for geneological research it may be more beneficial to use a tree and encorporate the necessary overhead in order to maintain the tree and the various nodes encorporated.
</details>
<br>

### Example Problems:

<details>
<summary>Problem:</summary>
<br>
</details>
<br>


<details>
<summary>Solution For Example:</summary>
<br>
</details>
<br>

### Your Turn To Practice:

<details>
<summary>Problem:</summary>
<br>
</details>
<br>


<details>
<summary>A Possible Solution:</summary>
<br>
</details>
<br>


[To Queues ->](2-topic.md)