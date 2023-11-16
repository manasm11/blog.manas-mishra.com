+++
title = 'Exercise 1.6'
weight = 100
hidden = true
question = "Modify the Lissajous program to produce images in multiple colors by adding more values to palette and then displaying them by changing the third argument of SetColorIndex in some interesting way."
date = "2023-11-15T05:58:51+05:30"
ytcode = "1idWemc1gJw"
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

Let's run the program to see the output. We'll execute `go run main.go > abc.gif`

{{% notice note %}}
If you are working on Windows, make sure to run the command in Command Prompt, not Power Shell. This is because Power Shell changes the newline characters to carriage returns, this causes issues to render gif.
{{% /notice %}}

{{< figure src="/img/bow.gif" caption="abc.gif" alt="output of abc.gif" >}}

To use multiple colors, in the gif, we only need to change two lines of code. 

{{< highlight diff "title=main.go" >}}
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

- var palette = []color.Color{color.White, color.Black}
+ var palette = []color.Color{color.White, color.Black, color.RGBA{0xff, 0x00, 0x00, 0xff}}

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
-               blackIndex)
+               uint8(i)%2+1)
        }
        phase += 0.1
        anim.Delay = append(anim.Delay, delay)
        anim.Image = append(anim.Image, img)
    }
    gif.EncodeAll(out, &anim) // NOTE: ignoring encoding errors
}
{{< / highlight >}}

We'll get a gif with black and red colors alternating in gif. Lets save output to *bcd.gif* with this command `go run main.go > bcd.gif`.

{{< figure src="/img/bcd.gif" caption="bcd.gif" alt="output of bcd.gif" >}}

The in hexadecimal, *ff* is the largest number and *00* is smallest. So to get pure red color, we set *0xff* into *R* value in RGBA struct and 0x00 in the *G* and *B* parts. The *A* value in *RGBA* defines transparency, since we want an opaque color, we set it's value as *0xff*.

Since we want the color index to change in every iteration, we use modulo (%) operator with *i* to set the index in each iteration dynamically. We add *1* because we don't want the color to be *0th* index (white color).

To demonstrate and make the code more general, let's add blue color also in the gif. I modified the highlighted lines.

{{< highlight go "title=main.go,linenos=table,hl_lines=14-17 42 46" >}}
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

var palette = []color.Color{color.White, color.Black,
	color.RGBA{0xff, 0x00, 0x00, 0xff}, // RED
	color.RGBA{0x00, 0x00, 0xff, 0xff}, // BLUE
}

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
		delay   = 8     //delay between frames in 10ms units
	)
	freq := rand.Float64() * 3.0 // relative frequency of y oscillator
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0 // phase difference
	for i := 0; i < nframes; i++ {
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		img := image.NewPaletted(rect, palette)
        colorIndex := uint8(i%(len(palette))-1)+1
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

Let's save the gif with black, red and blue colors into *cde.gif* using `go run main.go > cde.gif` command.

{{< figure src="/img/cde.gif" caption="cde.gif" alt="output of cde.gif" >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}