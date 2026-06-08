from ursina import Text, Ursina

app = Ursina(title="main")
app_test = Ursina(title="secondary")

app.run()
app_test.run()