+++
title = 'Exercise 1.11'
weight = 130
hidden = true
question = " Try fetchall with longer argument lists, such as samples from the top million web sites available at alexa.com. How does the program behave if a web site just doesn’t respond? (Section 8.9 describes mechanisms for coping in such cases.)"
date = "2023-11-15T05:58:51+05:30"
ytcode = "gEcFZQyn4yk"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

First we'll have to download the top 1 million websites alexa dataset. You can download it via kaggle or using {{< downloadablelink "/csv/top-1m.csv" "this link" >}}.

Now, we'll start by duplicating the fetchall example code.

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

We will have to read the urls from the csv file and make http calls.
{{< highlight go "title=main.go,linenos=table,linenostart=13,hl_lines=4-10" >}}
func main() {
    start := time.Now()
    ch := make(chan string)
    bs, _ := os.ReadFile("top-1m.csv")
    urlLines := strings.Split(string(bs), "\n")
    for _, urlLine := range urlLines {
        url := strings.Split(urlLine, ",")[1]
        go fetch("https://"+url, ch) // start a goroutine
    }
    for range urlLines {
        fmt.Println(<-ch) // receive from channel ch
    }
    fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}
{{< / highlight >}}

{{% notice warning %}}
Don't try to run this function on your computer because this creates 1 million concurrent http calls. This will lead your computer to hang until you kill the process.
{{% /notice %}}

We will change the code to perform only 100 concurrent connections. We will create a *rateLimiter*. Here is the final code of solution.

{{< highlight go "title=main.go,linenos=table,hl_lines=16 21 29-31" >}}
// Fetchall fetches URLs in parallel and reports their times and sizes.
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

func main() {
	start := time.Now()
	ch := make(chan string)
	rateLimiter := make(chan struct{}, 100)
	bs, _ := os.ReadFile("top-1m.csv")
	urlLines := strings.Split(string(bs), "\n")
	for _, urlLine := range urlLines {
		url := strings.Split(urlLine, ",")[1]
		go fetch("https://"+url, ch, rateLimiter) // start a goroutine
	}
	for range urlLines {
		fmt.Println(<-ch) // receive from channel ch
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string, rateLimiter chan struct{}) {
	rateLimiter <- struct{}{}
	defer func() { <-rateLimiter }()
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

I removed the use of ioutil package because it is deprecated.

First line of fetch function ensures that the program would proceed only where there is room in the rateLimiter channel. Once there is space of atleast one element in the rateLimiter channel, the function proceeds and makes http calls.

The defer statement ensures that once the fetch function completes, it removes one element from the rateLimiter channel, so there is room for one more element. This way, we are using rateLimiter channel to ensure only 100 simultaneous connections are established.

This function would take 2-3 days to execute 1 million http calls. You may want to run this type of programs in remote servers if you are gathering any useful data from websites. To test it locally, I reduced the number of websites to 200 in the csv file.

{{< showimage "014" "time elapsed 34.24 seconds." "800x webp text" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
