import sublime
import sublime_plugin
import sys

PLUGIN_NAME = 'ShellVE'

SHELL_TITLE = "TERMINAL"
SHELL_CMD = "terminal_view_open"


def open_shell(view=None, wnd_ids=set()):
    """ """

    if not view:
        view = sublime.active_window().active_view()

    # remove ids of closed windows, to prevent potential issues
    open_wnds = {w.id() for w in sublime.windows()}
    wnd_ids = wnd_ids & open_wnds

    window = view.window()
    if not window:
        return
    wnd_id = window.id()

    if wnd_id in wnd_ids:
        return

    pr_data = window.project_data()
    if not pr_data:
        return

    try:
        ve_python = pr_data["settings"]["python_interpreter"]
    except:
        return

    if 'virtualenvs' not in ve_python:  # TODO: replace with regexp
        return
    else:
        ve_activate = ve_python.rstrip("python") + "activate"

    terminals = [v for v in window.views() if v.name() == SHELL_TITLE]

    if terminals:  # we are not opening another terminal
        return

    shell_args = {
        "cmd": "/bin/bash --rcfile {}".format(ve_activate),
        "title": SHELL_TITLE
    }

    window.run_command(SHELL_CMD, args=shell_args)
    wnd_ids.add(wnd_id)


class Listener(sublime_plugin.EventListener):
    def on_new_async(self, view):
        print("on_new_async called (AT)")
        open_shell(view)

    def on_load_async(self, view):
        print("on_load_async called (AT)")
        open_shell(view)

    def __call__(self):
        print("plugin_loaded called (AT)")
        open_shell()


def plugin_loaded():
    """ Checking whether TerminalView is installed.
    If not give out status bar message.
    Else start terminal pane. """
    
    if "TerminalView" not in sys.modules:
        msg = "ShellVE: TerminalView not found. Please install."
        print(msg)
        window = sublime.active_window()
        view = window.active_view()
        view.window().status_message(msg)
    else:
        print("ShellVE: TerminalView found")
        Listener()()


class OpenShellVeCommand(sublime_plugin.WindowCommand):
    def run(self):
        open_shell()
