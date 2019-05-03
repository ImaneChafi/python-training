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
<tree>
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

Hint: use [`open`](https://docs.python.org/3/library/functions.html#open) to read a file and [`xml.etree`](https://docs.python.org/3/library/xml.etree.elementtree.html) to work with XML.

### Part 2
Adjust your program so that it accepts a directory path as a command line argument, runs `ls -R1` on that path, and then generates the XML output as before.

Hint: use [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) for reading command line args and [`subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run) to run a process.

### Part 3
Add information about file owner and modification time to the XML file. Instead of `ls -R1`, run `ls -Rhl` to get this additional info*. Its output looks like this:

```
total 8200
-rw-r--r--  1 matan  staff   509B  2 May 23:26 file1.txt
-rw-r--r--  1 matan  staff   3.5M  2 May 23:27 file2.mp3
drwxr-xr-x  4 matan  staff   128B  2 May 23:10 folder1

./folder1:
total 8192
-rw-r--r--  1 matan  staff   3.7M  2 May 23:27 hello.py
drwxr-xr-x  4 matan  staff   128B  2 May 23:10 nested_folder

./folder1/nested_folder:
total 24
-rw-r--r--  1 matan  staff   8.0K  2 May 23:29 file3.txt
-rw-r--r--  1 matan  staff   521B  2 May 23:10 file4.txt
```

The resulting XML `file` elements should now include additional attributes: `owner`, `size` (in bytes) and `modified` (formatted like `2019-05-04T12:27:02`).

Hint: use the [`time`](https://docs.python.org/3/library/time.html) module.

\* No, you may not omit the `h` from the command. :)
