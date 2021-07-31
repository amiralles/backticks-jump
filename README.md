# backticks-jump
A small Sublime Text plugin to quickly jump back and forth between the previous and next cursor positions. (It works similarly to vim's bultin backtick-backtick command.)


### Installation
At the moment, there is no "official" package to install this plugin, but you can still uset it by copying `backticks_jump.py` into `<Sublime's Installation Path>/Packages/User`

Once you did that, just add a shortcut to run the `backticks_jump` and jump back and forth.

```
{ "keys": ["ctrl+,"], "command": "backticks_jump"}
```

If you are using the `Vintage` package you can get the exact same shortcut you use in vim by adding these lines to you key bindings.

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

### TODO
Create a package so that it's easier to install.
