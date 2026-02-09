from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Data storage
agents_data = {}
pending_commands = {}

@app.route('/')
def dashboard():
    return render_template('index.html', agents=agents_data)

@app.route('/api/report', methods=['POST'])
def report():
    data = request.json
    agent_id = data.get("machine_name")
    agents_data[agent_id] = data
    
    # Check for pending kill commands
    command = pending_commands.pop(agent_id, {"action": "none"})
    return jsonify(command)

@app.route('/api/kill/<agent_id>/<int:pid>', methods=['POST'])
def queue_kill(agent_id, pid):
    pending_commands[agent_id] = {"action": "kill", "pid": pid}
    return jsonify({"status": "queued"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)