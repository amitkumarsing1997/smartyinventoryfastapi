import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        # "src.app.app:app",
        "smartinventoryfastapi.app2:app",
        host="0.0.0.0",
        # host="localhost",
        port=8000,
        reload=True
    )
