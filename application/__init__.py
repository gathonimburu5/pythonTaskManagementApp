from application.extension import app, db

def application_actions():
    if app.config["DEBUG"] == "production":
        app.config.from_object("application.configuration.DevelopmentConfig")
    else:
        app.config.from_object("application.configuration.ProductionConfig")

    app.app_context().push()
    db.init_app(app)

    from application.controllers.home_controller import home_blue
    app.register_blueprint(home_blue)

    from application.controllers.comment_controller import comment_ctl
    app.register_blueprint(comment_ctl)

    return app