from app import create_app

app = create_app()

if __name__ == "__main__":
    port = app.config.get("PORT", 5000)
    debug = app.config.get("DEBUG", False)
    app.run(debug=debug, port=port, host="0.0.0.0")