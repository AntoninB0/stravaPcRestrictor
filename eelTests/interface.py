import eel

# Set web files folder
eel.init('eelTests/web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)




eel.start('main.html', size=(1000, 1000))  # Start