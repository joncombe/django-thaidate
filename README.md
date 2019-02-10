django-thaidate
===============

A drop-in replacement for the "[date](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#date)" django templatetag. The only difference is that it shows Thai years, not Gregorian calendar ones.

The `TIME_ZONE` needs to be set to `'Asia/Bangkok'` in your `settings.py`

```
{{ value|date:"D d M Y" }}  # อา. 10 ก.พ. 2019

{{ value|thaidate:"D d M Y" }}  # อา. 10 ก.พ. 2562
```
