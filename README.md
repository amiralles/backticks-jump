# backticks-jump
A small Sublime Text plugin ispired by _**vim's bultin backtick-backtick command**_ that allows you to jump back and forth between the previous and next cursor position.

So instead of hitting `ctrl+-` to jump to the previous position and then `ctrl+shift+-` to get back, you just hit a single shortcut of your choice.

And of course, it can be mapped to `backtick backtick` if you are running "Vintange Mode."


![backticks-jump](https://user-images.githubusercontent.com/2120820/127752340-76bac089-5550-4484-980f-aa6edc8fa4cb.gif)



### Installation
At the moment, there is no "official" package to install this plugin, but you can still uset it by copying `backticks_jump.py` into `<Sublime's Installation Path>/Packages/User`

Once you did that, just add a shortcut to run the `backticks_jump` and jump back and forth.

```
{ "keys": ["ctrl+,"], "command": "backticks_jump"}
```


If you are using the `Vintage` package you can get the exact same shortcut you use in `vim` by adding these lines to you key-bindings config file.

```
  // jumps back/forth between the previous and next cursor positions.
  { "keys": ["`", "`"],
      "context": [
          { "key": "setting.command_mode", "operand": true },
          { "key": "setting.is_widget", "operand": false }
      ],
    "command": "backticks_jump"
  },
````

More custom key-bindings [here](https://gist.github.com/amiralles/c05b88c381cdd0ee20a8d74043fb0a06)

### TODO
Create a package so that it's easier to install.
