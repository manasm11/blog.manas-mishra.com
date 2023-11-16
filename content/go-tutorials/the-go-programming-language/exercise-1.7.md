+++
title = 'Exercise 1.7-1.9'
weight = 110
hidden = true
question = """1.7: The function call io.Copy(dst, src) reads from src and writes to dst. Use it instead of ioutil.ReadAll to copy the response body to os.Stdout without requiring a buffer large enough to hold the entire stream. Be sure to check the error result of io.Copy...  1.8: Modify fetch to add the prefix http:// to each argument URL if it is missing. You might want to use strings.HasPrefix...  1.9: Modify fetch to also print the HTTP status code, found in resp.Status."""
date = "2023-11-15T05:58:51+05:30"
ytcode = "Gwt6JawP7KA"
+++

{{< exercisequestion >}}

{{< ytvideo >}}

As always, let's start with replicating the code from book.

{{< highlight go "title=main.go,linenos=table" >}}
// Fetch prints the content found at a URL.
package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
)

func main() {
    for _, url := range os.Args[1:] {
        resp, err := http.Get(url)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }
        b, err := ioutil.ReadAll(resp.Body)
        resp.Body.Close()
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
            os.Exit(1)
        }
        fmt.Printf("%s", b)
    }
}
{{< / highlight >}}

To solve exercise 1.7, we need to make following changes in the main.go.

{{< highlight diff "title=main.go,linenos=table,linenostart=11" >}}
// Fetch prints the content found at a URL.
func main() {
    for _, url := range os.Args[1:] {
        resp, err := http.Get(url)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }
-       b, err := ioutil.ReadAll(resp.Body)
+       _, err = io.Copy(os.Stdout, resp.Body)
        resp.Body.Close()
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
            os.Exit(1)
        }
-       fmt.Printf("%s", b)
    }
}
{{< / highlight >}}

Running the program with `go run main.go http://gopl.io` gives the same output as the original code.

Now, to solve exercise 1.8, we need to add these few lines in the code.

{{< highlight go "title=main.go,linenos=table,linenostart=11,hl_lines=4-6" >}}
// Fetch prints the content found at a URL.
func main() {
    for _, url := range os.Args[1:] {
        if !strings.HasPrefix("http", url) {
            url = "http://" + url
        }
        resp, err := http.Get(url)
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
            os.Exit(1)
        }
        _, err = io.Copy(os.Stdout, resp.Body)
        resp.Body.Close()
        if err != nil {
            fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
            os.Exit(1)
        }
    }
}
{{< / highlight >}}

Running this program with url without *http* prefix also gives the same output. You may try to run `go run main.go gopl.io`

Now to display the status code, we just need to add one more line in out *main.go*. Here is the final *main.go* that solves all the exercises 1.7, 1.8 and 1.9.

{{< highlight go "title=main.go,linenos=table,hl_lines=23" >}}
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
)

// Fetch prints the content found at a URL.
func main() {
	for _, url := range os.Args[1:] {
		if !strings.HasPrefix("http", url) {
			url = "http://" + url
		}
		resp, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		_, err = io.Copy(os.Stdout, resp.Body)
		fmt.Println("status:", resp.Status)
		resp.Body.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
			os.Exit(1)
		}
	}
}
{{< / highlight >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
