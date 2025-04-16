from application import application_actions

app = application_actions()
app.app_context().push()

if __name__ == "__main__":
    app.run(debug=True)