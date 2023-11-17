+++
title = 'Exercise 2.2'
weight = 150
hidden = true
question = "Write a general-purpose unit-conversion program analogous to cf that reads numbers from its command-line arguments or from the standard input if there are no arguments, and converts each number into units like temperature in Celsius and Fahrenheit, length in feet and meters, weight in pounds and kilograms, and the like."
date = "2023-11-15T05:58:51+05:30"
ytcode = "1xOdJszUB9I"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

For reference, this is the directory structure of the final solution.
```
ex2.2
   │   go.mod
   │   main.go
   │
   ├───lenconv
   │       conv.go
   │       lenconv.go
   │
   ├───tempconv
   │       conv.go
   │       tempconv.go
   │
   └───wgtconv
           conv.go
           wgtconv.go
```
We'll initialize the project with `go mod init ex2.2`.

Now let's start with the most straightforward package: *tempconv*. We just need to duplicate the code example from book.

{{< highlight go "title=tempconv/tempconv.go,linenos=table" >}}
// Package tempconv performs Celsius and Fahrenheit conversions.
package tempconv

import "fmt"

type Celsius float64
type Fahrenheit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreezingC     Celsius = 0
	BiolingC      Celsius = 100
)

func (c Celsius) String() string    { return fmt.Sprintf("%g°C", c) }
func (f Fahrenheit) String() string { return fmt.Sprintf("%g°F", f) }
{{< /highlight >}}

{{< highlight go "title=tempconv/conv.go,linenos=table" >}}
package tempconv

// CToF converts a Celsius temperature to Fahrenheit.
func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

// FToC converts a Fahrenheit temperature to Celsius.
func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }
{{< /highlight >}}

Now, let's create *lenconv* package which will have functions to convert meter to foot and vice versa.
{{< highlight go "title=lenconv/lenconv.go,linenos=table" >}}
// Package lenconv performs Foot and Meter conversions.
package lenconv

import "fmt"

type Foot float64
type Meter float64

const (
	oneMeter Foot = 3.28084
)

func (f Foot) String() string  { return fmt.Sprintf("%gft", f) }
func (m Meter) String() string { return fmt.Sprintf("%gm", m) }
{{< /highlight >}}

{{< highlight go "title=lenconv/conv.go,linenos=table" >}}
package lenconv

// MToF converts Meter to Foot.
func MToF(m Meter) Foot { return Foot(m) * oneMeter }

// FToM converts Foot to Meter.
func FToM(f Foot) Meter { return Meter(f / oneMeter) }
{{< /highlight >}}

At last, we'll create a *wgtconv* package which will convert Kilogram to Pound and vice versa.

{{< highlight go "title=wgtconv/wgtconv.go,linenos=table" >}}
// Package wgtconv performs Kilogram and Pound conversions.
package wgtconv

import "fmt"

type Kilogram float64
type Pound float64

const (
	oneKg Pound = 2.20462
)

func (kg Kilogram) String() string { return fmt.Sprintf("%gkg", kg) }
func (lbs Pound) String() string   { return fmt.Sprintf("%glbs", lbs) }
{{< /highlight >}}

{{< highlight go "title=wgtconv/conv.go,linenos=table" >}}
package wgtconv

// KToP converts Kilogram to Pound.
func KToP(kg Kilogram) Pound { return Pound(kg) * oneKg }

// PToK converts Pound to Kilogram.
func PToK(p Pound) Kilogram { return Kilogram(p / oneKg) }
{{< /highlight >}}

Now we'll use these three packages in *main.go* to take input from user, either as cli argument or through input prompt, and convert the number into different units.

{{< highlight go "title=main.go,linenos=table" >}}
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"ex2.2/lenconv"
	"ex2.2/tempconv"
	"ex2.2/wgtconv"
)

func main() {
	if len(os.Args) > 1 {
		for _, input := range os.Args[1:] {
			num, err := strconv.ParseFloat(input, 64)
			if err != nil {
				fmt.Println("Invalid number", err)
				os.Exit(1)
			}
			convertAndPrint(num)
		}
	} else {
		for {
			consoleReader := bufio.NewReader(os.Stdin)
			fmt.Print("enter a number> ")
			input, _ := consoleReader.ReadString('\n')
			input = strings.TrimSpace(input)
			num, err := strconv.ParseFloat(input, 64)
			if err != nil {
				fmt.Println("Invalid number", err)
				os.Exit(1)
			}
			convertAndPrint(num)
		}
	}
}

func convertAndPrint(n float64) {
	var (
		celcius    = tempconv.Celsius(n)
		fahrenheit = tempconv.Fahrenheit(n)
		foot       = lenconv.Foot(n)
		meter      = lenconv.Meter(n)
		kg         = wgtconv.Kilogram(n)
		pound      = wgtconv.Pound(n)
	)

	fmt.Println(celcius, "is", tempconv.CToF(celcius))
	fmt.Println(fahrenheit, "is", tempconv.FToC(fahrenheit))
	fmt.Println(foot, "is", lenconv.FToM(foot))
	fmt.Println(meter, "is", lenconv.MToF(meter))
	fmt.Println(kg, "is", wgtconv.KToP(kg))
	fmt.Println(pound, "is", wgtconv.PToK(pound))
}
{{< /highlight >}}

Let's run the command `go run main.go -40 50` to check the output.
{{< showimage "016" "Output of the command." "400x webp text" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
