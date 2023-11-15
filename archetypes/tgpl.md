+++
title = '{{ replace .Name "-" " " | title }}'
weight = {{ math.Mul .Site.Pages.Len 10 }}
hidden = true
question = ""
date = "{{ .Date }}"
+++