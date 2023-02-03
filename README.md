#Data Structure Project
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,qt" />
  </a>
</p>

<p>
  This XML Editor was realized using Python and PyQt5 for GUI alongisde NetworkX that was used to visualize the graph
</p>

<h2> Algorithms </h2>
<h3>Minify</h3>
<p>Iterate over each line step by step and strip it of white spaces using strip() function</p>
<h3>ClearSpacing</h3>
<p>Iterate over each line step by step and strip it of white spaces to the left only.</p>
<h3>Prettify</h3>
<p>After stripping lines from their left white spaces using ClearSpacing,determine positions of arch brackets that form the xml tag, previousstatus is set to open at first then if line contains both open and closed tags then it’ll be shifted, if only closed tag then shift backwards if previous status is closed and shift forward if the previous status is open then the new string is returned.</p>
<h3>Json</h3>
<p>
•	Read the xml file and store it in lines(list).
•	Define classes for tags and mistakes.
•	Iterate in each row of lines.
•	Iterate In each column for the row. If it is found an opening tag, push it into the stack of tags.
•	If it is found a closing tag and it matches the top of the tags stack, then this tag is consistent and popped.
•	If it does not match the top tag, search for its tag in the copy of the stack if it is found, so a mistake will added to the list(opened tag without its closed one), the I will fix it by putting it in the right place in the line.
•	If it is not found after all tags in the copied Stack are popped, then adding mistake in the list(an closed tag without its opening one)
•	The Stack at the end must be empty
•	Return the new lines as a string and the mistake List.
</p>
<h3>HuffmanEnc</h3>
<p>
  HuffmanEncoding function accepts only sample.xml as an argument.
•	Using function CalculateProbability to return all symbols in the file with their probabilities.
•	Create huffman tree nodes by iterating on the different distinct symbols in file giving codes for every node , 0 for left and 1 for right.
•	After finishing this iteration we get the root of the tree passed to function to calculate codes of these symbols and return in huffmanencoding.
•	Passing sample.xml file with the huffmanencoding to outputEncoded function to return a stream of bits as a string to be saved then as a binary stream to a file as the compressed file.
</p>
<h3>HuffmanDec</h3>
<p>
•	Huffman Decoding function accepts as arguments the encoded string and the Huffman tree root.
•	Iterate on each bit to recognize the stream as symbols to decode and write on decompressed file.
•	After finishing all iterations, the file would be retrieved.
</p>
