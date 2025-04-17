from application.extension import app, db

def application_actions():
    if app.config["DEBUG"] == "production":
        app.config.from_object("application.configuration.DevelopmentConfig")
    else:
        app.config.from_object("application.configuration.ProductionConfig")

    app.app_context().push()
    db.init_app(app)

    from application.controllers.dashboard_controller import dashboard_ctrl
    app.register_blueprint(dashboard_ctrl, url_prefix="/")

    from application.controllers.home_controller import home_blue
    app.register_blueprint(home_blue, url_prefix="/tasks")

    from application.controllers.comment_controller import comment_ctl
    app.register_blueprint(comment_ctl, url_prefix="/comment")

    return app