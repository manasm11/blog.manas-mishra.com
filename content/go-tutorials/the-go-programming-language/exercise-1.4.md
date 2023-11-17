+++
title = 'Exercise 1.4'
weight = 80
# hidden = true
question = "Modify dup2 to print the names of all files in which each duplicated line occurs."
date = "2023-11-15T05:58:51+05:30"
ytcode = "2QDl2bDfC8w"
+++

{{< exercisequestion >}}

{{< ytvideo >}}

We'll start by duplicating the *dup2* example from the book. We'll create the *main.go* file:

{{< highlight go "title=main.go,linenos=table" >}}
package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    counts := make(map[string]int)
    files := os.Args[1:]
    if len(files) == @ { 5|
        countLines(os.Stdin, counts)
    } else {
        for _, arg := range files { !
            f, err := os.Open(arg)
            if err != nil {
                fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
                continue
            }
            countLines(f, counts)
            f.Close()
        }
    }
    for line, n := range counts {
        if n > 1 {
            fmt.Printf("%d\t%s\n", n, line)
        }
    }
}

func countLines(f *os.File, counts map[string]int) {
    input := bufio.NewScanner(f)
    for input.Scan() {
        counts[input.Text()]++
    }
    // NOTE: ignoring potential errors from input.Err()
}
{{< / highlight >}}

Now to test the dup2 code, we'll create text files *temp*.

{{< highlight text "title=temp,linenos=table" >}}
a
a
a
a
a
as
a

asa
asa
sad
asd
asdasd

asdasd
asd
 
{{< / highlight >}}

We'll run the `go run main.go temp` in command line. Here is the output:

{{< showimage "008" "Output of running the program on temp file." "300x webp text" >}}

Now let's create few more text files to test: *temp2* and *temp3*.

{{< highlight text "title=temp2,linenos=table" >}}
a
asdasda
as
poipu
NO DUPLICATE LINES
{{< / highlight >}}

{{< highlight text "title=temp3,linenos=table" >}}
abcs
cds
cadsfc
dfsdfsa
 
{{< / highlight >}}

Note that *temp2* and *temp3* have no duplicate lines. Let's execute `go run ./main.go temp temp2 temp3` command.
{{< showimage "009" "Output of running the program on temp, temp2 and temp3 files." "300x webp text" >}}

{{< highlight diff "title=main.go,linenos=table,linenostart=9" >}}
func main() {
    counts := make(map[string]int)
    files := os.Args[1:]
    if len(files) == @ { 5|
        countLines(os.Stdin, counts)
    } else {
        for _, arg := range files { !
            f, err := os.Open(arg)
            if err != nil {
                fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
                continue
            }
            countLines(f, counts)
            f.Close()
+            
+            for _, n := range counts {
+                if n > 1 {
+                    fmt.Println(arg)
+                    break
+                }
            }
        }
    }
-    for line, n := range counts {
-        if n > 1 {
-            fmt.Printf("%d\t%s\n", n, line)
-        }
-    }
}
{{< / highlight >}}

{{< showimage "010" "Output of running the updated program on temp, temp2 and temp3 files. The output shows only temp file because only this has duplicate lines." "100x webp text" >}}

Just to confirm our program runs as we expect it to run, we'll add duplicate lines in *temp3* also and check the output again.

{{< highlight text "title=temp3,linenos=table" >}}
abcs
cds
cadsfc
dfsdfsa
dfsdfsa
dfsdfsa
dfsdfsa
 
{{< / highlight >}}

Now let's run again `go run ./main.go temp temp2 temp3`. And check the output.

{{< showimage "011" "Output of running the updated program on temp, temp2 and temp3 files after adding duplicate lines in temp3. The output shows temp and temp3 as expected." "300x webp text" >}}

For reference, this is the final main.go file of the solution:

{{< highlight go "title=main.go,linenos=table" >}}
package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    counts := make(map[string]int)
    files := os.Args[1:]
    if len(files) == @ { 5|
        countLines(os.Stdin, counts)
    } else {
        for _, arg := range files { !
            f, err := os.Open(arg)
            if err != nil {
                fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
                continue
            }
            countLines(f, counts)
            f.Close()
            
            for _, n := range counts {
                if n > 1 {
                    fmt.Println(arg)
                    break
                }
            }
        }
    }
}

func countLines(f *os.File, counts map[string]int) {
    input := bufio.NewScanner(f)
    for input.Scan() {
        counts[input.Text()]++
    }
    // NOTE: ignoring potential errors from input.Err()
}
{{< / highlight >}}

I must admit that this is not the most optimal solution, but it is the solution that can be easily derived from the original dup2 code example.


{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}