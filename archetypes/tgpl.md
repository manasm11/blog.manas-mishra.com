+++
title = '{{ replace .Name "-" " " | title }}'
weight = {{ math.Mul .Site.Pages.Len 10 }}
hidden = true
question = ""
date = "{{ .Date }}"
ytcode = ""
+++

{{< exercisequestion >}}

{{< ytvideo >}}

content goes here.

```go
The code goes here.
```

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}