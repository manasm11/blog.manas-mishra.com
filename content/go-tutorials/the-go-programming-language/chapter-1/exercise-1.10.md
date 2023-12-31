+++
title = 'Exercise 1.10'
weight = 120
# hidden = true
question = "Find a web site that produces a large amount of data. Investigate caching by running fetchall twice in succession to see whether the reported time changes much. Do you get the same content each time? Modify fetchall to print its output to a file so it can be examined."
date = "2023-11-15T05:58:51+05:30"
ytcode = "i3mkhsxehiQ"
+++


{{< exercisequestion >}}

{{< ytvideo >}}

Let's start by duplicating the *fetchall* example code from the book.

{{< highlight go "title=main.go,linenos=table">}}
// Fetchall fetches URLs in parallel and reports their times and sizes.
package main

import (
    "fmt"
    "io"
    "io/ioutil"
    "net/http"
    "os"
    "time"
)

func main() {
    start := time.Now()
    ch := make(chan string)
    for _, url := range os.Args[1:] {
        go fetch(url, ch) // start a goroutine
    }
    for range os.Args[1:] {
        fmt.Println(<-ch) // receive from channel ch
    }
    fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
    start := time.Now()
    resp, err := http.Get(url)
    if err != nil {
        ch <- fmt.Sprint(err) // send to channel ch
        return
    }

    nbytes, err := io.Copy(ioutil.Discard, resp.Body)
    resp.Body.Close() // don't leak resources
    if err != nil {
        ch <- fmt.Sprintf("while reading %s: %v", url, err)
        return
    }
    secs := time.Since(start).Seconds()
    ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)
}
{{< / highlight >}}

We can try to run the program with multiple websites as argument with this command `go run main.go https://golang.org http://gopl.io https://godoc.org`
{{< showimage "012.png" "Output of running program with multiple websites as argument." "600x webp text" >}}

The first part of question asks us to investigate caching mechanism of the *http.Get* method. To do that, we will just duplicate a few lines of code in the program to make the http calls twice.

{{< highlight go "title=main.go,linenos=table,hl_lines=11-16,linenostart=13">}}
func main() {
    start := time.Now()
    ch := make(chan string)
    for _, url := range os.Args[1:] {
        go fetch(url, ch) // start a goroutine
    }
    for range os.Args[1:] {
        fmt.Println(<-ch) // receive from channel ch
    }
    for _, url := range os.Args[1:] {
        go fetch(url, ch) // start a goroutine
    }
    for range os.Args[1:] {
        fmt.Println(<-ch) // receive from channel ch
    }
    fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}
{{< / highlight >}}

Now let's run the same command as above: `go run main.go https://golang.org http://gopl.io https://godoc.org`

{{< showimage "013.png" "Output of running program after modifying to analyze caching. We can see the second calls take less time than first one's due to caching." "600x webp text" >}}

Now, we need to store the console output to a file for later review. We'll do this by using *os.OpenFile* function and opening a file in *create* and *write* modes. Here's the final code of solution.

{{< highlight go "title=main.go,linenos=table,hl_lines=15-20 25-27 33-35" >}}
// Fetchall fetches URLs in parallel and reports their times and sizes.
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

func main() {
	start := time.Now()
	ch := make(chan string)
	f, err := os.OpenFile("output.txt", os.O_CREATE|os.O_WRONLY, 0x666)
	if err != nil {
		errMsg := "Error: " + err.Error() + "\n"
		fmt.Print(errMsg)
		f.Write([]byte(errMsg))
	}
	for _, url := range os.Args[1:] {
		go fetch(url, ch) // start a goroutine
	}
	for range os.Args[1:] {
		output := <-ch // receive from channel ch
		fmt.Println(output)
		f.Write([]byte(output + "\n"))
	}
	for _, url := range os.Args[1:] {
		go fetch(url, ch) // start a goroutine
	}
	for range os.Args[1:] {
		output := <-ch // receive from channel ch
		fmt.Println(output)
		f.Write([]byte(output + "\n"))
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err) // send to channel ch
		return
	}

	nbytes, err := io.Copy(io.Discard, resp.Body)
	resp.Body.Close() // don't leak resources
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)
}
{{< / highlight >}}

Now let's run the same command as above: `go run main.go https://golang.org http://gopl.io https://godoc.org`

```text {title="output.txt"}
0.93s    32378  https://godoc.org
1.63s    61870  https://golang.org
2.34s     4154  http://gopl.io
0.62s    32378  https://godoc.org
0.67s     4154  http://gopl.io
0.73s    61870  https://golang.org
```

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
