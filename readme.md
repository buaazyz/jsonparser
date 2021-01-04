# my JSON parser

imitate minilang to realize a simple json parser



## grammar

```
kvs  -> LBRACE pair (COMMA pair)* RBRACE

pair -> STRING COLON val

val  -> kvs
	 -> list
 	 -> atom

list -> LSQUARE (val) (COMMA val)* RSQUARE

atom -> STRING | INT |FLOAT




```







## Process

**begin on 2021.1.4**

1）complete  lexer    2021.1.4

2）complete  parser 2021.1.4

