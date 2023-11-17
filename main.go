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
