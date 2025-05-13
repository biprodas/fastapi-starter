import uvicorn

if __name__ == "__main__":
    config = uvicorn.Config("app.api:app", port=8000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
