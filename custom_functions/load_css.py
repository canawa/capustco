class LoadCss():
    def load_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

# print(LoadCss().load_file('styles/button_styles.css'))
