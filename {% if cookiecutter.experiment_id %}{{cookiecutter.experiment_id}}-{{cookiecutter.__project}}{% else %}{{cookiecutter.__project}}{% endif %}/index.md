---
title: GitLab pages notebook index
---

# Notebooks

## Contents

The following notebooks detail the results for the analyses conducted in this repository:

{% for file in site.static_files %}
{% if file.path contains 'notebooks/' and file.extname == '.html' %}
[{{ file.name | replace: '.html', '' }}]({{ file.path }}) |
{% endif %}
{% endfor %}

---

*This list is automatically generated using the `notebooks/` directory.*
