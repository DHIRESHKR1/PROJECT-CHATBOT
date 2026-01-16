import re

class RuleBot:
    def __init__(self):
        self.user_name = None

    def respond(self, user_input):
        user_input = user_input.lower()
        response = ""
        buttons = []

        if "hello" in user_input or "hi" in user_input:
            response = "Hello! How can I 'help' you?\n"
            buttons = ["help", "issues", "weather", "bye"]
        
        elif "help" in user_input:
            response = (
                "Here are some commands I understand:\n"
                "Also here are some major problems with their solution, hit 'issues':\n"
                "- 'hello' or 'hi'\n"
                "- 'name'\n"
                "- 'issues'\n"
                "- 'weather'\n"
                "- 'help'\n"
                "- 'bye'"
            )
            buttons = ["issues", "weather", "name", "bye"]
            
        elif "issues" in user_input:
            response = (
                "Enter the problem number:\n "
                "- '1' or 'Network Connectivity Issues'\n"
                "- '2' or 'System Performance Problems'\n"
                "- '3' or 'Software Not Responding / Crashing'\n"
                "- '4' or 'Password Reset or Account Locked'\n"
                "- '5' or 'Security Concerns / Suspicious Email'\n"
                "- 'bye'"
            )
            buttons = ["1", "2", "3", "4", "5", "bye"]

        elif "1" in user_input or "network connectivity issues" in user_input:
            response = (
                "\nCheck if the Wi-Fi is turned on.\n"
                "Restart the router or network adapter.\n"
                "Forget and reconnect to the Wi-Fi network.\n"
                "Check if other devices face the same issue (possible outage).\n"
                "Contact the IT network team if the issue continues.\n"
            )
            buttons = ["issues", "help", "bye"]
        
        elif "2" in user_input or "system performance problems" in user_input:
            response = (
                "\nClose unnecessary apps running in the background.\n"
                "Clear temporary files.\n"
                "Restart the system.\n"
                "Check available storage; keep at least 20% free.\n"
                "Run antivirus scan to remove malware.\n"
                "Recommend upgrading RAM if hardware is old.\n"
            )
            buttons = ["issues", "help", "bye"]

        elif "3" in user_input or "software not responding" in user_input or "crashing" in user_input:
            response = (
                "\nForce close and reopen the app.\n"
                "Update the software to the latest version.\n"
                "Clear cache or configuration files.\n"
                "Reinstall the application if needed.\n"
                "Check if there is an official outage or bug reported.\n"
            )
            buttons = ["issues", "help", "bye"]

        elif "4" in user_input or "password reset" in user_input or "account locked" in user_input:
            response = (
                "\nUse the company’s self-service password reset portal.\n"
                "Follow multi-factor authentication steps.\n"
                "If locked, wait 10–15 minutes and try again.\n"
                "If still locked, create a ticket for the IT support team.\n"
            )
            buttons = ["issues", "help", "bye"]

        elif "5" in user_input or "security concerns" in user_input or "suspicious email" in user_input:
            response = (
                "\nDo NOT click links or open attachments.\n"
                "Verify the sender’s address.\n"
                "Report the email to the IT security team.\n"
                "Delete the email only after reporting it.\n"
                "Remind about phishing awareness guidelines.\n"
            )
            buttons = ["issues", "help", "bye"]

        elif "name" in user_input:
            response = "I'm Sangchii, Nice to meet you."
            buttons = ["help", "issues", "bye"]

        elif "weather" in user_input:
            response = "I can't check real weather yet, but it's always sunny in Python world!"
            buttons = ["help", "issues", "bye"]

        elif "bye" in user_input:
            response = "Goodbye!"
            buttons = []

        else:
            response = "Sorry, I don't understand that yet."
            buttons = ["help", "issues", "bye"]
            
        return response, buttons

def main():
    bot = RuleBot()
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Have a Great Day , Goodbye!")
            break
        
        response, buttons = bot.respond(user_input)
        print(f"Chatbot: {response}")
        if buttons:
            print(f"Options: {buttons}")

if __name__ == "__main__":
    main()
