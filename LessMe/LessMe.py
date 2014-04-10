import sublime, sublime_plugin, os , subprocess

class LessMe(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		filename = view.file_name()
		syntaxPath = view.settings().get('syntax')
		compressed = filepath = ext = syntax = ""

		if filename:
			filepath,exts = os.path.splitext(filename)
			ext = exts[1:]
			compressed = filepath + '.css'
			
		if syntaxPath:
			syntax = os.path.splitext(syntaxPath)[0].split('/')[-1].lower()

		if ext in ['less'] or 'less' in [syntax] :
			self.compile_to_css(filename, compressed, view)


	def compile_to_css(self, source, target, view):
		cmd = " ".join(['lessc','"'+source+'"','"'+target+'"', '--source-map','--no-color'])
		pipe = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
		error = pipe.stderr.read()
		if error:
			message = '[LESS Compile Fail]\n-------------------------\n'
			try:
				message += error.decode()
			except UnicodeDecodeError:
				message += error.decode('gb2312')
			sublime.error_message(message+'-------------------------')
		else:
			sublime.status_message('[LESS Compile Success at: '+target+']')



	
