from app import create_app

app = create_app()

@app.route('/')
def index():
    return "Welcome to the Calculator API! Please enter your operation through the URL :URL/operation/number1/number2"

#main function
if __name__ == "__main__":
    print("Registered Routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
    app.run(debug=True)

#comment by afnane 
#comment by wissal
#comment by wissam
#comment by miminaa
#coment comment by wissam