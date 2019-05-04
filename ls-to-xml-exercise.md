# Text file processing

### Part 1

Write a program to display a structure of files and folders in a hierarchical format.

For example, say we have some structure of files and folders on disk. We list all the files contained in the current folder by running the following command:
```shell
find . -type f > output.txt
```

Now `output.txt` has a list of all the files (including those in subfolders). For example:
```
./file1.txt
./file2.mp3
./folder1/hello.py
./folder1/nested_folder/file3.txt
./folder1/nested_folder/file4.txt
```

Your program will read the contents of `output.txt` and write the following text to the terminal:
```
file1.txt
file2.mp3
folder1/
    hello.py
    nested_folder/
        file3.txt
        file4.txt
```

(Your program shouldn't actually scan the contents of the file system, it should only read `output.txt`.)

Hint: use [`open`](https://docs.python.org/3/library/functions.html#open) to read a file. You can iterate over a file in a `for` loop to read it line by line. You can split a string using [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split).

### Part 2
Unfortunately, your program from Part 1 doesn't work for empty directories, because `find . -type f` lists only files. Change your program so that it reads the output of the `ls -R1` command instead.
Here's what the output of `ls -R1` looks like for the file structure above:
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

### Part 3
Instead of writing to the terminal, your program should write an XML file. For the same file structure above, the program would write an XML file with the following contents:
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

Hint: use [`xml.etree`](https://docs.python.org/3/library/xml.etree.elementtree.html) to work with XML. The XML output doesn't have to be nicely formatted (`xml.etree` outputs everything on one line).

### Part 4
Adjust your program so that it accepts a directory path as a command line argument, runs `ls -R1` on that path, and then generates the XML output as before.

Hint: use [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) for reading command line args and [`subprocess.run`](https://docs.python.org/3/library/subprocess.html#subprocess.run) to run a process.

### Part 5
Add information about file owner and modification time to the XML file. Instead of `ls -R1`, run `ls -Rhl` to get this additional info. Its output looks like this:

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

The resulting XML `file` elements should now include additional attributes: `owner`, `size` (in bytes), and `modified` (formatted like `2019-05-02T23:29:00`).

Hint: use the [`time`](https://docs.python.org/3/library/time.html) module.
