#Logfind

This is an implementation of the logfind project proposed on the website ["Projects The Hard Way"](http://projectsthehardway.com/2015/06/16/project-1-logfind-2/).

The program is basically a poor man's grep. It looks through a list of files and returns the ones that match a series of search words the user inputs.

# Setup
First make sure you setup a .logfind file in your home directory. This file should contain absolute paths to the files you wish to search.
Your home directory is dependent on your OS. You can find it by entering these commands in your terminal (or just navigate to them in your Window GUI).    

- _Linux/Mac:_  
<code> $ cd ~ </code>
- _Windows:_  
<code> $ cd %USERPROFILE% </code> or <code>$ cd C:/User/UserName </code>  

Then create the .logfind file with the file paths.

# Usage

<code>$ logfind [-o] search_words</code>  
The **default** behavior is to find files that have all the words.  
The **-o** sets it to look for files that have any of the words.

