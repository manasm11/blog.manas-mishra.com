+++
title = '{{ replace .Name "-" " " | title }}'
weight = {{ math.Mul .Site.Pages.Len 10 }}
question = ""
date = "{{ .Date }}"
ytcode = ""
+++
{{< exercisequestion >}}
{{< ytvideo >}}

{{< purchasebook link="https://amzn.to/46n8kiI" title="The Go Programming Language by Alan Donovan (Author), Brian Kernighan (Author)" >}}