from flask import g
from server import app


@app.before_request
def add_tests():
    # Setting this to True will load Jasmine and our test file(s)
    g.run_tests = True


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )
