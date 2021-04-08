imbot
==========================
"imbot" for making a bot to control any website from json file.

.. image:: https://travis-ci.com/byRo0t96/imbot.svg?branch=main

Installation
============

.. code::

    pip install imbot

Usage
=====
.. code:: python

    from imbot import imbot

    p1=imbot("<JSON_FILE_PATH>","<OPTION>",<TIME_EVERY_OPERATION>)
    p1.run() # for run imbot
    p1.end() # close


This is an example for login to github and go your profile:
.. code:: json
{
    "login":{
        "url":"https://github.com/",
        "xpaths":[
	    {"xpath":"/html/body/div[1]/header/div/div[2]/div[2]/a[1]","opt":"click"},
	    {"xpath":"//input[@name=\"login\"]","opt":"put","data":"<YOUR_EMAIL>"},
	    {"xpath":"//input[@name=\"password\"]","opt":"put","data":"<YOUR_PASSWORD>"},
	    {"xpath":"//input[@type=\"submit\"]","opt":"click"},
	    {"xpath":"//*[@id=\"otp\"]","opt":"put"},
	    {"xpath":"//*[@id=\"login\"]/div[3]/form/button","opt":"click"},
	    {"xpath":"/html/body/div[1]/header/div[7]/details/summary/span[2]","opt":"click"},
	    {"xpath":"/html/body/div[1]/header/div[7]/details/details-menu/a[1]","opt":"click"}
	]
    }
}


.. begin changelog

Changelog
=========

0.0.1
-----
- First public release.

.. end changelog
