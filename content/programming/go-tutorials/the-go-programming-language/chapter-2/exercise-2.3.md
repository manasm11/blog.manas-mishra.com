+++
title = 'Exercise 2.3'
weight = 160
# hidden = true
question = "Rewrite PopCount to use a loop instead of a single expression. Compare the performance of the two versions. (Section 11.4 shows how to compare the performance of different implementations systematically.)"
date = "2023-11-15T05:58:51+05:30"
ytcode = "l8PBYF2M-bE"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

For reference, this is the directory structure of final solution.
```
ex2.3
  │   go.mod
  │   main.go
  │
  └───popcount
          popcount.go
          popcount_test.go
```

We'll first initialize the module using `go mod init ex2.3` command. Then we'll duplicate the code from the book.

Inside popcount directory, we'll create popcount.go file which will contain the example code from the book.

{{< highlight go "title=popcount/popcount.go,linenos=table,hl_lines=" >}}
package popcount

// pc[i] is the population count of i.
var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&1)
	}
}

// PopCount returns the population count (number of set bits) of x.
func PopCount(x uint64) int {
	return int(pc[byte(x>>(0*8))] +
		pc[byte(x>>(1*8))] +
		pc[byte(x>>(2*8))] +
		pc[byte(x>>(3*8))] +
		pc[byte(x>>(4*8))] +
		pc[byte(x>>(5*8))] +
		pc[byte(x>>(6*8))] +
		pc[byte(x>>(7*8))])
}
{{< /highlight >}}

Now we'll add *popcountLoop* function in the *popcount.go* file which will use for loop instead of one line statement.

{{< highlight go "title=popcount/popcount.go,linenostart=24,linenos=table,hl_lines=" >}}
func PopCountLoop(x uint64) int {
	var result byte
	for i := 0; i < 8; i++ {
		result += pc[byte(x>>(i*8))]
	}
	return int(result)
}
{{< /highlight >}}

Before running benchmarks, we must confirm that both functions *PopCount* and *PopCountLoop* functions produce same results. We'll create *main.go* file to do so.

{{< highlight go "title=main.go,linenos=table,linenostart=,hl_lines=" >}}
package main

import (
	"fmt"

	"ex2.3/popcount"
)

func main() {
	input := uint64(28)
	fmt.Println("result from PopCount", popcount.PopCount(input))
	fmt.Println("result from PopCountLoop", popcount.PopCountLoop(input))
}
{{< /highlight >}}

I ran it with different input values and they gave same results.

Now let's add benchmarks for both the functions in *popcount_test.go* file.

{{< highlight go "title=popcount/popcount_test.go,linenos=table,linenostart=,hl_lines=" >}}
package popcount_test

import (
	"testing"

	"ex2.3/popcount"
)

func BenchmarkPopCount(b *testing.B) {
	for i := 0; i < b.N; i++ {
		popcount.PopCount(uint64(i))
	}
}

func BenchmarkPopCountLoop(b *testing.B) {
	for i := 0; i < b.N; i++ {
		popcount.PopCountLoop(uint64(i))
	}
}
{{< /highlight >}}

We'll compare the two functions by running the benchmarks using `go test -bench=Benchmark`

{{< showimage "017.png" "Console output of benchmark." "800x webp text" >}}

Clearly, the *PopCount* function takes almost 10 times less time than *PopCountLoop* function. Single line execution in *PopCount* is much more efficient than loop execution in *PopCountLoop*.

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
