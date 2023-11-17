+++
title = 'Exercise 1.2'
weight = 60
# hidden = true
question = "Modify the echo program to print the index and value of each of its arguments, one per line."
date = "2023-11-15T05:58:51+05:30"
ytcode = "kX_7OZYz73w"
+++

{{< exercisequestion >}}

{{< ytvideo >}}

This exercise just requires you to know about the for-each loop, which by itself gives you the index and the value which you can easily print.

Here is the small code snippet of the solution:

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	for i, v := range os.Args {
		fmt.Println(i, v)
	}
}
```

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}