+++
title = 'Exercise 2.5'
weight = 200
hidden = true
question = "The expression x&(x-1) clears the rightmost non-zero bit of x. Write a version of PopCount that counts bits by using this fact, and assess its performance."
date = "2023-11-18T02:41:03+05:30"
ytcode = "g-AerVrfoPw"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

For reference, this is the directory structure of the final solution:

```
ex2.5
    │   go.mod
    │
    └───popcount
            popcount.go
            popcount_test.go
```

Let's start with initializing the module with `go mod init ex2.5` command and create *popcount/popcount.go* file with the example code from book.

{{< highlight go "title=popcount/popcount.go,linenos=table,linenostart=,hl_lines=" >}}
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

In the question, we are given that `x&(x-1)` removes the rightmost non-zero bit of x. We will use this fact to keep removing the rightmost bit until all bits are zero. Each time we remove a bit, we'll update a counter value. When the value is zero, the counter will give us the number of bits in original value.

Let's implement this logic in *PopCount2* function:

{{< highlight go "title=popcount/popcount.go,linenos=table,linenostart=23,hl_lines=" >}}
func PopCount2(x uint64) int {
	var result int
	for x != 0 {
		x = x & (x - 1)
		result++
	}
	return result
}
{{< /highlight >}}

Before running benchmarks, let's check if both functions give out same outputs. We'll do so by creating a test in *popcount/popcount_test.go* file.

{{< highlight go "title=popcount/popcount_test.go,linenos=table,linenostart=,hl_lines=" >}}
package popcount_test

import (
	"testing"

	"ex2.5/popcount"
)

func TestBothPopCountGiveSameResults(t *testing.T) {
	for i := uint64(0); i < 200; i++ {
		if popcount.PopCount(i) != popcount.PopCount2(i) {
			t.Fatalf("popcount values are not equal for i=%d", i)
		}
	}
}
{{< /highlight >}}

Upon running the test with `go test ./popcount` gives the "ok" output, which means both functions produce same output. Now let's create benchmarks for both the functions.

{{< highlight go "title=popcount/popcount_test.go,linenos=table,linenostart=16,hl_lines=" >}}
func BenchmarkPopCount(b *testing.B) {
	for i := 0; i < b.N; i++ {
		popcount.PopCount(uint64(i))
	}
}

func BenchmarkPopCount2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		popcount.PopCount2(uint64(i))
	}
}
{{< /highlight >}}

Running the benchmark with `go test -bench ./popcount` gives this result:

{{< showimage "019" "Output of benchmark" "800x webp text" >}}

Clearly, the *PopCount* is much more efficient than *PopCount2*.

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}