+++
title = 'Exercise 1.3'
weight = 70
hidden = true
question = "Experiment to measure the difference in running time between our potentially inefficient versions and the one that uses strings.Join. (Section 1.6 illustrates part of the time package, and Section 11.4 shows how to write benchmark tests for systematic performance evaluation.)"
date = "2023-11-15T05:58:51+05:30"
ytcode = "dHI2k4NYFdY"
+++

{{< exercisequestion >}}

{{< ytvideo >}}

We'll start the exercise by creating the *main.go* file with the imports and calling the *echo1()*, *echo2()* and *echo3()* functions.

{{< highlight go "title=main.go,linenos=table" >}}
package main

import ( 
    "fmt"
    "os"
)

func main() {
    echo1()
    echo2()
    echo3()
}
{{< / highlight >}}

Now let's create the echo1, echo2 and echo3 implementations as mentioned in the book.

{{< highlight go "title=main.go,linenos=table,linenostart=14" >}}
func echo1() {
    var s, sep string
    for i := 1; i < len(os.Args); i++ {
        s += sep + os.Args[i]
        sep = " "
    } I
    fmt.Println(s)
}
{{< / highlight >}}

{{< highlight go "title=main.go,linenos=table,linenostart=23" >}}
func echo2() {
    s, sep := "", ""
    for _, arg := range os.Args[1:] {
        s += sep + arg
        sep = " "
    }
    fmt.Println(s)
}
{{< / highlight >}}

{{< highlight go "title=main.go,linenos=table,linenostart=32" >}}
func echo3() {
    fmt.Println(strings.Join(os.Args[1:], " "))
}
{{< / highlight >}}

After successfully executing all three echo functions by `go run main.go`, we'll try to measure time taken by each function call by using simply the time package. We'll add these few lines:

{{< highlight go "title=main.go,linenos=table,hl_lines=6 10 12 14 16 18-20" >}}
package main

import ( 
    "fmt"
    "os"
    "time"
)

func main() {
    start1 := time.Now()
    echo1()
    stop1, start2 := time.Now(), time.Now()
    echo2()
    stop2, start3 := time.Now(), time.Now()
    echo3()
    stop3 := time.Now()

    fmt.Println("Time to execute echo1 =", stop1.Sub(start1))
    fmt.Println("Time to execute echo2 =", stop2.Sub(start2))
    fmt.Println("Time to execute echo3 =", stop3.sub(start3))
}
{{< / highlight >}}

Here is the output I got from running it.
{{< showimage "001" "Time taken for each echo call is 0 seconds." >}}

To get better comparison for performance of each echo function, we need to run it multiple times. One way is to execute each echo function in a for loop for *n* number of times which in our case is *1000*. We'll make following changes to the code:

{{< highlight go "title=main.go,linenos=table,hl_lines=9 13 15 17 19 21 23" >}}
package main

import ( 
    "fmt"
    "os"
    "time"
)

const n = 1000

func main() {
    start1 := time.Now()
    for i := 0; i < n; i++ {
        echo1()
    }
    stop1, start2 := time.Now(), time.Now()
    for i := 0; i < n; i++ {
        echo2()
    }
    stop2, start3 := time.Now(), time.Now()
    for i := 0; i < n; i++ {
        echo3()
    }
    stop3 := time.Now()

    fmt.Println("Time to execute echo1 =", stop1.Sub(start1))
    fmt.Println("Time to execute echo2 =", stop2.Sub(start2))
    fmt.Println("Time to execute echo3 =", stop3.sub(start3))
}
{{< / highlight >}}
{{< showimage "002" "Output of running program after the changes." >}}

This seems to conclude that echo1 is slowest and echo2 and echo3 have almost equal performance. It may seem to be correct comparison, but there is an issue. Here, our echo functions are doing two tasks: calculating the output string and printing them. But we need to compare the time taken to calculate string only. So we'll make our code more testable by returning the calculated string instead of printing it, by changing the following lines:

{{< highlight go "title=main.go,linenos=table,linenostart=31,hl_lines=1 7 10 16 19 20" >}}
func echo1() string{
    var s, sep string
    for i := 1; i < len(os.Args); i++ {
        s += sep + os.Args[i]
        sep = " "
    } I
    return s
}

func echo2() string {
    s, sep := "", ""
    for _, arg := range os.Args[1:] {
        s += sep + arg
        sep = " "
    }
    return s
}

func echo3() string {
    return strings.Join(os.Args[1:], " ")
}
{{< / highlight >}}

Here's the output after running `go run ./main.go`.

{{< showimage "001" "Console output after making echo functions more testable. Time take show 0 seconds." >}}

We'll need to increase *n*. Let's change it:
{{< highlight go "title=main.go,linenos=table,hl_lines=9" >}}
package main

import ( 
    "fmt"
    "os"
    "time"
)

const n = 1000000
{{< / highlight >}}
Here's the output of running `go run ./main.go`
{{< showimage "004" "Console output of running program after changing n to 1000000" >}}

This concludes that echo3 function has the best performance, and echo1 and echo2 functions have almost equal performance.

This conclusion is correct but this is not the optimal way of comparing performances of the functions due to two reasons: one is that we need to do hit and trial to get to an *n* which gives us perceivable results, and the second reason is that every time we need to test out code, we need to change out *main.go* file. Which is not recommended if you are testing someone else's code. For this reason, golang provides us with standard testing and benchmarking functionalities in *testing* module.

Go tests can only be used in go modules. So first we need to run the `go mod init ex1.2` to initialize module. Then we need to create *main_test.go* file. Here we'll add the benchmarks for all three echo functions:

```go { title="main_test.go" }
package main

import "testing"

func BenchmarkEcho1(b *testing.B) {
	for i := 1; i < b.N; i++ {
		echo1()
	}
}

func BenchmarkEcho2(b *testing.B) {
	for i := 1; i < b.N; i++ {
		echo2()
	}
}

func BenchmarkEcho3(b *testing.B) {
	for i := 1; i < b.N; i++ {
		echo3()
	}
}
```

We can run the individual benchmarks with the `go test -bench=BenchmarkEcho1`, `go test -bench=BenchmarkEcho2` and `go test -bench=BenchmarkEcho3` commands. Here are the results:


{{< showimage "005" "results of BenchmarkEcho1" "800x webp text" >}}
{{< showimage "006" "results of BenchmarkEcho2" "800x webp text" >}}
{{< showimage "007" "results of BenchmarkEcho3" "800x webp text" >}}

These results conclude the same thing that echo3 function is most optimal, and echo1 and echo2 functions are almost equal in performance.

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}