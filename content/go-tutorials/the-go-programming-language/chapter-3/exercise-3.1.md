+++
title = 'Exercise 3.1'
weight = 220
question = "If the function f returns a non-finite float64 value, the SVG file will contain invalid <polygon> elements (although many SVG renderers handle this gracefully). Modify the program to skip invalid polygons."
date = "2023-11-18T12:09:01+05:30"
ytcode = "OW5pZsS3w8w"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

Let's start by duplicating the code example from book.

{{< highlight go "title=main.go,linenos=table,linenostart=1,hl_lines=" >}}
// Surface computes an SVG rendering of a 3-D surface function.
package main

import (
    "fmt"
    "math"
)

const (
    width, height = 600, 320            // canvas size in pixels
    cells         = 100                 // number of grid cells
    xyrange       = 30.0                // axis ranges (-xyrange..+xyrange)
    xyscale       = width / 2 / xyrange // pixels per x or y unit
    zscale        = height * 0.4        // pixels per z unit
    angle         = math.Pi / 6         // angle of x, y axes (=30°)
)

var sin30, cos30 = math.Sin(angle), math.Cos(angle) // sin(30°), cos(30°)

func main() {
    fmt.Printf("<svg xmlns='http://www.w3.org/2000/svg' "+
        "style='stroke: grey; fill: white; stroke-width: 0.7' "+
        "width='%d' height='%d'>", width, height)
    for i := 0; i < cells; i++ {
        for j := 0; j < cells; j++ {
            ax, ay := corner(i+1, j)
            bx, by := corner(i, j)
            cx, cy := corner(i, j+1)
            dx, dy := corner(i+1, j+1)
            fmt.Printf("<polygon points='%g,%g %g,%g %g,%g %g,%g'/>\n",
                ax, ay, bx, by, cx, cy, dx, dy)
        }
    }
    fmt.Println("</svg>")
}

func corner(i, j int) (float64, float64) {
    // Find point (x,y) at corner of cell (i,j).
    x := xyrange * (float64(i)/cells - 0.5)
    y := xyrange * (float64(j)/cells - 0.5)

    // Compute surface height z.
    z := f(x, y)

    // Project (x,y,z) isometrically onto 2-D SVG canvas (sx,sy).
    sx := width/2 + (x-y)*cos30*xyscale
    sy := height/2 + (x+y)*sin30*xyscale - z*zscale
    return sx, sy
}

func f(x, y float64) float64 {
    r := math.Hypot(x, y) // distance from (0,0)
    return math.Sin(r) / r
}
{{< /highlight >}}

We must try to run the file with `go run main.go > temp.svg`. You can download the svg from {{< downloadablelink "/img/temp.svg" "this link 'temp.svg'" >}}. If you look at {{< downloadablelink "/img/temp.svg" "this temp.svg file" >}}, there are **1001** lines. We'll change the code to prevent polygons with non-finite *f* function values and see how many lines the new svg has.

{{< showimage "020" "Screenshot of temp.svg" "400x webp text" >}}

To check a *float64* is a finite number or not, we'll use two functions from *math* package: `math.IsInf` and `math.IsNan`.

{{< define "math.IsInf" >}}
package math // import "math"

func IsInf(f float64, sign int) bool
    IsInf reports whether f is an infinity, according to sign. If sign > 0,
    IsInf reports whether f is positive infinity. If sign < 0, IsInf reports
    whether f is negative infinity. If sign == 0, IsInf reports whether f is
    either infinity.
{{< /define >}}

{{< define "math.IsNan">}}
package math // import "math"

func IsNaN(f float64) (is bool)
    IsNaN reports whether f is an IEEE 754 “not-a-number” value.
{{< /define >}}

Using these functions, we'll create a function `isFinite` which takes a float64 and return if the float64 is finite or not.

{{< highlight go "title=main.go,linenos=table,linenostart=56,hl_lines=" >}}
func isFinite(num float64) bool {
	return !math.IsInf(num, 0) && !math.IsNaN(num)
}
{{< /highlight >}}

Now, we'll use the *isFinite* function in *corner* function. We'll make few changes in the *main.go*.

{{< highlight go "title=main.go,linenos=table,hl_lines=26-41 49 60" >}}
// Surface computes an SVG rendering of a 3-D surface function.
package main

import (
	"fmt"
	"math"
)

const (
	width, height = 600, 320            // canvas size in pixels
	cells         = 100                 // number of grid cells
	xyrange       = 30.0                // axis ranges (-xyrange..+xyrange)
	xyscale       = width / 2 / xyrange // pixels per x or y unit
	zscale        = height * 0.4        // pixels per z unit
	angle         = math.Pi / 6         // angle of x, y axes (=30°)
)

var sin30, cos30 = math.Sin(angle), math.Cos(angle) // sin(30°), cos(30°)

func main() {
	fmt.Printf("<svg xmlns='http://www.w3.org/2000/svg' "+
		"style='stroke: grey; fill: white; stroke-width: 0.7' "+
		"width='%d' height='%d'>", width, height)
	for i := 0; i < cells; i++ {
		for j := 0; j < cells; j++ {
			ax, ay, ok := corner(i+1, j)
			if !ok {
				continue
			}
			bx, by, ok := corner(i, j)
			if !ok {
				continue
			}
			cx, cy, ok := corner(i, j+1)
			if !ok {
				continue
			}
			dx, dy, ok := corner(i+1, j+1)
			if !ok {
				continue
			}
			fmt.Printf("<polygon points='%g,%g %g,%g %g,%g %g,%g'/>\n",
				ax, ay, bx, by, cx, cy, dx, dy)
		}
	}
	fmt.Println("</svg>")
}

func corner(i, j int) (float64, float64, bool) {
	// Find point (x,y) at corner of cell (i,j).
	x := xyrange * (float64(i)/cells - 0.5)
	y := xyrange * (float64(j)/cells - 0.5)

	// Compute surface height z.
	z := f(x, y)

	// Project (x,y,z) isometrically onto 2-D SVG canvas (sx,sy).
	sx := width/2 + (x-y)*cos30*xyscale
	sy := height/2 + (x+y)*sin30*xyscale - z*zscale
	return sx, sy, isFinite(z)
}

func f(x, y float64) float64 {
	r := math.Hypot(x, y) // distance from (0,0)
	return math.Sin(r) / r
}

func isFinite(num float64) bool {
	return !math.IsInf(num, 0) && !math.IsNaN(num)
}
{{< /highlight >}}

After running the `go run main.go > temp2.svg`, we get the svg that looks similar. But if you look at the {{< downloadablelink "/img/temp2.svg" "actual svg file (temp2.svg)" >}}, there are **997** lines.

{{< showimage "021" "Difference between temp.svg and temp2.svg lines" "800x webp text" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}