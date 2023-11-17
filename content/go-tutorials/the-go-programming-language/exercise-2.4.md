+++
title = 'Exercise 2.4'
weight = 170
hidden = true
question = "Write a version of PopCount that counts bits by shifting its argument through 64 bit positions, testing the rightmost bit each time. Compare its performance to the table-lookup version."
date = "2023-11-15T05:58:51+05:30"
ytcode = "TqbiOZENxCg"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

For reference, this is the directory structure of final solution.
```
ex2.4
    │   go.mod
    │   main.go
    │
    └───popcount
            popcount.go
            popcount_test.go
```

We'll first initialize the module using `go mod init ex2.4` command. Then we'll duplicate the code from the book.

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

Now we'll add *PopCount2* function in the *popcount.go* file which will use bit shifting and check for rightmost bit.

{{< highlight go "title=popcount/popcount.go,linenos=table,linenostart=24,hl_lines=" >}}
func PopCount2(x uint64) int {
	var result int
	for i := 0; i < 64; i++ {
		result += int((x >> i) & 1)
	}
	return result
}
{{< /highlight >}}

{{% notice info %}}
Performing "&" operation with any int gives the rightmost bit. If the rightmost value of "n" is 1, n&1 will result in 1, if rightmost bit is 0, the result of n&1 will be 0.
{{% /notice %}}

The *PopCount2* function performs a loop 64 times and each time performs right shift operation. Then we access the rightmost bit using *&1* and add it to the *result* variable.

The *PopCount2* function uses loop. I will create another function *PopCount3* which will use one-line statement instead of loop to see if there are any performance differences.

{{< highlight go "title=popcount/popcount.go,linenos=table,linenostart=32,hl_lines=" >}}
func PopCount3(x uint64) int {
	return int(
		(x>>0)&1 + (x>>1)&1 + (x>>2)&1 + (x>>3)&1 +
			(x>>4)&1 + (x>>5)&1 + (x>>6)&1 + (x>>7)&1 +
			(x>>8)&1 + (x>>9)&1 + (x>>10)&1 + (x>>11)&1 +
			(x>>12)&1 + (x>>13)&1 + (x>>14)&1 + (x>>15)&1 +
			(x>>16)&1 + (x>>17)&1 + (x>>18)&1 + (x>>19)&1 +
			(x>>20)&1 + (x>>21)&1 + (x>>22)&1 + (x>>23)&1 +
			(x>>24)&1 + (x>>25)&1 + (x>>26)&1 + (x>>27)&1 +
			(x>>28)&1 + (x>>29)&1 + (x>>30)&1 + (x>>31)&1 +
			(x>>32)&1 + (x>>33)&1 + (x>>34)&1 + (x>>35)&1 +
			(x>>36)&1 + (x>>37)&1 + (x>>38)&1 + (x>>39)&1 +
			(x>>40)&1 + (x>>41)&1 + (x>>42)&1 + (x>>43)&1 +
			(x>>44)&1 + (x>>45)&1 + (x>>46)&1 + (x>>47)&1 +
			(x>>48)&1 + (x>>49)&1 + (x>>50)&1 + (x>>51)&1 +
			(x>>52)&1 + (x>>53)&1 + (x>>54)&1 + (x>>55)&1 +
			(x>>56)&1 + (x>>57)&1 + (x>>58)&1 + (x>>59)&1 +
			(x>>60)&1 + (x>>61)&1 + (x>>62)&1 + (x>>63)&1)
}
{{< /highlight >}}

Before running benchmarks, let's check if all three functions give out same outputs. I'll create a *main.go* file to do so.

{{< highlight go "title=main.go,linenos=table,linenostart=,hl_lines=" >}}
package main

import (
	"fmt"

	"ex2.4/popcount"
)

func main() {
	var input uint64 = 64
	fmt.Println("popcount", popcount.PopCount(input))
	fmt.Println("popcount2", popcount.PopCount2(input))
	fmt.Println("popcount3", popcount.PopCount3(input))
}
{{< /highlight >}}

I tried running `go run main.go` with changing input value and got same results for all three functions.

Now let's write benchmarks in *popcount/popcount_test.go* file.

{{< highlight go "title=popcount/popcount_test.go,linenos=table,linenostart=,hl_lines=" >}}
package popcount_test

import (
	"testing"

	"ex2.4/popcount"
)

func BenchmarkPopCount3(b *testing.B) {
	for i := 0; i < b.N; i++ {
		popcount.PopCount3(uint64(i))
	}
}

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

Let's run the benchmark using `go test -bench=Benchmark`.

{{< showimage "018" "Output of running benchmarks" "800x webp text" >}}

Clearly, the original *PopCount* function is most optimized and there is not much performance difference between *PopCount2* and *PopCount3*.

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
