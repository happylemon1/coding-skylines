from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/run_code", methods=["POST"])
def run_code():
    data = request.json
    code = data.get("code", "")
    try:
        exec_locals = {}
        exec(code, {}, exec_locals)
        output = exec_locals.get("output", None)
        return jsonify({"success": True, "output": output, "building": "house"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
