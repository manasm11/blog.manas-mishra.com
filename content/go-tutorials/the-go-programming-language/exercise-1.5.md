+++
title = 'Exercise 1.5'
weight = 90
hidden = true
question = "Change the Lissajous program’s color palette to green on black, for added authenticity. To create the web color #RRGGBB, use color.RGBA{0xRR, 0xGG, 0xBB, 0xff}, where each pair of hexadecimal digits represents the intensity of the red, green, or blue component of the pixel."
date = "2023-11-15T05:58:51+05:30"
ytcode = "NJyA5Paefx4"
+++

{{< exercisequestion >}}
{{< ytvideo >}}

We'll start by duplicating the code from the book in *main.go* file.

{{< highlight go "title=main.go,linenos=table" >}}
// Lissajous generates GIF animations of random Lissajous figures.
package main

import (
    "image"
    "image/color"
    "image/gif"
    "io"
    "math"
    "math/rand"
    "os"
)

var palette = []color.Color{color.White, color.Black}

const (
    whiteIndex = 0 // first color in palette
    blackIndex = 1 // next color in palette
)

func main() {
    lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
    const (
        cycles  = 5     // number of complete x oscillator revolutions
        res     = 0.001 // angular resolution
        size    = 100   // image canvas covers [-size..+size]
        nframes = 64    // number of animation frames
        delay   = 8     // delay between frames in 10ms units
    )
    freq := rand.Float64() * 3.0 // relative frequency of y oscillator
    anim := gif.GIF{LoopCount: nframes}
    phase := 0.0 // phase difference
    for i := 0; i < nframes; i++ {
        rect := image.Rect(0, 0, 2*size+1, 2*size+1)
        img := image.NewPaletted(rect, palette)
        for t := 0.0; t < cycles*2*math.Pi; t += res {
            x := math.Sin(t)
            y := math.Sin(t*freq + phase)
            img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5),
                blackIndex)
        }
        phase += 0.1
        anim.Delay = append(anim.Delay, delay)
        anim.Image = append(anim.Image, img)
    }
    gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}
{{< / highlight >}}

Let's run the program to see the output. We'll execute `go run main.go > bow.gif`

{{% notice note %}}
If you are working on Windows, make sure to run the command in Command Prompt, not Power Shell. This is because Power Shell changes the newline characters to carriage returns, this causes issues to render gif.
{{% /notice %}}

{{< figure src="/img/bow.gif" caption="bow.gif" alt="output of bow.gif">}}

Now we'll make some changes to make the gif display green on black.
{{< highlight diff "title=main.go,linenos=table,linenostart=14" >}}
- var palette = []color.Color{color.White, color.Black}
+ var palette = []color.Color{color.Black, color.RGBA{0x00, 0xff, 0x00, 0xff}}

const (
-   whiteIndex = 0 // first color in palette
+   backgroundIndex = 0 // first color in palette
-   blackIndex = 1 // next color in palette
+   colorIndex      = 1 // next color in palette
)
{{< / highlight >}}

Here is the final *main.go* file.

{{< highlight go "linenos=table,title=main.go">}}
// Lissajous generates GIF animations of random Lissajous figures.
package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
)

var palette = []color.Color{color.Black, color.RGBA{0x00, 0xff, 0x00, 0xff}}

const (
	backgroundIndex = 0 // first color in palette
	colorIndex      = 1 // next color in palette
)

func main() {
	lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
	const (
		cycles  = 5     // number of complete x oscillator revolutions
		res     = 0.001 // angular resolution
		size    = 100   // image canvas covers [-size..+size]
		nframes = 64    // number of animation frames
		delay   = 8     //delay between frames in 10ms units
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), colorIndex)
		}
		phase += 0.1
		anim.Delay = append(anim.Delay, delay)
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}
{{< / highlight >}}

Now let's create another gif file *gob.gif* using the command: `go run main.go > gob.gif`. Here is the output:

{{< figure src="/img/gob.gif" caption="gob.gif" alt="output of gob.gif">}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}