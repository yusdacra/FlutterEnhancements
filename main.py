import sublime
import sublime_plugin
import subprocess

class FlutterHotReloadCommand(sublime_plugin.WindowCommand):
	def run(self):
		subprocess.call(["bash", "-c", ("kill -SIGUSR1 {0}").format(int(subprocess.check_output(["cat", "./.flutter.pid"])))])

class FlutterHotRestartCommand(sublime_plugin.WindowCommand):
	def run(self):
		subprocess.call(["bash", "-c", ("kill -SIGUSR2 {0}").format(int(subprocess.check_output(["cat", "./.flutter.pid"])))])

class FlutterHotReloadWhenSaved(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		view.window().run_command("flutter_hot_reload")