+++
title = 'Exercise 1.1'
weight = 50
# hidden = true
question = "Modify the echo program to also print os.Args[0], the name of the command that invoked it."
date = "2023-11-15T05:58:51+05:30"
ytcode = "94Id2JlQmj0"
+++

{{< exercisequestion >}}

{{< ytvideo >}}

There is not much of of explanation needed. We just have to modify the echo2 program and replace `strings.Join(os.Args[1:], " ")` to `strings.Join(os.Args, " ")`.

Here is the final `main.go` file.

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Println(strings.Join(os.Args, " "))
}
```

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}