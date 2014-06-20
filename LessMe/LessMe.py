import sublime, sublime_plugin, os , subprocess

class LessMe(sublime_plugin.EventListener):
	def on_post_save_async(self, view):
		filename = view.file_name()
		syntaxPath = view.settings().get('syntax')
		compressed = filepath = ext = syntax = ""

		if not filename:
			return
		else:	
			filepath,exts = os.path.splitext(filename)
			ext = exts[1:]

		if syntaxPath:
			syntax = os.path.splitext(syntaxPath)[0].split('/')[-1].lower()

		if ext in ['less'] or 'less' in [syntax] :
			line = view.substr(view.line(1))
			tag = "//@module"
			moudles = [];
			if line.startswith(tag):
				moudles = (line[len(tag):-1]).split()

			if len(moudles):
				current_dir = os.path.dirname(filename)
				for module in moudles :
					origin = os.path.realpath(os.path.join(current_dir,module))
					if(os.path.exists(origin)):
						compiled = self.get_compiled_file_name(origin)
						self.compile_to_css(origin, compiled)
			else:
				compressed = filepath + '.css'
				self.compile_to_css(filename, compressed)

	def get_compiled_file_name(self,filename):
		filepath,exts = os.path.splitext(filename)
		return filepath + '.css'

	def compile_to_css(self, source, target):
		cmd = " ".join(['lessc','"'+source+'"','"'+target+'"', '--source-map','--no-color'])
		pipe = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
		error = pipe.stderr.read()
		if error:
			message = '[LESS编译失败]\n-------------------------\n'
			try:
				message += error.decode()
			except UnicodeDecodeError:
				message += error.decode('gb2312')
			sublime.error_message(message+'-------------------------')
		else:
			sublime.status_message('[LESS 编译成功: '+target+']')



	
