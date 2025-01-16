from flask import Flask, request
from setlogging import get_logger
import os

app = Flask(__name__)

# Set up logging
LOG_FILE = './webhook_logs.txt'
logger = get_logger(log_file=LOG_FILE)


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    try:
        # Attempt to parse JSON payload
        try:
            data = request.get_json(force=True)
        except Exception:
            logger.error("Malformed JSON payload")
            return "400 Bad Request", 400

        # Validate payload structure
        required_fields = {"incident_id", "status", "updated_at"}
        if not data or not isinstance(data, dict) or not required_fields.issubset(data.keys()):
            logger.error("Invalid payload or missing required fields")
            return "400 Bad Request", 400

        # Log incident_id and status
        incident_id = data["incident_id"]
        status = data["status"]
        logger.info(f"Incident ID: {incident_id}, Status: {status}")

        # Return success response
        return "200 OK", 200

    except Exception as e:
        # Log exception and return generic error message
        logger.error(f"Error processing webhook: {e}")
        return "500 Internal Server Error", 500


if __name__ == "__main__":
    # Ensure log file exists
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
