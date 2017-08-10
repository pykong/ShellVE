# ShellVE
Sublime Text 3 plugin to automagically open TerminalView tab with a project's virtual environment already started.

## Why?
I always liked how PyCharm linked a project with a perticular virtual environment. You, easily set it up once. Then you never need to remember the correct virtual environment to start in you shell.  One project, one virtual environment. And you project automatically runs with the correct one.
The Virtualenv plugin for Sublime Text makes a similar linkage possible, but it is only for build systems. If you need more control, e.g. when wnating to install libs to your VE, you are going to need a shell.
ShellVE fills that gap for you.

## Installation
Do it via PackageControl. You likely know how to. (Else see [PackageControl Usage](https://packagecontrol.io/docs/usage).)

### Satisfy dependencies
As the plugin relies on TerminalView as the terminal emulator and sole dependency, it might be neccessary to run PackageControl: Satisfy dependencies after installing ShellVE.

## Usage
### 1. Make sure virtual environment path is included into your .sublime-project:

        [
              "settings": {
                  "python_interpreter": "/home/user/.virtualenvs/example/bin/python"
              }
        ]
        
Note: This is the same format for specifying the VE path as used in the essential python development plugin Anaconda. Yet, the format is different from that used in the plugin Virtualenv.

#### 2a. Just open the project and a view with a shell window with your virtual environment already started will automatically open.
          
How cool is that?        
This is dependend on the sophisticated terminal plugin [TerminalView](https://github.com/Wramberg/TerminalView) by the ingenious Wramberg.          

#### 2b. Alternatively open via keybinding.

This is useful if you closed the automatically spawnded TerminalView.

Default keybindings:

Linux: <kbd>ctrl</kbd> + <kbd>super</kbd> + <kbd>v</kbd>

## Limitations
1. Currently works only on Linux. I am not going to expand it to other platforms, yet I will welcome any pull requests in this regard.

2. Currently only works with TerminalView as the dependend terminal plugin. There are other great terminal emulators for Sublime Text, like [Terminal](works) or [Glue](https://packagecontrol.io/packages/Glue). I am not going to expand it to other terminal plugins though either. Yet, also welcome regarding pull requests.

3. Environment variables are not inherited from the virtual environment currently

## TODO
- Making sure terminal is always started in project folder.
- Ensure environment variables are always the same, irrespective if a virtual environment is started in the system terminal or ShellVE.

## Contributors
- A big ThankYou to [Wramberg](https://github.com/Wramberg/TerminalView) for providing the amazing TerminalView plugin.
