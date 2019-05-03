# Text file processing

### Part 1
Write a program to convert the output of the `ls -R1` command to a hierarchical XML structure.
 
 The program should read its input from a text file and write its output to another file.
 
 For example, the following `ls -R1` output:
 ```
  file1.txt
  file2.mp3
  folder1

  ./folder1:
  hello.py
  nested_folder

  ./folder1/nested_folder:
  file3.txt
  file4.txt 
 ```
 
 Will be converted to the following XML file:
 ```xml
<tree generated_at="2019-04-29T20:27:02Z">
  <file name="file1.txt" />
  <file name="file2.mp3" />
  <folder name="folder1">
    <file name="hello.py" />
    <folder name="nested_folder">
      <file name="file3.txt" />
      <file name="file4.txt" />
    </folder>
  </folder>
</tree>
```
