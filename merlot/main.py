from merlot import create_app

merlot = create_app()

if __name__ == '__main__':
    merlot.run(debug=True)
