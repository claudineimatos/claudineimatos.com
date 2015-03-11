Title: Tricks on YAML
Tags: foreman, yaml
Author: Claudinei Matos
Status: Draft

Today I needed to create a wrapper to Puppet's Apache module so I've did it in the fastest way.


* Associative Array

Array of Hashes:

Desired output:
content_prices: 
  - {country: AU, price: 6990000} 
  - {country: AT, price: 4990000} 
  - {country: BE, price: 4990000}  

Howto on YAML:
content_prices:
  - country: AU
    price: 6990000
  - country: AT
    price: 4990000
  - country: BE
    price: 4990000

reference: http://stackoverflow.com/questions/17173864/how-to-make-a-list-of-associative-array-in-yaml


* Multiline string

variable: ! "content\n
new line content\n
new line #2"

reference: http://stackoverflow.com/questions/3790454/in-yaml-how-do-i-break-a-string-over-multiple-lines
