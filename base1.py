# basics of chat bot / demo 



def chatbot_response(user_input):
    # user_input = name
    # user_input = text
    user_input = user_input.lower()
    # name = input()
    # text = input()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I 'help' you?\n"
    
    # elif user_name in user_input:
    #     print("What's your name?",user_name)
    #     return "Nice to meet you",user_name
    
    elif "help" in user_input:
        return (
            "Here are some commands I understand:\n"
            "Also here are some major probles with there solution, hit 'issues':\n"
            "- 'hello' or 'hi'\n"
            "- 'name'\n"
            "- 'issues'\n"
            "- 'weather'\n"
            "- 'help'\n"
            "- 'bye'"
        )
    elif "issues" in user_input:
        return (
            "Enter the problem number:\n "
            "- '1' or 'Network Connectivity Issues'\n"
            "- '2' or 'System Performance Problems'\n"
            "- '3' or 'Software Not Responding / Crashing'\n"
            "- '4' or 'Password Reset or Account Locked'\n"
            "- '5' or 'Security Concerns / Suspicious Email'\n"
            "- 'bye'"

        )
    elif "1" in user_input or "Network Connectivity Issues" in user_input:
        return (
            "\nCheck if the Wi-Fi is turned on.\n"
                "Restart the router or network adapter.\n"
                "Forget and reconnect to the Wi-Fi network.\n"
                "Check if other devices face the same issue (possible outage).\n"
                "Contact the IT network team if the issue continues.\n"
                )
    
    elif "2" in user_input or "System Performance Problems" in user_input:
        return (
            "\nClose unnecessary apps running in the background.\n"
            "Clear temporary files.\n"
            "Restart the system.\n"
            "Check available storage; keep at least 20%  free.\n"
            "Run antivirus scan to remove malware.\n"
            "Recommend upgrading RAM if hardware is old.\n"
        )
    
    elif "3" in user_input or "Software Not Responding / Crashing" in user_input:
        return (
            "\nForce close and reopen the app.\n"
            "Update the software to the latest version.\n"
            "Clear cache or configuration files.\n"
            "Reinstall the application if needed.\n"
            "Check if there is an official outage or bug reported.\n"
        )
    
    elif "4" in user_input or "Password Reset or Account Locked" in user_input:
        return (
            "\nUse the company’s self-service password reset portal.\n"
            "Follow multi-factor authentication steps.\n"
            "If locked, wait 10–15 minutes and try again.\n"
            "If still locked, create a ticket for the IT support team.\n"
        )
    
    elif "5" in user_input or "Security Concerns / Suspicious Email" in user_input:
        return (
            "\nDo NOT click links or open attachments.\n"
            "Verify the sender’s address.\n"
            "Report the email to the IT security team.\n"
            "Delete the email only after reporting it.\n"
            "Remind about phishing awareness guidelines.\n"
        )
    
    elif "name" in user_input :
        return "I'm Sangchii, Nice to meet you."
    
    elif "weather" in user_input:
        return "I can't check real weather yet, but it's always sunny in Python world!"
    
    elif "bye" in user_input:
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that yet."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")
    
    if user.lower() == "bye":
        print("Chatbot: Have a Great Day , Goodbye!")
        break
    
    print("Chatbot:", chatbot_response(user))
