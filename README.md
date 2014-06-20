LessMe
======
A Sublime Text 3 plugin for automatically compiling .less file to .css as well as source map file when it be saved.  


import tag supported
----------
When importing a another less file by using **import** tag in main.less, just like this:
```less
@import url("submodule.less")
...
```
and you should add the below code in the submodule.less's **first line**.
```
//@module ..main.less
```

And then, when the submodule.less be saved, the main.less will be compiled to css as well.  

Dependencies
----------

[node.js][1]  
[less][2] module  

Installation
-------

1.[Download][1] and install node.js   
2.Install less module through npm:  
```shell
npm install -g less  
```
3.Download LessMe and drop to your Sublime Text Packages Directory.  

  [1]: http://nodejs.org/
  [2]: http://lesscss.org/