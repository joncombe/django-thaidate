django-thaidate
===============

A drop-in replacement for the "[date](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#date)" django templatetag. The only difference is that it shows Thai years, not Gregorian calendar ones.

#### Installation
 - `pip install django-thaidate`
 - Add `thaidate` to `INSTALLED_APPS` in `settings.py`

#### Usage
```
{% load thaidate %}

{{ value|date:"D d M Y" }}  # อา. 10 ก.พ. 2019
{{ value|thaidate:"D d M Y" }}  # อา. 10 ก.พ. 2562
```

#### A reminder to self
Are you trying to show a Thai date on a page rendered with another language? Use the built-in `language` flag:

```
{% load i18n thaidate %}

{% language 'th' %}
{{ value|date:"D d M Y" }}  # อา. 10 ก.พ. 2019
{{ value|thaidate:"D d M Y" }}  # อา. 10 ก.พ. 2562
{% endlanguage %}
```