+++
title = 'Exercise 3.3: Adding Color to SVG'
weight = 230
question = "Color each polygon based on its height, so that the peaks are colored red (#ff0000) and the valleys blue (#0000ff)."
date = "2023-11-19T10:15:00+05:30"
ytcode = "IYlauRWCbLI"
+++
{{< exercisequestion >}}
{{< ytvideo >}}

We'll start the exercise with duplicating the code from the book.

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

You can run the modified file with `go run main.go > temp.svg`. You can download the generated SVG from {{< downloadablelink "/img/temp.svg" "this link 'temp.svg'" >}}. 

{{< showimage "020" "Screenshot of temp.svg" "400x webp text" >}}

Since we need to color svg according to height, we would need to return height also from the *corner* function. Then we'll calculate the average height of all the corners and use it to create color conditionally. One observation is that all the values of *z* were from *-1 to +1*. Here is the final code:

{{% notice info %}}
To add color in \<polygon\> tag, we need to add **fill** attribute.
{{% /notice %}}

{{% notice info %}}
To generate two digit hex code from integer in *Sprinf*, we have to use **%02X** verb.
{{% /notice %}}


{{< highlight go "title=main.go,linenos=table,linenostart=1,hl_lines=26-39 44 55" >}}
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
			ax, ay, az := corner(i+1, j)
			bx, by, bz := corner(i, j)
			cx, cy, cz := corner(i, j+1)
			dx, dy, dz := corner(i+1, j+1)
			avgZ := (az + bz + cz + dz) / 4
			var hexCode string
			if avgZ > 0 {
				hexCode = fmt.Sprintf("#%02X%02X%02X", int64(avgZ*16*16), 0, 0)
			} else {
				hexCode = fmt.Sprintf("#%02X%02X%02X", 0, 0, -int64(avgZ*16*16))
			}
			fmt.Printf("<polygon fill='%s' points='%g,%g %g,%g %g,%g %g,%g'/>\n", hexCode,
				ax, ay, bx, by, cx, cy, dx, dy)
		}
	}
	fmt.Println("</svg>")
}

func corner(i, j int) (float64, float64, float64) {
	// Find point (x,y) at corner of cell (i,j).
	x := xyrange * (float64(i)/cells - 0.5)
	y := xyrange * (float64(j)/cells - 0.5)

	// Compute surface height z.
	z := f(x, y)

	// Project (x,y,z) isometrically onto 2-D SVG canvas (sx,sy).
	sx := width/2 + (x-y)*cos30*xyscale
	sy := height/2 + (x+y)*sin30*xyscale - z*zscale
	return sx, sy, z
}

func f(x, y float64) float64 {
	r := math.Hypot(x, y) // distance from (0,0)
	return math.Sin(r) / r
}
{{< /highlight >}}

You can run generate the svg file using `go run main.go > colorful.svg`. You may download the file through {{< downloadablelink "/img/colorful.svg" "this link" >}}.


{{< showimage "022" "Colored polygons in SVG rendering" "800x webp text" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}
