from website import create_app 
app = create_app()

# Runs the flask application only if this file is ran, not if the file is imported
if __name__ == "__main__": 
    app.run(debug=True) # Ensures the webserver only runs when condition is met
                        # debug=True is used in development to refresh server whenever 
                        # changes made to code base 