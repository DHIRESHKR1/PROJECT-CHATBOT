#backend code

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return (
            "Hello! How can I help you?",
            ["help", "name", "issues", "weather", "bye"]
        )

    elif "help" in user_input:
        return (
            "Here are some commands I understand:",
            ["hello", "name", "issues", "weather", "bye"]
        )

    elif "issues" in user_input:
        return (
            "Select a problem:",
            ["1", "2", "3", "4", "5", "bye"]
        )

    elif user_input == "1":
        return (
            "Network Connectivity Issues:",
            ["Restart router", "Check Wi-Fi", "Contact IT", "bye"]
        )

    elif user_input == "2":
        return (
            "System Performance Problems:",
            ["Restart system", "Clear storage", "Upgrade RAM", "bye"]
        )

    elif user_input == "3":
        return (
            "Software Crashing:",
            ["Restart app", "Update software", "Reinstall", "bye"]
        )

    elif user_input == "4":
        return (
            "Password Reset / Account Locked:",
            ["Reset password", "Wait 15 minutes", "Contact IT", "bye"]
        )

    elif user_input == "5":
        return (
            "Security Concerns:",
            ["Report email", "Delete email", "Security guidelines", "bye"]
        )

    elif "name" in user_input:
        return (
            "I'm Sangchii, nice to meet you 😊",
            ["help", "issues", "bye"]
        )

    elif "weather" in user_input:
        return (
            "It's always sunny in the Python world ☀️",
            ["help", "bye"]
        )

    elif "bye" in user_input:
        return (
            "Have a great day! 👋",
            []
        )

    else:
        return (
            "Sorry, I don't understand that.",
            ["help", "bye"]
        )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response, buttons = chatbot_response(user_input)
    return jsonify({"response": response, "buttons": buttons})


if __name__ == "__main__":
    app.run(debug=True)
