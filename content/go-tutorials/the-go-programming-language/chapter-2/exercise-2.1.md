+++
title = 'Exercise 2.1'
weight = 140
# hidden = true
question = "Add types, constants, and functions to tempconv for processing temperatures in the Kelvin scale, where zero Kelvin is −273.15°C and a difference of 1K has the same magnitude as 1°C."
date = "2023-11-15T05:58:51+05:30"
ytcode = "uTLCD4FVwZs"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

For reference, this is the directory of our final solution.
```
ex2.1
   │───go.mod
   │───main.go
   │
   └───tempconv
        │──conv.go
        └──tempconv.go
```

We will initialize the project with `go mod init tempconv`. Then we will imitate the above mentioned directory structure.

{{< highlight go "title=tempconv.go,linenos=table" >}}
// Package tempconv performs Celsius and Fahrenheit conversions.
package tempconv

import "fmt"

type Celsius float64
type Fahrenheit float64

const (
    AbsoluteZeroC Celsius = -273.15
    FreezingC     Celsius = 0
    BoilingC      Celsius = 100
)

func (c Celsius) String() string    { return fmt.Sprintf("%g°C", c) }
func (f Fahrenheit) String() string { return fmt.Sprintf("%g°F", f) }
{{< /highlight >}}

{{< highlight go "title=conv.go,linenos=table" >}}
package tempconv

// CToF converts a Celsius temperature to Fahrenheit.
func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

// FToC converts a Fahrenheit temperature to Celsius.
func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }
{{< /highlight >}}

In *tempconv.go* file, we'll add Kelvin data type and string method.
{{< highlight go "title=tempconv.go,linenos=table,hl_lines=8 18" >}}
// Package tempconv performs Celsius and Fahrenheit conversions.
package tempconv

import "fmt"

type Celsius float64
type Fahrenheit float64
type Kelvin float64

const (
    AbsoluteZeroC Celsius = -273.15
    FreezingC     Celsius = 0
    BoilingC      Celsius = 100
)

func (c Celsius) String() string    { return fmt.Sprintf("%g°C", c) }
func (f Fahrenheit) String() string { return fmt.Sprintf("%g°F", f) }
func (k Kelvin) String() string     { return fmt.Sprintf("%gK", k) }
{{< /highlight >}}

In *conv.go*, we'll add four new functions to convert Kelvin to Celsius and Fahrenheit and vice versa.
{{< highlight go "title=conv.go,linenos=table,hl_lines=9-19" >}}
package tempconv

// CToF converts a Celsius temperature to Fahrenheit.
func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

// FToC converts a Fahrenheit temperature to Celsius.
func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }

// CToK converts a Celsius temperature to Kelvin.
func CToK(c Celsius) Kelvin { return Kelvin(c - AbsoluteZeroC) }

// KToC converts a Kelvin temperature to Celsius.
func KToC(k Kelvin) Celsius { return Celsius(k) + AbsoluteZeroC }

// KToF converts a Kelvin temperature to Fahrenheit.
func KToF(k Kelvin) Fahrenheit { return CToF(KToC(k)) }

// FToK converts a Fahrenheit temperature to Kelvin.
func FToK(f Fahrenheit) Kelvin { return CToK(FToC(f)) }
{{< /highlight >}}

To test the package, we'll create *main.go* file and add some tests.

{{< highlight go "title=main.go,linenos=table,hl_lines=">}}
package main

import (
	"fmt"
	"tempconv/tempconv"
)

func main() {
	var (
		c1 = tempconv.Celsius(-273.15)
		c2 = tempconv.Celsius(273.15)
		k1 = tempconv.Kelvin(0)
		f  = tempconv.Fahrenheit(-40)
	)

	fmt.Println(c1, "is", tempconv.CToF(c1))
	fmt.Println(c1, "is", tempconv.CToK(c1))
	fmt.Println(c2, "is", tempconv.CToF(c2))
	fmt.Println(c2, "is", tempconv.CToK(c2))
	fmt.Println(k1, "is", tempconv.KToC(k1))
	fmt.Println(k1, "is", tempconv.KToF(k1))
	fmt.Println(f, "is", tempconv.FToC(f))
	fmt.Println(f, "is", tempconv.FToK(f))
}
{{< /highlight >}}

Here is the output of running `go run main.go` command.
{{< showimage "015" "console output of running the program" "400x webp text" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
