from flask import Flask, render_template, request             #importing class, function from flask

app = Flask(__name__)

@app.route('/')                                              #adding route
@app.route('/<filename>/')
def showfile(filename='file1.txt'):                           #function to read file and display it in html
    start_line = request.args.get('start_line', type=int)
    end_line = request.args.get('end_line', type=int)

    try:
        if filename=='file1.txt' or filename=='file3.txt':         #checking for a particular file and opening it with utf-8 encoding
            with open(filename, 'r',encoding='utf-8') as f:
                lines = f.readlines()
        else:
            with open(filename, 'r',encoding='utf-16') as f:        #opening file with utf-16 encoding
                lines = f.readlines()

        if start_line is not None and end_line is not None:          
            lines = lines[start_line-1:end_line]
        elif start_line is not None:
            lines = lines[start_line-1:]
        elif end_line is not None:
            lines = lines[:end_line]

        content = ''.join(lines)
        return render_template('file.html', content=content)        #displaying html file with render_template function
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
